# %%
import finesse.ligo
import importlib
import numpy as np
from finesse.analysis.actions import FrequencyResponse
from finesse.ligo.suspension import QUADSuspension
from finesse.ligo.asc import add_arm_ASC_DOFs

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
sus_component = QUADSuspension

ITMX_sus = model.add(sus_component("ITMX_sus", model.ITMX.mech))
ETMX_sus = model.add(sus_component("ETMX_sus", model.ETMX.mech))
ITMY_sus = model.add(sus_component("ITMY_sus", model.ITMY.mech))
ETMY_sus = model.add(sus_component("ETMY_sus", model.ETMY.mech))

ITMX, ETMX, ITMY, ETMY = (
    ITMX_sus.dofs.L2_F_pitch,
    ETMX_sus.dofs.L2_F_pitch,
    ITMY_sus.dofs.L2_F_pitch,
    ETMY_sus.dofs.L2_F_pitch,
)

(
    CHARD_P,
    CSOFT_P,
    DHARD_P,
    DSOFT_P,
    CHARD_Y,
    CSOFT_Y,
    DHARD_Y,
    DSOFT_Y,
) = add_arm_ASC_DOFs(model, ITMX, ETMX, ITMY, ETMY)


# %%
def run(P_target, detune_SRCL):
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
    model.run("run_locks()")
    model.SRCL.DC += detune_SRCL
    pre = model.run()
    print("rescaling intput power by", P_target / pre["Px"])
    model.L0.P = 60 * P_target / pre["Px"]

    F_Hz = np.linspace(2.6, 2.8, 200)
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
model.modes(maxtem=1)
sol_m5 = run(P_target, -5)
sol_0 = run(P_target, 0)
sol_p5 = run(P_target, 5)


# %%
def plot(sol, DOF, axs=None, label=""):
    axs = finesse.plotting.bode(
        sol.f, sol[f"{DOF}_P.AC.i", f"{DOF}_P.AC.o"], axs=axs, label=DOF + label
    )
    axs[0].set_title(
        f"FINESSE3 comparing recycling cavity effects on HARD mode\nP={P_target/1e3:0.0f}kW"
    )
    axs[0].set_xscale("linear")
    return axs


# %%
axs = plot(sol_m5, "DHARD", label=" SRCL -5")
axs = plot(sol_0, "DHARD", label=" SRCL 0", axs=axs)
axs = plot(sol_p5, "DHARD", label=" SRCL +5", axs=axs)

# %%
