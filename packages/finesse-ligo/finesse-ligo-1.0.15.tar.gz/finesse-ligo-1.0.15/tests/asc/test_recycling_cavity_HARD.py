# %%
import finesse.ligo
import importlib
import numpy as np
from finesse.components.mechanical import Pendulum
from finesse.components import DegreeOfFreedom
from finesse.analysis.actions import FrequencyResponse
from finesse.ligo.suspension import SimplifiedQUAD, QUADSuspension

finesse.init_plotting(fmts=["png"], dpi=200)
# %%
katfile = importlib.resources.read_text(
    "finesse_ligo.katscript", "aligo_reversed_itm.kat"
)
base = finesse.ligo.make_aligo(katscript=katfile)
# %%
model = base.deepcopy()
model.modes(maxtem=1)
model.fsig.f = 1
simple_pendulum = False
use_ss_sus = True
drive_L2 = True

if simple_pendulum:
    ITMX_sus = model.add(
        Pendulum("ITMX_sus", model.ITMX.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000)
    )
    ETMX_sus = model.add(
        Pendulum("ETMX_sus", model.ETMX.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000)
    )
    ITMY_sus = model.add(
        Pendulum("ITMY_sus", model.ITMY.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000)
    )
    ETMY_sus = model.add(
        Pendulum("ETMY_sus", model.ETMY.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000)
    )
    ITMX, ETMX, ITMY, ETMY = (
        ITMX_sus.dofs.F_pitch,
        ETMX_sus.dofs.F_pitch,
        ITMY_sus.dofs.F_pitch,
        ETMY_sus.dofs.F_pitch,
    )
else:
    # Using test of the SS sus model currently
    if use_ss_sus:
        sus_component = QUADSuspension  # will get renamed from test eventually
    else:
        sus_component = SimplifiedQUAD

    ITMX_sus = model.add(sus_component("ITMX_sus", model.ITMX.mech))
    ETMX_sus = model.add(sus_component("ETMX_sus", model.ETMX.mech))
    ITMY_sus = model.add(sus_component("ITMY_sus", model.ITMY.mech))
    ETMY_sus = model.add(sus_component("ETMY_sus", model.ETMY.mech))
    if drive_L2:
        ITMX, ETMX, ITMY, ETMY = (
            ITMX_sus.dofs.L2_F_pitch,
            ETMX_sus.dofs.L2_F_pitch,
            ITMY_sus.dofs.L2_F_pitch,
            ETMY_sus.dofs.L2_F_pitch,
        )
    else:
        ITMX, ETMX, ITMY, ETMY = (
            ITMX_sus.dofs.L3_F_pitch,
            ETMX_sus.dofs.L3_F_pitch,
            ITMY_sus.dofs.L3_F_pitch,
            ETMY_sus.dofs.L3_F_pitch,
        )

g_itmx = 1 - float(model.LX.L.value / np.abs(model.ITMX.Rcx.value))
g_etmx = 1 - float(model.LX.L.value / np.abs(model.ETMX.Rcx.value))
g_itmy = 1 - float(model.LY.L.value / np.abs(model.ITMY.Rcy.value))
g_etmy = 1 - float(model.LY.L.value / np.abs(model.ETMY.Rcy.value))

rx = 2 / ((g_itmx - g_etmx) + np.sqrt((g_etmx - g_itmx) ** 2 + 4))
ry = 2 / ((g_itmy - g_etmy) + np.sqrt((g_etmy - g_itmy) ** 2 + 4))

# Drive pitch torque but readout pitch motion
CHARD_P = model.add(
    DegreeOfFreedom("CHARD_P", ITMX, -1, ETMX, +rx, ITMY, -1, ETMY, +ry)
)
CSOFT_P = model.add(
    DegreeOfFreedom("CSOFT_P", ITMX, +rx, ETMX, +1, ITMY, +ry, ETMY, +1)
)
DHARD_P = model.add(
    DegreeOfFreedom("DHARD_P", ITMX, -1, ETMX, +rx, ITMY, +1, ETMY, -ry)
)
DSOFT_P = model.add(
    DegreeOfFreedom("DSOFT_P", ITMX, +rx, ETMX, +1, ITMY, -ry, ETMY, -1)
)


# %%
def run(P_target, use_SRC, use_PRC):
    # input power fudge to get arm power correct
    model.L0.P = 60
    ITM_Rc_D_per_W = -46e-6
    ETM_Rc_D_per_W = -33.46e-6

    model.ITMXlens.f = base.ITMXlens.f
    model.ITMYlens.f = base.ITMYlens.f
    model.ITMX.Rc = 2 / (2 / base.ITMX.Rc + ITM_Rc_D_per_W * P_target * 0.5e-6)
    model.ITMY.Rc = 2 / (2 / base.ITMY.Rc + ITM_Rc_D_per_W * P_target * 0.5e-6)
    model.ETMX.Rc = 2 / (2 / base.ETMX.Rc + ETM_Rc_D_per_W * P_target * 0.5e-6 * 3 / 5)
    model.ETMY.Rc = 2 / (2 / base.ETMY.Rc + ETM_Rc_D_per_W * P_target * 0.5e-6 * 3 / 5)
    model.SRM.misaligned = False
    model.PRM.misaligned = False
    model.run("run_locks()")
    model.SRM.misaligned = not use_SRC
    model.PRM.misaligned = not use_PRC
    pre = model.run()
    print("rescaling intput power by", P_target / pre["Px"])
    model.L0.P = 60 * P_target / pre["Px"]

    F_Hz = np.linspace(2.5, 3, 200)
    # F_Hz = np.geomspace(0.1, 10, 1000)
    sol = model.run(
        FrequencyResponse(
            F_Hz,
            [
                CHARD_P.AC.i,
                DHARD_P.AC.i,
            ],
            [CHARD_P.AC.o, DHARD_P.AC.o],
        )
    )

    print(
        P_target, "", sol.f[np.argmax(sol.f * abs(sol["DHARD_P.AC.i", "DHARD_P.AC.o"]))]
    )
    return sol


# %%
P_target = 380e3
model.modes(maxtem=4)
sol_wPRC_wSRC = run(P_target, True, True)
sol_woPRC_woSRC = run(P_target, False, False)


# %%
def plot(sol, DOF, axs=None, label=""):
    axs = finesse.plotting.bode(
        sol.f, sol[f"{DOF}_P.AC.i", f"{DOF}_P.AC.o"], axs=axs, label=DOF + label
    )
    axs[0].set_title(
        f"FINESSE3 comparing recycling cavity effects on HARD mode\nP={P_target/1e3:0.0f}kW"
    )
    axs[0].set_xscale("linear")
    axs[0].set_ylim(-40, 10)
    return axs


# %%
axs = plot(sol_wPRC_wSRC, "CHARD", label=" With RC")
axs = plot(sol_woPRC_woSRC, "CHARD", axs=axs, label=" No RC")
# %%
axs = plot(sol_wPRC_wSRC, "DHARD", label=" With RC")
axs = plot(sol_woPRC_woSRC, "DHARD", axs=axs, label=" No RC")

# %%
