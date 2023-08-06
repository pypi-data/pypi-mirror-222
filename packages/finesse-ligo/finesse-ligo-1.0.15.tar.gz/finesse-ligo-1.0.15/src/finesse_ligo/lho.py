import finesse
import numpy as np
import importlib.resources
from finesse.detectors import MathDetector
from finesse.symbols import Constant

from finesse.analysis.actions import OptimiseRFReadoutPhaseDC, Xaxis


def make_O4_lho(
    RF_AS_readout=False, verbose=False, katscript=None, positive_ITM_Rc=True
):
    base = finesse.Model()
    if katscript is None:
        if positive_ITM_Rc:
            base.parse(
                importlib.resources.read_text(
                    "finesse_ligo.katscript", "aligo_reversed_itm.kat"
                )
            )
        else:
            base.parse(
                importlib.resources.read_text("finesse_ligo.katscript", "aligo.kat")
            )
    else:
        base.parse(katscript)

    # Gives a PRC lenth of 57.6508±0.0007m
    base.f1.value = 9100230

    # Nominal Design RoCs for reference
    # ---------------------------------
    # ITMX 1934
    # ETMX 2245
    # PR3 36.027
    # PR2 -4.545
    # PRM 11.009
    # SR3 35.972841
    # SR2 -6.406
    # SRM -5.6938
    # ---------------------------------------------------------------
    # From Galaxy https://galaxy.ligo.caltech.edu/optics/
    # https://dcc.ligo.org/DocDB/0141/T1700149/008/ITM_summary-v8.pdf
    # ---------------------------------------------------------------
    # CP-O1 + ITM-07 substrate lens
    base.ITMXlens.f = 1 / (1 / 664e3 - 1 / 310812)
    base.ITMX.Rc = 1940.3 if positive_ITM_Rc else -1940.3
    base.ITMX.T = 0.015
    base.ITMX.R = 1 - base.ITMX.L.ref - base.ITMX.T.ref

    # CP-O4 + ITM-01 substrate lens
    base.ITMYlens.f = 1 / (1 / 69.6e3 - 1 / 92780)
    base.ITMY.Rc = 1940.2 if positive_ITM_Rc else -1940.2
    base.ITMY.T = 0.015
    base.ITMY.R = 1 - base.ITMY.L.ref - base.ITMY.T.ref

    # ETM-13
    base.ETMX.Rc = 2244.2
    base.ETMX.T = 4e-6
    base.ETMX.R = 1 - base.ETMX.L.ref - base.ETMX.T.ref
    # ETM-16
    base.ETMY.Rc = 2246.9
    base.ETMY.T = 4e-6
    base.ETMY.R = 1 - base.ETMY.L.ref - base.ETMY.T.ref
    # PR3-01
    base.PR3.Rc = 36.021
    base.PR3.T = 4e-6
    base.PR3.R = 1 - base.PR3.L.ref - base.PR3.T.ref
    # PR2-04
    base.PR2.Rc = -4.543
    base.PR2.T = 230e-6
    base.PR2.R = 1 - base.PR2.L.ref - base.PR2.T.ref
    # PRM-04
    base.PRM.Rc = 10.948
    base.PRM.T = 0.031
    base.PRM.R = 1 - base.PRM.L.ref - base.PRM.T.ref
    # SR3-02
    base.SR3.Rc = 36.013
    # SR2-03
    base.SR2.Rc = -6.424
    # SRM-06
    base.SRM.Rc = -5.678

    base.OM1.Rc = 4.6  # E1100056-v2-02
    # TSAMS installation https://alog.ligo-wa.caltech.edu/aLOG/index.php?callRep=65004 16/09/2022
    base.OM2.Rc = 1.7  # E1100056-v2-01, this is also a TSAMs mirror so RoC can change
    base.OM3.Rc = np.inf  # E1000457-v1
    base.OM3.set_RTL(R=0.99, T=0.01, L=0)

    base.nsilica.value = 1.44963
    base.lmich.value = np.nan

    # E1300128-v4 for lengths which include the SRM/SR2 shifts
    base.LX.L.value = 3999498e-3
    base.LY.L.value = 3999468.1e-3

    # Total optical length should be lPRC.value = 57651.3e-3 for reference
    base.LPR23.value = 16162.6e-3
    base.LPR3BS.value = 19537.4e-3
    base.lp1.L.value = 16608.6e-3

    # Total optical length should be lSRC.value = 56008.5e-3 for reference
    base.LSR23.value = 15460.1e-3
    base.LSR3BS.value = 19365.8e-3
    base.ls1.L.value = 15740e-3

    # + extra CP to ITM distance
    base.lx1.L.value = 4829.6e-3 + 20e-3
    base.ly1.L.value = 4847.8e-3 + 20e-3

    # Make ITM substrate a bit thicker to include CP
    base.ITMXsub.L = (99.82 + 200.22) * 1e-3
    base.ITMYsub.L = (99.91 + 199.64) * 1e-3
    base.BSsub1.L = 60.41e-3 / np.cos(np.deg2rad(29.186885954108114))
    base.BSsub2.L = 60.41e-3 / np.cos(np.deg2rad(29.186885954108114))

    if positive_ITM_Rc:
        ITMX_AR_IN = base.ITMX.p2.i
        ITMY_AR_IN = base.ITMY.p2.i
    else:
        ITMX_AR_IN = base.ITMX.p1.i
        ITMY_AR_IN = base.ITMY.p1.i

    lx = base.path(base.BS.p3, ITMX_AR_IN)
    ly = base.path(base.BS.p2, ITMY_AR_IN)
    base.lschnupp.value = (lx.optical_length - ly.optical_length).eval()
    spx = base.path(base.SRM.p1.o, ITMX_AR_IN)
    spy = base.path(base.SRM.p1.o, ITMY_AR_IN)
    ppx = base.path(base.PRM.p2.o, ITMX_AR_IN)
    ppy = base.path(base.PRM.p2.o, ITMY_AR_IN)
    base.lSRC.value = (spx.optical_length + spy.optical_length) / 2
    base.lPRC.value = (ppx.optical_length + ppy.optical_length) / 2

    # Design lengths for output path
    # Taken from https://dcc.ligo.org/DocDB/0095/T1200410/002/T1200410-v2.pdf
    # SRM to OM1 = 3.571m
    # OM1 to OM2 = 4.966 - 3.571 = 1.395m
    # OM2 to OM3 = 5.674 - 4.966 = 0.708m
    # OM3 to OMC waist = 5.936 - 5.674 = 0.262m
    # but we need OM3 to OMC input coupler. The OMC mode is 140mm past the OMC IC.
    # so the distance from OM3 to OMC IC should be 0.122m

    # Distances from Zemax SRM to polarizer: Corey email
    # plus some measurements from in chamber during O3+O4
    # base.sSRM_OFI.L = 0.9046
    # base.sOFI_OM1.L = 3.45 - base.sSRM_OFI.L
    # base.sOM1_OM2.L = 1.39 # 1.39m Measured by Dan, Danny, TVo, Terra ~ 14th April 2018
    # base.sOM2_OM3.L = 0.63 # Measured by Shelia ~17th April 2018
    # base.sOM3_OMC.L = 0.117 + 0.2 # Unclear where these numbers came from, one measured
    # from OM3 to the OMC cage then a guess at how far it
    # is to the OMC input coupler

    # https://dcc.ligo.org/LIGO-E2100383-v3
    # A+_D0901129_23 AUG 2021, OM1-3 +SRM and OMC PRISM.STEP
    base.sSRM_OFI.L = 0.9046
    base.sOFI_OM1.L = 3.440 - base.sSRM_OFI.L
    base.sOM1_OM2.L = 1.492
    base.sOM2_OM3.L = 0.654
    base.sOM3_OMC.L = (
        0.276  # distance to OM3 to first tombstone on OMC breadboard
        + 0.03  # guess about 3cm from tombstone refl to OMC input coupler
    )

    base.phase_level = 2
    base.add(MathDetector("cost_prcl", Constant(base.Pprc_9) * Constant(base.Px)))

    return base


