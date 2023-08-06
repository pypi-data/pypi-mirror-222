import numpy as np
import importlib
from scipy.interpolate import griddata
from finesse.utilities.maps import (
    overlap_tilt_coefficients,
    read_metropro_file,
    overlap_piston_coefficient,
)
import pathlib
import finesse


def get_test_mass_surface_profile(test_mass):
    """Loads a surface profile of a test mass optic measured by a Zygo inteferometer.
    This surface profile data is the relative to a perfect sphere for the ideal radius
    of curvature for the mirror. Values outside the 160mm radius are given a NaN value.

    Parameters
    ----------
    test_mass : str
        LIGO test mass name and serial number, ITM01, ETM13, etc.

    Returns
    -------
    x, y : array_like
        1D array of map coordinates
    A : array_like
        2D array of map surface profile in meters

    Notes
    -----
    ITM maps have negative sign applied to match with typical LIGO like FINESSE
    models where positive z direction point towards the BS.
    """
    import h5py

    datapath = pathlib.Path(finesse.config.config_instance()["finesse.data"]["path"])
    filepath = datapath / "finesse-ligo" / (test_mass + ".h5")
    filepath = filepath.expanduser().absolute()
    if not filepath.exists():
        raise FileNotFoundError(
            f"Could not find {filepath}.\n\nUse finesse_ligo.download('{str(test_mass)}.h5') to try and download it."
        )

    with h5py.File(filepath, "r") as data:
        x = np.array(data["x"])
        y = np.array(data["y"])
        A = np.array(data["A"])
    return x, y, A


