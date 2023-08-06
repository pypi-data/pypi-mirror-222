# %%
import finesse.ligo
import importlib
import numpy as np
from finesse.components.mechanical import Pendulum
from finesse.analysis.actions import FrequencyResponse
import cmath
from finesse.ligo.suspension import SimplifiedQUAD, QUADSuspension
from finesse.ligo.asc import add_arm_ASC_DOFs, arm_g_factors

finesse.init_plotting()
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
use_ss_sus = False
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
P_target = 380e3

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
pre = model.run()
model.L0.P = 60 * P_target / pre["Px"]

F_Hz = np.linspace(1, 4, 200)
# F_Hz = np.geomspace(0.1, 10, 1000)
sol = model.run(
    FrequencyResponse(
        F_Hz,
        [CHARD_P.AC.i, CSOFT_P.AC.i, DHARD_P.AC.i, DSOFT_P.AC.i],
        [CHARD_P.AC.o, CSOFT_P.AC.o, DHARD_P.AC.o, DSOFT_P.AC.o],
    )
)
out = model.run()
sol.f[np.argmax(sol.f * abs(sol["DHARD_P.AC.i", "DHARD_P.AC.o"]))], out["Px"]
# %%
axs = finesse.plotting.bode(sol.f, sol["CHARD_P.AC.i", "CHARD_P.AC.o"], label="CHARD")
axs = finesse.plotting.bode(
    sol.f, sol["DHARD_P.AC.i", "DHARD_P.AC.o"], label="DHARD", axs=axs, ls="--"
)
axs = finesse.plotting.bode(
    sol.f, sol["CSOFT_P.AC.i", "CSOFT_P.AC.o"], label="CSOFT", axs=axs
)
axs = finesse.plotting.bode(
    sol.f, sol["DSOFT_P.AC.i", "DSOFT_P.AC.o"], label="DSOFT", axs=axs, ls="--"
)
P = out["Px"]

if simple_pendulum:
    omega_0 = 2 * np.pi * ITMX_sus.fpitch
    I = ITMX_sus.I_pitch
    c = 299792458.0
    L = float(model.Larm.value)
    g_itmx, g_etmx, g_itmy, g_etmy = arm_g_factors(model)

    # Eq 2 from https://opg.optica.org/ao/fulltext.cfm?uri=ao-49-18-3474
    omega_plus = np.sqrt(
        omega_0**2
        + P
        * L
        / (I * c)
        * (-(g_itmx + g_etmx) + cmath.sqrt(4 + (g_itmx - g_etmx) ** 2))
        / (1 - g_itmx * g_etmx)
    )
    omega_minus = np.sqrt(
        omega_0**2
        + P
        * L
        / (I * c)
        * (-(g_itmx + g_etmx) - cmath.sqrt(4 + (g_itmx - g_etmx) ** 2))
        / (1 - g_itmx * g_etmx)
    )

    axs[0].vlines(
        omega_0 / 2 / np.pi,
        -70,
        60,
        ls=":",
        label=rf"$\omega_{{0}} = {omega_0.real/2/np.pi:0.2f}$Hz",
        color="k",
        zorder=-100,
    )
    axs[0].vlines(
        omega_plus.real / 2 / np.pi,
        -70,
        60,
        ls=":",
        label=rf"$\omega_{{+}} = {omega_plus.real/2/np.pi:0.2f}$Hz",
        zorder=-100,
    )
    axs[0].vlines(
        omega_minus.real / 2 / np.pi,
        -70,
        60,
        color="red",
        ls=":",
        label=rf"$\omega_{{-}} = {omega_minus.real/2/np.pi:0.2f}$Hz",
        zorder=-100,
    )
    axs[0].margins(0)
    axs[0].set_title(
        f"E.Hirose, Appl. Opt. 49, 3474-3484 (2010)\nEq.2 vs FINESSE3, P={P/1e3:0.0f}kW"
    )
    axs[0].legend()
    axs[0].set_xlim(F_Hz.min(), F_Hz.max())
    axs[0].set_title(
        f"E.Hirose, Appl. Opt. 49, 3474-3484 (2010)\nEq.2 vs FINESSE3, P={P/1e3:0.0f}kW with simple pendulum"
    )
else:
    axs[0].set_title(f"FINESSE3, P={P/1e3:0.0f}kW with QUAD state space")
axs[0].set_xscale("linear")
# %%