def add_AS_WFS(model):
    """Adds in AS WFS path on transmission of OM3, 1 lens L101,
    1 beamsplitter M101 and AS A and B
    References: DCC D1000342 and T1000247
    Adds in correct path to AS_C QPD (includes lens and beamsplitter)
    Reference: T1200410
    Also adds additional AS port ASC dofs (SRC and MICH)
    """
    model.parse(
        """
        # lens in transmission of OM1
        lens AS_L1 f=334e-3

        # lens in transmission of OM3
        lens AS_L101 f=334e-3

        # add in BS between AS A and AS B WFS
        bs AS_M101 R=0.5 T=0.5

        # add in BS between OM1 and AS_C lens
        bs AS_M6 R=0.5 T=0.5

        # set up nothing at AS A and B to put WFS, C for QPD
        nothing AS_A
        nothing AS_B
        nothing AS_C

        # create WFS A and B at placeholder location
        # only includes 45 and 36  MHz WFS (used for DHARD and MICH ASC)
        # could be updated to include 72 MHz (118-45, requires addition of 13th order demod to model)
        readout_rf AS_A_WFS45x optical_node=AS_A.p1.i f=f2 pdtype=xsplit output_detectors=true
        readout_rf AS_A_WFS45y optical_node=AS_A.p1.i f=f2 pdtype=ysplit output_detectors=true
        readout_rf AS_B_WFS45x optical_node=AS_B.p1.i f=f2 pdtype=xsplit output_detectors=true
        readout_rf AS_B_WFS45y optical_node=AS_B.p1.i f=f2 pdtype=ysplit output_detectors=true
        readout_rf AS_A_WFS36x optical_node=AS_A.p1.i f=f2-f1 pdtype=xsplit output_detectors=true
        readout_rf AS_A_WFS36y optical_node=AS_A.p1.i f=f2-f1 pdtype=ysplit output_detectors=true
        readout_rf AS_B_WFS36x optical_node=AS_B.p1.i f=f2-f1 pdtype=xsplit output_detectors=true
        readout_rf AS_B_WFS36y optical_node=AS_B.p1.i f=f2-f1 pdtype=ysplit output_detectors=true
        readout_rf AS_A_WFS72x optical_node=AS_A.p1.i f=f2-f1 pdtype=xsplit output_detectors=true
        readout_rf AS_A_WFS72y optical_node=AS_A.p1.i f=f3-f2 pdtype=ysplit output_detectors=true
        readout_rf AS_B_WFS72x optical_node=AS_A.p1.i f=f2-f1 pdtype=xsplit output_detectors=true
        readout_rf AS_B_WFS72y optical_node=AS_A.p1.i f=f3-f2 pdtype=ysplit output_detectors=true

        # AS_C QPD created at placeholder
        readout_dc AS_Cy optical_node=AS_C.p1.i pdtype=ysplit output_detectors=true
        readout_dc AS_Cx optical_node=AS_C.p1.i pdtype=xsplit output_detectors=true

        # ASC dofs sensed at the AS port
        dof SRC1_P SRM.dofs.pitch +1
        dof SRC1_Y SRM.dofs.yaw +1
        dof SRC2_P SRM.dofs.pitch +1 SR2.dofs.pitch -7.6
        dof SRC2_Y SRM.dofs.yaw +1 SR2.dofs.yaw 7.1
        dof MICH_P BS.dofs.pitch +1
        dof MICH_Y BS.dofs.yaw +1
    """
    )
    model.connect(model.OM3.p3, model.AS_L101.p1, L=605e-3)
    model.connect(model.AS_L101.p2, model.AS_M101.p1)
    model.connect(model.AS_M101.p2, model.AS_A.p1, L=191e-3)
    model.connect(model.AS_M101.p3, model.AS_B.p1, L=475e-3)
    model.connect(model.OM1.p3, model.AS_M6.p1)
    model.connect(model.AS_M6.p3, model.AS_L1.p1, L=670e-3)
    model.connect(model.AS_L1.p2, model.AS_C.p1, L=225e-3)

    model.parse(
        """
        # Amplifiers
        amplifier AS_A_WFS45x_G gain=1
        amplifier AS_A_WFS45y_G gain=1
        amplifier err_DHARD_P gain=1
        amplifier err_DHARD_Y gain=1
    """
    )

    # Add amplifiers to AS_A WFS
    model.connect(model.AS_A_WFS45x.Q, model.AS_A_WFS45x_G.p1)
    model.connect(model.AS_A_WFS45y.Q, model.AS_A_WFS45y_G.p1)

    # Summing node to create DHARD
    model.connect(model.AS_A_WFS45x_G.p2, model.err_DHARD_P.p1)
    model.connect(model.AS_A_WFS45y_G.p2, model.err_DHARD_Y.p1)
    return model