def get_test_mass_surface_profile_interpolated(
    test_mass, nan_value=0, make_axisymmetric=False
):
    """Loads a surface profile of a test mass optic measured by a Zygo inteferometer.
    This surface profile data is the relative to a perfect sphere for the ideal radius
    of curvature for the mirror.

    Parameters
    ----------
    test_mass : str
        LIGO test mass name and serial number, ITM01, ETM13, etc.
    nan_value : float, optional
        Value to replace NaNs with to allow for interpolation beyond radius
    make_axisymmetric : bool, optional
        If True, return a 2D interpolator that averages the surface profile radially.
        This makes the map axisymmetric to remove any odd-mode couplings.

    Returns
    -------
    surface_function : callable(x,y)
        Function that interpolates data for the a given test mass profile.

    Notes
    -----
    ITM maps have negative sign applied to match with typical LIGO like FINESSE
    models where positive z direction point towards the BS.
    """
    from scipy.interpolate import RectBivariateSpline

    x, y, A = get_test_mass_surface_profile(test_mass)
    A[np.isnan(A)] = nan_value
    interpolator = RectBivariateSpline(
        x, y, A.T if "ETM" in test_mass else -A.T, kx=1, ky=1
    )
    if make_axisymmetric:
        # Make radial samples over which to average
        r = np.linspace(0, min((max(x), max(y))), len(x) // 2)
        phi = np.linspace(-np.pi, np.pi, len(x) // 2)
        R, PHI = np.meshgrid(r, phi)
        X = R * np.cos(PHI)
        Y = R * np.sin(PHI)
        A = interpolator(X, Y, grid=False)
        A_r = A.mean(0)
        # Project back onto original grid size
        XX, YY = np.meshgrid(x, y)
        RR = np.sqrt(XX**2 + YY**2)
        Z = np.interp(RR, r, A_r)
        interpolator = RectBivariateSpline(x, y, Z.T, kx=1, ky=1)
    return interpolator


def O5_nominal_surface_profile_functions():
    """Returns functions that can be used to compute the surface profile of the the LIGO
    test masses. These surface profiles are the nominally expected ones for O5. This is
    before any corrective polishing has taken place. These surface profiles are
    relatively flat in the center but rapidly change towards the edges of the mirror.

    Notes
    -----
    The returned ITM surface profile will appear opposite to the ETM. This is done so
    because in FINESSE typically the ITM and ETM have the oppositee z coordinate system.
    Negative values on the ITM surface make the arm cavity shorter.

    The raw data for this surface profile can be retrieved using:

    >>> with importlib.resources.path(
    ...     "finesse_ligo.data.maps", "O5_nominal_surface_profiles.npz"
    ... ) as datafile:
    ...     data = np.load(datafile)

    Returns
    -------
    f_surface_itm : callable(x,y)
        Function that can be called to compute the interpolated data for the ITM surface profile
    f_surface_itm : callable(x,y)
        Function that can be called to compute the interpolated data for the ETM surface profile

    Examples
    --------
    A typical use case to generate a 2D map of the surface profiles

    >>> sx, sy = finesse.ligo.maps.O5_nominal_surface_profile_functions()
    >>> x = np.linspace(-0.16, 0.16, 100)
    >>> X, Y = np.meshgrid(x,x)
    >>> plt.imshow(sx(X,Y))
    """
    with importlib.resources.path(
        "finesse_ligo.data.maps", "O5_nominal_surface_profiles.npz"
    ) as datafile:
        data = np.load(datafile)

    ITM = data["ITM"]
    ETM = data["ETM"]
    r = data["r"]

    f_surface_itm = lambda x, y: np.interp(
        np.sqrt(np.atleast_1d(x) ** 2 + np.atleast_1d(y) ** 2), r, -ITM
    )
    f_surface_etm = lambda x, y: np.interp(
        np.sqrt(np.atleast_1d(x) ** 2 + np.atleast_1d(y) ** 2), r, ETM
    )

    return f_surface_itm, f_surface_etm


def process_ligo_zygo_binary_data(filename, spot_size_weight):
    """Takes LIGO Zygo map data (binary .dat format) and processes. The processing
    strips noisy data from the edge of the measurement and removes tilt. It returns the
    inner 320mm diameter of the mirror. Assuming anything out this bounds has zero
    reflectivity.

    Parameters
    ----------
    filename : str
        Name of .dat file of MetroPro binary Zygo data to process

    spot_size_weight : float
        Spot size to use for weighting the tilt removal

    Returns
    -------
    x, y : array_like
        x and y 1D arrays for the map points

    A : array_like
        2D array of mirror surface displacement relative to some reference sphere.
        Units are in meters.

    Examples
    --------
    This function was designed to work with MetroPro data taken of various LIGO optics.
    For example, these can be downloaded from DCC entries like LIGO-E1700257, and using
    files ITM01_S1-P_160.dat.

    Notes
    -----
    If any NaN values are present in the central 160mm radius this code will perform
    a 2D linear interpolation over each NaN point. This uses scipy griddata which
    is not particularly fast.
    """
    A, data = read_metropro_file(filename)

    Nx = data["Nx"]
    Ny = data["Ny"]

    x_extent = data["cameraRes"] * Nx
    y_extent = data["cameraRes"] * Ny

    x = np.linspace(-x_extent / 2, x_extent / 2, Nx)
    y = np.linspace(-y_extent / 2, y_extent / 2, Ny)
    X, Y = np.meshgrid(x, y)

    R = np.sqrt(X**2 + Y**2)
    A[R > 0.16] = 0

    nan_idx = np.isnan(A.flat)

    if np.any(nan_idx):
        # If any nans, interpolate them away
        not_nan_idx = ~nan_idx
        points = np.vstack((X.flat[not_nan_idx], Y.flat[not_nan_idx])).T
        values = A.flat[not_nan_idx]
        xi = np.vstack((X.flat[nan_idx], Y.flat[nan_idx])).T
        A.flat[nan_idx] = griddata(points, values, xi, method="linear")

    yaw, pitch = overlap_tilt_coefficients(x, y, A, weight_spot=spot_size_weight)
    piston = overlap_piston_coefficient(x, y, A, weight_spot=spot_size_weight)
    A -= yaw * X + pitch * Y + piston
    A[R > 0.16] = np.nan
    # Remove all rows/cols that are just NaN
    # should be left with just data in the 160mm
    # radius for the mirror
    idx_x = ~np.all(np.isnan(A), axis=0)
    idx_y = ~np.all(np.isnan(A), axis=1)
    A = A[:, idx_x]
    A = A[idx_y, :]
    new_x = x[idx_x]
    new_y = y[idx_y]
    return np.linspace(-0.16, 0.16, new_x.size), np.linspace(-0.16, 0.16, new_y.size), A


def aligo_O4_BS_AR_baffle(r_lim=0.21, N=300, AoI=45, offset_direction=1):
    """Square amplitude map representing the Advanced LIGO beamsplitter (O4) anti-
    reflective side baffle. It is two offset ellipses that is at 45 degrees to the beams
    in the X and signal recycling paths. See https://dcc.ligo.org/LIGO-D1200703.

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction
    AoI : float
        Degrees of angle of incident of beam relative to baffle
    offset_direction : int
        Whether the other baffle hole is in the positive to negative direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    bs_ar_baffle : array_like
        2D amplitude map
    """
    x = np.linspace(-r_lim, r_lim, N)
    X, Y = np.meshgrid(x, x)
    inches_2_m = 25.4e-3
    r_major = 11.69 / 2 * inches_2_m * np.cos(np.deg2rad(AoI))
    r_minor = 10.236 / 2 * inches_2_m
    x_offset = offset_direction * 2 * 2.74 * inches_2_m * np.cos(np.deg2rad(AoI))

    ellipse = (X / r_major) ** 2 + (Y / r_minor) ** 2  # hole main beam goes through
    ellipse_offset = ((X - x_offset) / r_major) ** 2 + (Y / r_minor) ** 2  # other hole
    bs_ar_baffle = np.ones_like(X)

    bs_ar_baffle[np.logical_and(ellipse > 1, ellipse_offset > 1)] = 0
    return x, bs_ar_baffle


def aligo_O4_BS_HR_baffle(r_lim=0.21, N=300, AoI=45, offset_direction=1):
    """Square amplitude map representing the Advanced LIGO beamsplitter (O4) high-
    reflective side baffle. It is two offset ellipses that is at 45 degrees to the beams
    in the X and signal recycling paths. See https://dcc.ligo.org/LIGO-D1200704. Main
    difference between HR and AR baffles is the 1.433" vs 2.74" separation of the two
    ellipses.

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction
    AoI : float
        Degrees of angle of incident of beam relative to baffle
    offset_direction : int
        Whether the other baffle hole is in the positive to negative direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    bs_ar_baffle : array_like
        2D amplitude map
    """
    x = np.linspace(-r_lim, r_lim, N)
    X, Y = np.meshgrid(x, x)
    inches_2_m = 25.4e-3
    r_major = 11.69 / 2 * inches_2_m * np.cos(np.deg2rad(AoI))
    r_minor = 10.236 / 2 * inches_2_m
    x_offset = offset_direction * 2 * 1.433 * inches_2_m * np.cos(np.deg2rad(AoI))

    ellipse = (X / r_major) ** 2 + (Y / r_minor) ** 2  # hole main beam goes through
    ellipse_offset = ((X - x_offset) / r_major) ** 2 + (Y / r_minor) ** 2  # other hole
    bs_ar_baffle = np.ones_like(X)

    bs_ar_baffle[np.logical_and(ellipse > 1, ellipse_offset > 1)] = 0
    return x, bs_ar_baffle


def aligo_O4_ITM_baffle(r_lim=0.21, N=300):
    """Square amplitude map representing the Advanced LIGO (O4) ITM elliptic baffle.

    See:
    https://dcc.ligo.org/DocDB/0026/D1003238/005/D1003238-v5.PDF
    https://dcc.ligo.org/D1101804

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    baffle : array_like
        2D amplitude map
    """
    x = np.linspace(-r_lim, r_lim, N)
    X, Y = np.meshgrid(x, x)
    inches_2_m = 25.4e-3
    r_major = 10.79 / 2 * inches_2_m
    r_minor = 8.818 / 2 * inches_2_m

    ellipse = (X / r_minor) ** 2 + (Y / r_major) ** 2
    baffle = np.ones_like(X)

    baffle[ellipse > 1] = 0
    return x, baffle


def aligo_O4_ESD_inner_aperture(r_lim=0.21, N=300):
    """Square amplitude map representing the Advanced LIGO (O4) inner aperture of the
    ESD pattern found on the compensation plate.

    See:
    https://dcc.ligo.org/LIGO-D080177

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    baffle : array_like
        2D amplitude map
    """
    assert r_lim >= 266e-3 / 2
    x = np.linspace(-r_lim, r_lim, N)
    X, Y = np.meshgrid(x, x)
    r_major = 266e-3 / 2
    r_minor = 266e-3 / 2

    ellipse = (X / r_minor) ** 2 + (Y / r_major) ** 2  # hole main beam goes through
    baffle = np.ones_like(X)

    baffle[ellipse > 1] = 0
    return x, baffle


def aligo_O4_BS_to_ITMX_baffle(r_lim=0.14, N=200):
    """Combines the ITM elliptical, BS AR, and ESD apertures to make an aperture map for
    the baffling between ITMX and BS AR.

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    baffle : array_like
        2D amplitude map
    """

    x, BS_AR = aligo_O4_BS_AR_baffle(r_lim=r_lim, N=N)
    x, ITM_ELLIP = aligo_O4_ITM_baffle(r_lim=r_lim, N=N)
    x, CP_ESD = aligo_O4_ESD_inner_aperture(r_lim=r_lim, N=N)

    BS_ITM_BAFFLE = np.bitwise_and(
        BS_AR.astype(bool), ITM_ELLIP.astype(bool), CP_ESD.astype(bool)
    )
    return x, BS_ITM_BAFFLE


def aligo_O4_BS_to_ITMY_baffle(r_lim=0.14, N=200):
    """Combines the ITM elliptical, BS HR, and ESD apertures to make an aperture map for
    the baffling between ITMY and BS HR.

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    baffle : array_like
        2D amplitude map
    """

    x, BS_AR = aligo_O4_BS_HR_baffle(r_lim=r_lim, N=N)
    x, ITM_ELLIP = aligo_O4_ITM_baffle(r_lim=r_lim, N=N)
    x, CP_ESD = aligo_O4_ESD_inner_aperture(r_lim=r_lim, N=N)

    BS_ITM_BAFFLE = np.bitwise_and(
        BS_AR.astype(bool), ITM_ELLIP.astype(bool), CP_ESD.astype(bool)
    )
    return x, BS_ITM_BAFFLE


def aligo_O4_PR3_SR3_baffle(r_lim=0.14, N=200):
    """Amplitude map for the SR3 or PR3 baffle.

    See: https://dcc.ligo.org/D1700238

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    baffle : array_like
        2D amplitude map
    """
    in_2_m = 25.4e-3
    r_x = 265.03e-3 / 2
    r_y = 264.9e-3 / 2
    assert r_lim >= r_x and r_lim >= r_y
    x = np.linspace(-r_lim, r_lim, N)
    X, Y = np.meshgrid(x, x)

    ellipse = (X / r_x) ** 2 + (Y / r_y) ** 2
    baffle = np.ones_like(X)
    baffle[np.bitwise_and(X > 2.29 * in_2_m, Y > 3.89 * in_2_m)] = 0
    baffle[np.bitwise_and(X > 2.29 * in_2_m, Y < -3.85 * in_2_m)] = 0
    baffle[np.bitwise_and(X < -2.29 * in_2_m, Y > 3.89 * in_2_m)] = 0
    baffle[np.bitwise_and(X < -2.29 * in_2_m, Y < -3.85 * in_2_m)] = 0
    baffle[ellipse > 1] = 0
    return x, baffle


def aligo_O4_TM_aperture(r_lim=0.16, N=300):
    """Square amplitude map representing the Advanced LIGO (O4) test mass coated
    apertures.

    Parameters
    -----------
    r_lim : float
        Limit of map in each direction radially
    N : int
        Number of sample points along each direction

    Returns
    -------
    x : array_like
        1D array for dimensions of map in both directions
    baffle : array_like
        2D amplitude map
    """
    x = np.linspace(-r_lim, r_lim, N)
    X, Y = np.meshgrid(x, x)
    r_major = 0.16
    r_minor = 0.16

    ellipse = (X / r_minor) ** 2 + (Y / r_major) ** 2
    baffle = np.ones_like(X)
    baffle[ellipse > 1] = 0
    return x, baffle
