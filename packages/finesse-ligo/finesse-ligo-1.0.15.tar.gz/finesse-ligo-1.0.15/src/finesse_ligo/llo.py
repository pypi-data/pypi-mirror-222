import finesse
import numpy as np
import importlib.resources

# from finesse.analysis.actions import OptimiseRFReadoutPhaseDC
# from .actions import DARM_RF_to_DC
# from .tools import set_lock_gains


def make_O4_llo(
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
    # CP-O6 + ITM-04 substrate lens
    base.ITMXlens.f = 1 / (1 / 137e6 - 1 / 310812)
    base.ITMX.Rc = 1937.9 if positive_ITM_Rc else -1937.9  # vendor measured 1938.61
    base.ITMX.T = 0.0148
    base.ITMX.R = 1 - base.ITMX.L.ref - base.ITMX.T.ref

    # CP-O3 + ITM-08 substrate lens
    base.ITMYlens.f = 1 / (1 / 64.860e3 - 1 / 92780)
    base.ITMY.Rc = 1940.7 if positive_ITM_Rc else -1940.7  # vendor measured 1938.44
    base.ITMY.T = 0.0148
    base.ITMY.R = 1 - base.ITMY.L.ref - base.ITMY.T.ref

    # ETM-08
    base.ETMX.Rc = 2240.0
    base.ETMX.T = 7.1e-6
    base.ETMX.R = 1 - base.ETMX.L.ref - base.ETMX.T.ref
    # ETM-07
    base.ETMY.Rc = 2236.3
    base.ETMY.T = 7.6e-6
    base.ETMY.R = 1 - base.ETMY.L.ref - base.ETMY.T.ref
    # PR3-03
    base.PR3.Rc = 36.021
    base.PR3.T = 5.3e-6
    base.PR3.R = 1 - base.PR3.L.ref - base.PR3.T.ref
    # PR2-02
    base.PR2.Rc = -4.543
    base.PR2.T = 243e-6  # vendor measured 223ppm
    # base.PR2.Loss = 0.6e-6 + 10e-6 # absorption + scatter loss
    base.PR2.R = 1 - base.PR2.L.ref - base.PR2.T.ref
    # PRM-02
    base.PRM.Rc = 11.009
    base.PRM.T = 0.031  # vendor measured 2.97%
    #    base.PRM.Loss = 0.5e-6 + 5.4e-6 # absorption + scatter loss
    base.PRM.R = 1 - base.PRM.L.ref - base.PRM.T.ref
    # SR3-01
    base.SR3.Rc = 35.97
    #    base.SR3.T = 5e-6
    # SR2-03 - not in galaxy, not in E1100927, asked garylinn, using LHO number
    base.SR2.Rc = -6.424
    # SRM-03
    base.SRM.Rc = -5.637
    base.SRM.T = 0.324
    #    base.SRM.Loss = 0.1e-6+7.3e-6 # absorption + scatter loss

    base.OM1.Rc = 4.6  # using old llo value, , NEW TSMAs mirror
    base.OM2.Rc = (
        1.7058  # Using old value, new mirror is also a TSAMs mirror so RoC can change
    )
    base.OM3.Rc = np.inf  # E1000457-v1
    base.OM3.set_RTL(R=0.99, T=0.01, L=0)

    # Design lengths for output path
    # Taken from https://dcc.ligo.org/DocDB/0095/T1200410/002/T1200410-v2.pdf
    # SRM to OM1 = 3.571m
    # OM1 to OM2 = 4.966 - 3.571 = 1.395m
    # OM2 to OM3 = 5.674 - 4.966 = 0.708m
    # OM3 to OMC waist = 5.936 - 5.674 = 0.262m
    # but we need OM3 to OMC input coupler. The OMC mode is 140mm past the OMC IC.
    # so the distance from OM3 to OMC IC should be 0.122m

    # Distances from Zemax mostly
    # plus some measurements from in chamber during O3+O4
    # base.sSRM_OFI.L = 0.9046
    # base.sOFI_OM1.L = 2.52 # from zemax 7 dec 2018 llo
    # base.sOM1_OM2.L = 1.395 # old value
    # base.sOM2_OM3.L = 0.64 # from zemax 7 dec 2018 llo
    # base.sOM3_OMC.L = 0.456 - 0.2815/2 # model fit during sqz mode matching - omc.ic to omc waist position
    # previously we used base values and fudged this number

    #
    #    base.sSRM_OFI.L = 0.9046
    #    base.sOFI_OM1.L = 3.440 - base.sSRM_OFI.L
    #    base.sOM1_OM2.L = 1.492
    #    base.sOM2_OM3.L = 0.654
    base.sOM3_OMC.L = 0.456 - 0.2815 / 2

    return base


def add_AS_WFS(model):
    """Adds in AS WFS path on transmission of OM3, 1 lens L101,
    1 beamsplitter M101 and AS A and B
    References: DCC D1000342 and T1000247
    """
    model.parse(
        """
        # lens in transmission of OM3
        lens AS_L101 f=334e-3

        # add in BS between AS A and AS B WFS
        bs AS_M101 R=0.5 T=0.5

        # set up nothing at AS A and B to put WFS
        nothing AS_A
        nothing AS_B

        # create WFS A and B at placeholder location
        # only includes 45 and 36  MHz WFS (used for DHARD and MICH ASC)
        # could be updated to include 72 MHz (118-45, requires addition of 13th order demod to model)
        readout_rf AS_A_WFS45x optical_node=AS_A.p1.i f=f2 pdtype=xsplit
        readout_rf AS_A_WFS45y optical_node=AS_A.p1.i f=f2 pdtype=ysplit
        readout_rf AS_B_WFS45x optical_node=AS_B.p1.i f=f2 pdtype=xsplit
        readout_rf AS_B_WFS45y optical_node=AS_B.p1.i f=f2 pdtype=ysplit
        readout_rf AS_A_WFS36x optical_node=AS_A.p1.i f=f2-f1 pdtype=xsplit
        readout_rf AS_A_WFS36y optical_node=AS_A.p1.i f=f2-f1 pdtype=ysplit
        readout_rf AS_B_WFS36x optical_node=AS_B.p1.i f=f2-f1 pdtype=xsplit
        readout_rf AS_B_WFS36y optical_node=AS_B.p1.i f=f2-f1 pdtype=ysplit
    """
    )
    model.connect(model.OM3.p3, model.AS_L101.p1, L=605e-3)
    model.connect(model.AS_L101.p2, model.AS_M101.p1)
    model.connect(model.AS_M101.p3, model.AS_A.p1, L=191e-3)
    model.connect(model.AS_M101.p4, model.AS_B.p1, L=475e-3)

    return model


def add_REFL_path(model):
    """Adds in REFL path which includes LSC REFL PDs and ASC REFL WFS
    Starts on HAM2 and moves to HAM1
    Includes distances between PRMAR to IM2, plus all curved mirrors on REFL path
    all flat mirrors/beamsplitters set up as one lossy mirror right before RM1
    References: LHO alogs 63625 and 63510, DCC D1000313, T1000247, E1600302-v1, E1100494-v4
    T1300960-v2, T1200555
    """
    model.parse(
        """
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
        readout_rf REFL_A_WFS9x optical_node=ASC_REFL_A.p1.i f=f1 pdtype=xsplit
        readout_rf REFL_A_WFS9y optical_node=ASC_REFL_A.p1.i f=f1 pdtype=ysplit
        readout_rf REFL_B_WFS9x optical_node=ASC_REFL_B.p1.i f=f1 pdtype=xsplit
        readout_rf REFL_B_WFS9y optical_node=ASC_REFL_B.p1.i f=f1 pdtype=ysplit
        readout_rf REFL_A_WFS45x optical_node=ASC_REFL_A.p1.i f=f2 pdtype=xsplit
        readout_rf REFL_A_WFS45y optical_node=ASC_REFL_A.p1.i f=f2 pdtype=ysplit
        readout_rf REFL_B_WFS45x optical_node=ASC_REFL_B.p1.i f=f2 pdtype=xsplit
        readout_rf REFL_B_WFS45y optical_node=ASC_REFL_B.p1.i f=f2 pdtype=ysplit
        """
    )
    # connect mirrors in HAM2
    # model.connect(model.PRMAR.p2, model.IM4.p1, L=413e-3)
    # model.connect(model.IM4.p3, model.IM3.p1, L=1175e-3)
    # model.connect(model.IM3.p3, model.IM2.p1, L=910e-3)

    # connect HAM2 to HAM1
    model.connect(model.IM2.p3, model.LossyMirror.p1, L=0)
    model.connect(model.LossyMirror.p3, model.RM1.p1, L=4159.5e-3)
    model.connect(model.RM1.p3, model.RM2.p1, L=838e-3)
    model.connect(model.RM2.p3, model.M5.p1, L=910e-3)
    model.connect(model.M5.p3, model.REFL_L101.p1, L=1220e-3)
    model.connect(model.REFL_L101.p2, model.REFL_L102.p1, L=203e-3)
    model.connect(model.REFL_L102.p2, model.WFS_REFL_BS.p1)

    # connect to LSC RFPDs
    model.connect(model.M5.p4, model.LSC_REFL_BS.p1)
    model.connect(model.LSC_REFL_BS.p3, model.LSC_REFL_A.p1)
    model.connect(model.LSC_REFL_BS.p4, model.LSC_REFL_B.p1)

    # connect to WFS
    model.connect(model.WFS_REFL_BS.p3, model.ASC_REFL_A.p1, L=836e-3)
    model.connect(model.WFS_REFL_BS.p4, model.ASC_REFL_B.p1, L=468e-3)

    return model