def add_REFL_path(model):
    """Adds in REFL path which includes LSC REFL PDs and ASC REFL WFS
    Starts on HAM2 and moves to HAM1
    Includes distances between PRMAR to IM2, plus all curved mirrors on REFL path
    all flat mirrors/beamsplitters set up as one lossy mirror right before RM1
    References: base alogs 63625 and 63510, DCC D1000313, T1000247, E1600302-v1, E1100494-v4
    T1300960-v2, T1200555
    Also adds in additional ASC dofs sensed at the REFL port (INP1, PRC)
    """
    model.parse(
        """
        # make a second IM2
        bs IM2_REFL R=1 L=0 Rc=12.8
        # set up mirrors on HAM1
        bs LossyMirror R=1-0.0125 T=0.0125
        bs RM1 R=1-800e-6 T=800e-6 Rc=1.7
        bs RM2 R=1-800e-6 T=800e-6 Rc=-0.6
        bs M5 R=1-800e-6 T=800e-6 Rc=1.7
        lens REFL_L101 f=333.6e-3
        lens REFL_L102 f=-166.8e-3
        bs WFS_REFL_BS R=0.5 T=0.5
        bs LSC_REFL_BS R=0.5 T=0.5

        # create placeholder for LSC RFPDs and ASC WFS
        nothing ASC_REFL_A
        nothing ASC_REFL_B
        nothing LSC_REFL_A
        nothing LSC_REFL_B

        # place LSC REFL RFPDs, only 9MHz
        readout_rf LSC_REFL_RFPD_A optical_node=LSC_REFL_A.p1.i f=f1
        readout_rf LSC_REFL_RFPD_B optical_node=LSC_REFL_B.p1.i f=f1

        # place ASC REFL WFS, 9 and 45 MHz
        readout_rf REFL_A_WFS9x optical_node=ASC_REFL_A.p1.i f=f1 pdtype=xsplit output_detectors=true
        readout_rf REFL_A_WFS9y optical_node=ASC_REFL_A.p1.i f=f1 pdtype=ysplit output_detectors=true
        readout_rf REFL_B_WFS9x optical_node=ASC_REFL_B.p1.i f=f1 pdtype=xsplit output_detectors=true
        readout_rf REFL_B_WFS9y optical_node=ASC_REFL_B.p1.i f=f1 pdtype=ysplit output_detectors=true
        readout_rf REFL_A_WFS45x optical_node=ASC_REFL_A.p1.i f=f2 pdtype=xsplit output_detectors=true
        readout_rf REFL_A_WFS45y optical_node=ASC_REFL_A.p1.i f=f2 pdtype=ysplit output_detectors=true
        readout_rf REFL_B_WFS45x optical_node=ASC_REFL_B.p1.i f=f2 pdtype=xsplit output_detectors=true
        readout_rf REFL_B_WFS45y optical_node=ASC_REFL_B.p1.i f=f2 pdtype=ysplit output_detectors=true

        # ASC dofs sensed at REFL
        dof INP1_P IM4.dofs.pitch +1
        dof INP1_Y IM4.dofs.yaw +1
        dof PRC2_P PR2.dofs.pitch +1
        dof PRC2_Y PR2.dofs.yaw +1
        """
    )
    # connect mirrors in HAM2
    # model.connect(model.PRMAR.p2, model.IM4.p1, L=413e-3)
    # model.connect(model.IM4.p3, model.IM3.p1, L=1175e-3)
    # model.connect(model.IM3.p3, model.IM2.p1, L=910e-3)

    # connect HAM2 to HAM1
    model.connect(model.IFI.p4, model.IM2_REFL.p1, L=260e-3)
    model.connect(model.IM2_REFL.p2, model.LossyMirror.p1, L=0)
    model.connect(model.LossyMirror.p3, model.RM1.p1, L=4159.5e-3)
    model.connect(model.RM1.p2, model.RM2.p1, L=838e-3)
    model.connect(model.RM2.p2, model.M5.p1, L=910e-3)
    model.connect(model.M5.p2, model.REFL_L101.p1, L=1220e-3)
    model.connect(model.REFL_L101.p2, model.REFL_L102.p1, L=203e-3)
    model.connect(model.REFL_L102.p2, model.WFS_REFL_BS.p1)

    # connect to LSC RFPDs
    model.connect(model.M5.p4, model.LSC_REFL_BS.p1)
    model.connect(model.LSC_REFL_BS.p3, model.LSC_REFL_A.p1)
    model.connect(model.LSC_REFL_BS.p2, model.LSC_REFL_B.p1)

    # connect to WFS
    model.connect(model.WFS_REFL_BS.p3, model.ASC_REFL_A.p1, L=836e-3)
    model.connect(model.WFS_REFL_BS.p2, model.ASC_REFL_B.p1, L=468e-3)

    # Add amplifiers for WFS
    kat_cmds = []
    for wfs in ["A", "B"]:
        for direction in ["x", "y"]:
            for freq in ["9", "45"]:
                kat_cmds.append(
                    f"amplifier REFL_{wfs}_WFS{freq}{direction}_G gain=0.25"
                )

    # Add summing amplifier
    kat_cmds.append("amplifier err_CHARD_P gain=1")
    kat_cmds.append("amplifier err_CHARD_Y gain=1")
    model.parse("\n".join(kat_cmds))

    # Connect readout -> amplifier -> summing amplifier
    for wfs in ["A", "B"]:
        for direction, dof in zip(["x", "y"], ["Y", "P"]):
            for freq in ["9", "45"]:
                _name = f"REFL_{wfs}_WFS{freq}{direction}"
                model.connect(
                    getattr(model, f"{_name}").I, getattr(model, f"{_name}_G").p1
                )
                model.connect(
                    getattr(model, f"{_name}_G").p2,
                    getattr(model, f"err_CHARD_{dof}").p1,
                )

    return model


