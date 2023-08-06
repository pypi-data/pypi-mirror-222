import numpy as np
from finesse.components import DegreeOfFreedom
from more_itertools import roundrobin


def arm_g_factors(model):
    """Calculates the 'g-factors' for each arm.

    ..math::

        g = 1 - L/Rc

    Parameters
    ----------
    model: :class:`finesse.Model`
        LIGO model that includes X and Y arm to get values from

    Returns
    -------
    g_itmx, g_etmx, g_itmy, g_etmy : float
        g-factors for the x and y arm

    Notes
    -----
    See technical notes and papers:
        - https://dcc.ligo.org/LIGO-T0900511/public
        - https://doi.org/10.1364/AO.49.003474
    """
    g_itmx = 1 - float(model.LX.L.value / np.abs(model.ITMX.Rcx.value))
    g_etmx = 1 - float(model.LX.L.value / np.abs(model.ETMX.Rcx.value))
    g_itmy = 1 - float(model.LY.L.value / np.abs(model.ITMY.Rcy.value))
    g_etmy = 1 - float(model.LY.L.value / np.abs(model.ETMY.Rcy.value))
    return g_itmx, g_etmx, g_itmy, g_etmy


def arm_r_factors(model):
    """Calculates the 'r-factors' of each arm for ASC calculations.

    Parameters
    ----------
    model: :class:`finesse.Model`
        LIGO model that includes X and Y arm to get values from

    Returns
    -------
    rx, ry : float
        r-factors for the x and y arm

    Notes
    -----
    See technical notes and papers for ASC:
        - https://dcc.ligo.org/LIGO-T0900511/public
        - https://doi.org/10.1364/AO.49.003474
    """
    g_itmx, g_etmx, g_itmy, g_etmy = arm_g_factors(model)
    rx = 2 / ((g_itmx - g_etmx) + np.sqrt((g_etmx - g_itmx) ** 2 + 4))
    ry = 2 / ((g_itmy - g_etmy) + np.sqrt((g_etmy - g_itmy) ** 2 + 4))
    return rx, ry


def add_arm_ASC_DOFs(
    model, ITMX_drive, ETMX_drive, ITMY_drive, ETMY_drive, *, output_matrix=None
):
    """Adds the angular degree of freedom elements to decribe the common and
    differential HARD and SOFT modes. These are defined for right-handed coordinate
    systems where the positive-z normal vectors points out of the front (p1) surface of
    a mirror element. This code assumes that both the ITM and ETM z vectors point into
    the cavity and towards each other.

    Parameters
    ----------
    model: :class:`finesse.Model`
        LIGO model that includes X and Y arm to get values from

    ITMX_drive, ETMX_drive, ITMY_drive, ETMY_drive : :class:`LocalDegreeOfFreedom`
        Local degree of freedom on a mirror element to drive for each optic.
        Typically this is driving to some mirror input via a torque and reads
        out the mirror position.

    output_matrix: dict[str: [tuple|list]]
        This should be a dictionary that describes for each ASC arm DOF
        which test mass drive factors to use. It should contain keyes for
        CHARD_P, CSOFT_P, DHARD_P, DSOFT_P, CHARD_Y, CSOFT_Y, DHARD_Y,
        and DSOFT_P. The value of the dict should be four factors in the
        order of (ITMX, ETMX, ITMY, ETMY). For example:
            `"CHARD_P": (-1,  +rx, -1,  +ry)`

    Notes
    -----
    See https://dcc.ligo.org/LIGO-D2200425/public for a diagram of arm modes.

    See technical notes and papers for ASC:
        - https://dcc.ligo.org/LIGO-T0900511/public
        - https://doi.org/10.1364/AO.49.003474

    Returns
    -------
    CHARD_P, CSOFT_P, DHARD_P, DSOFT_P, CHARD_Y, CSOFT_Y, DHARD_Y, DSOFT_Y: :class:`DegreeOfFreedom`
        Returns the degree of freedom elements added to the model
    """
    drives = (ITMX_drive, ETMX_drive, ITMY_drive, ETMY_drive)
    rx, ry = arm_r_factors(model)
    if output_matrix is None:
        output_matrix = {
            # PITCH     IX   EX   IY   EY
            "CHARD_P": (-1, +rx, -1, +ry),
            "CSOFT_P": (+rx, +1, +ry, +1),
            "DHARD_P": (-1, +rx, +1, -ry),
            "DSOFT_P": (+rx, +1, -ry, -1),
            # YAW       IX   EX   IY   EY
            "CHARD_Y": (+1, +rx, -1, -ry),
            "CSOFT_Y": (+rx, -1, -ry, +1),
            "DHARD_Y": (+1, +rx, +1, +ry),
            "DSOFT_Y": (+rx, -1, +ry, -1),
        }

    # loop through everything and add the DOF elements
    for DOF, factors in output_matrix.items():
        model.add(DegreeOfFreedom(DOF, *roundrobin(drives, factors)))

    return (
        model.CHARD_P,
        model.CSOFT_P,
        model.DHARD_P,
        model.DSOFT_P,
        model.CHARD_Y,
        model.CSOFT_Y,
        model.DHARD_Y,
        model.DSOFT_Y,
    )