def add_transmon_path(model, arm="x"):
    """Adds Transmon at the ETMx and ETMy.

    Following T1000247-v3; T0900385-v6
    """

    if arm == "x":
        arm_cap = "X"
    elif arm == "y":
        arm_cap = "Y"

    model.parse(
        f"""
        # Transmon at ETM{arm_cap}AR
        # Steering the beam (keeping only one TS{arm}_M1 at a distance of 2m instead of SM1 and SM2)
        s s_TMON{arm}_1 portA=ETM{arm_cap}AR.p2 portB=TS{arm}_M1.p1 L=1
        bs TS{arm}_M1 R=1 T=0 alpha=30 Rc=4
        s s_TMON{arm}_2 portA=TS{arm}_M1.p2 portB=TS{arm}_M2.p1 L=1.9026
        bs TS{arm}_M2 R=1 T=0 alpha=TS{arm}_M1.alpha Rc=-0.200

        # adding lenses
        s s_TMON{arm}_3 portA=TS{arm}_M2.p2 portB=IQPD{arm}_L1.p1 L=1.0974
        lens IQPD{arm}_L1 f=0.333
        s s_TMON{arm}_4 portA=IQPD{arm}_L1.p2 portB=IQPD{arm}_L2.p1 L=0.240
        lens IQPD{arm}_L2 f=-0.111

        # splitting the beam for two QPDs with a mirror
        s s_TMON{arm}_5 portA=IQPD{arm}_L2.p2 portB=TS{arm}_M3.p1 L=0.1
        bs TS{arm}_M3 R=0.5 T=0.5

        # QPDs placeholders
        s s_TMON{arm}_6 portA=TS{arm}_M3.p2 portB=IQPD{arm}_QPD1.p1 L=0.410-0.1
        nothing IQPD{arm}_QPD1
        s s_TMON{arm}_7 portA=TS{arm}_M3.p3 portB=IQPD{arm}_QPD2.p1 L=0.410+0.300-0.1
        nothing IQPD{arm}_QPD2

        # QPDs
        readout_dc QPD{arm}_1x optical_node=IQPD{arm}_QPD1.p1.i pdtype=xsplit output_detectors=true
        readout_dc QPD{arm}_1y optical_node=IQPD{arm}_QPD1.p1.i pdtype=ysplit output_detectors=true
        readout_dc QPD{arm}_2x optical_node=IQPD{arm}_QPD2.p2.i pdtype=xsplit output_detectors=true
        readout_dc QPD{arm}_2y optical_node=IQPD{arm}_QPD2.p2.i pdtype=ysplit output_detectors=true
        """
    )

    return model


def optimize_AS_WFS(model):
    model.modes(maxtem=1)
    AS_WFS = (
        "AS_A_WFS45y",
        "AS_A_WFS45x",
        "AS_B_WFS45y",
        "AS_B_WFS45x",
        "AS_A_WFS36y",
        "AS_A_WFS36x",
        "AS_A_WFS72y",
        "AS_A_WFS72x",
        "AS_B_WFS72y",
        "AS_B_WFS72x",
    )

    model.run(
        OptimiseRFReadoutPhaseDC(
            "DHARD_P",
            "AS_A_WFS45y",
            "DHARD_P",
            "AS_B_WFS45y",
            "DHARD_Y",
            "AS_A_WFS45x",
            "DHARD_Y",
            "AS_B_WFS45x",
            "SRC1_P",
            "AS_A_WFS72y",
            "SRC1_Y",
            "AS_A_WFS72x",
            "MICH_P",
            "AS_A_WFS36y",
            "MICH_Y",
            "AS_A_WFS36x",
        )
    )
    # change to be optimized for Q
    for sensor in AS_WFS:
        getattr(model, sensor).phase += 90

    return model


def __add2plot(_readout, _ax, __model):
    for direc, ls in zip(["x", "y"], ["-", "--"]):
        out = __model.run(
            Xaxis(
                getattr(__model, _readout + direc).phase,
                "lin",
                -100,
                100,
                20,
                relative=True,
            )
        )
        for param, col in zip(["_I", "_Q"], ("b", "y")):
            _name = _readout + direc + param
            _ax.plot(out.x0, out[_name], c=col, label=_name, ls=ls)

    _ax.legend()


def plot_AS_WFS_phases(model, dof, d_dof=1e-9, relative=True, npoints=200, srange=100):
    """For given dof offset, plot the WFS as a function of demod phase.

    For given degree of freedom offset, scan
    the demodulation phase of the WFS and plot it.
    By default this is relative, so
    0 refers to the set demodulation phase.

    The offset is set on a copy of the model

    Parameters
    ----------
    model: finesse.Model
        The model object
    dof : string
        The degree of freedom, e.g. DHARD_P
    d_dof : float, optional
        Offset on degree of freedom, defaults 1e-9
    npoints : int, optional
        Number of points to plot, defaults 200
    srange : float, optional
        Start and stop point. Plot starts at -srange
        and ends and +srange. Default 100 degrees.
    """
    from matplotlib import pyplot as plt

    try:
        getattr(model, "AS_A_WFS45y")
    except AttributeError:
        raise AttributeError(
            "model does not have attribute 'AS_A_WFS45y'. Did you call `base.add_AS_WFS()`"
        )

    _model = model.deepcopy()

    fig, ax = plt.subplots(ncols=2, sharex=True, figsize=(10, 5))

    # First we plot the Pitch offsets
    getattr(_model, dof).DC = d_dof

    fig.suptitle(dof + " = " + str(d_dof * 1e9) + " [nrad]")

    __add2plot("AS_A_WFS45", ax[0], _model)
    __add2plot("AS_B_WFS45", ax[1], _model)
    fig.tight_layout()

    return fig, ax


def plot_REFL_WFS_phases(
    model, dof, d_dof=1e-9, relative=True, npoints=200, srange=100
):
    """For given dof offset, plot the WFS as a function of demod phase.

    For given degree of freedom offset, scan
    the demodulation phase of the WFS and plot it.
    By default this is relative, so
    0 refers to the set demodulation phase.

    The offset is set on a copy of the model

    Parameters
    ----------
    model: finesse.Model
        The model object
    dof : string
        The degree of freedom, e.g. DHARD_P
    d_dof : float, optional
        Offset on degree of freedom, defaults 1e-9
    npoints : int, optional
        Number of points to plot, defaults 200
    srange : float, optional
        Start and stop point. Plot starts at -srange
        and ends and +srange. Default 100 degrees.
    """
    from matplotlib import pyplot as plt

    try:
        getattr(model, "REFL_A_WFS45y")
    except AttributeError:
        raise AttributeError(
            "model does not have attribute 'REFL_A_WFS45y'. Did you call `base.add_REFL_path()`"
        )

    _model = model.deepcopy()

    fig, ax = plt.subplots(ncols=2, nrows=2, sharex=True, figsize=(10, 5))

    # First we plot the Pitch offsets
    getattr(_model, dof).DC = d_dof

    fig.suptitle(dof + " = " + str(d_dof * 1e9) + " [nrad]")

    __add2plot("REFL_A_WFS45", ax[0][0], _model)
    __add2plot("REFL_B_WFS45", ax[1][0], _model)
    __add2plot("REFL_A_WFS9", ax[0][1], _model)
    __add2plot("REFL_B_WFS9", ax[1][1], _model)
    fig.tight_layout()

    return fig, ax


def optimize_REFL_WFS(model):
    model.modes(maxtem=1)

    model.run(
        OptimiseRFReadoutPhaseDC(
            "CHARD_P",
            "REFL_A_WFS45y",
            "CHARD_P",
            "REFL_B_WFS45y",
            "CHARD_Y",
            "REFL_A_WFS45x",
            "CHARD_Y",
            "REFL_B_WFS45x",
            "CHARD_P",
            "REFL_A_WFS9y",
            "CHARD_P",
            "REFL_B_WFS9y",
            "CHARD_Y",
            "REFL_A_WFS9x",
            "CHARD_Y",
            "REFL_B_WFS9x",
        )
    )
    return model


def plot_phases(
    model, dof, readout, d_dof=1e-9, relative=True, npoints=200, srange=100
):
    """Plot the phase of a single DOF.

    Plot the phases. This is relative, so
    0 refers to the set demodulation phase.

    The offset is set on a copy of the model

    Parameters
    ----------
    model: finesse.Model
        The model object
    dof : string
        The degree of freedom, e.g. DHARD_P
    readout : string
        The readout, e.g. AS_A_WFS45y
    d_dof : float, optional
        Offset on degree of freedom, defaults 1e-9
    npoints : int, optional
        Number of points to plot, defaults 200
    srange : float, optional
        Start and stop point. Plot starts at -srange
        and ends and +srange. Default 100 degrees.
    """
    try:
        getattr(model, readout)
    except AttributeError:
        raise AttributeError(
            f"model has no attribute {readout}. Did you call `base.add_REFL_path()`"
        )

    _model = model.deepcopy()

    getattr(_model, dof).DC = d_dof
    out = _model.run(
        Xaxis(
            getattr(_model, readout).phase,
            "lin",
            -srange,
            srange,
            npoints,
            relative=relative,
        )
    )
    out.plot(readout + "_I", readout + "_Q")
