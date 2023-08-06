# %%
import finesse.ligo
import importlib
import numpy as np
from finesse.components.mechanical import Pendulum
from finesse.components import DegreeOfFreedom
from finesse.analysis.actions import FrequencyResponse
from finesse.ligo.suspension import SimplifiedQUAD, QUADSuspension
import matplotlib.pyplot as plt
import h5py
import scipy.signal as sig


finesse.init_plotting()
# %%
katfile = importlib.resources.read_text(
    "finesse_ligo.katscript", "aligo_reversed_itm.kat"
)
base = finesse.ligo.make_aligo(katscript=katfile)

model = base.deepcopy()
model.modes(maxtem=1)
model.fsig.f = 1
# %%


def compare_models(P, model_type):
    model = base.deepcopy()
    model.modes(maxtem=1)
    model.fsig.f = 1
    """P is target power in the arms model types are simple_pendulum, full_quad,
    double_pendulum (a reduced order model of the quad)"""
    if model_type == "simple_pendulum":
        ITMX_sus = model.add(
            Pendulum(
                "ITMX_sus", model.ITMX.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000
            )
        )
        ETMX_sus = model.add(
            Pendulum(
                "ETMX_sus", model.ETMX.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000
            )
        )
        ITMY_sus = model.add(
            Pendulum(
                "ITMY_sus", model.ITMY.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000
            )
        )
        ETMY_sus = model.add(
            Pendulum(
                "ETMY_sus", model.ETMY.mech, fpitch=1.48, I_pitch=0.757, Qpitch=1000
            )
        )
        ITMX, ETMX, ITMY, ETMY = (
            ITMX_sus.dofs.F_pitch,
            ETMX_sus.dofs.F_pitch,
            ITMY_sus.dofs.F_pitch,
            ETMY_sus.dofs.F_pitch,
        )
    elif model_type == "full_quad":
        sus_component = QUADSuspension
        ITMX_sus = model.add(sus_component("ITMX_sus", model.ITMX.mech))
        ETMX_sus = model.add(sus_component("ETMX_sus", model.ETMX.mech))
        ITMY_sus = model.add(sus_component("ITMY_sus", model.ITMY.mech))
        ETMY_sus = model.add(sus_component("ETMY_sus", model.ETMY.mech))

    elif model_type == "double_pendulum":
        sus_component = SimplifiedQUAD
        ITMX_sus = model.add(sus_component("ITMX_sus", model.ITMX.mech))
        ETMX_sus = model.add(sus_component("ETMX_sus", model.ETMX.mech))
        ITMY_sus = model.add(sus_component("ITMY_sus", model.ITMY.mech))
        ETMY_sus = model.add(sus_component("ETMY_sus", model.ETMY.mech))
    else:
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

    P_target = P
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

    F_Hz = np.linspace(2.1, 3.4, 200)
    sol_hard = model.run(
        FrequencyResponse(
            F_Hz,
            [
                CHARD_P.AC.i,
                DHARD_P.AC.i,
            ],
            [CHARD_P.AC.o, DHARD_P.AC.o],
        )
    )

    F_Hz = np.linspace(0.1, 0.5, 200)
    sol_soft = model.run(
        FrequencyResponse(
            F_Hz,
            [
                CSOFT_P.AC.i,
                DSOFT_P.AC.i,
            ],
            [CSOFT_P.AC.o, DSOFT_P.AC.o],
        )
    )

    out = model.run()

    peak_freq_dh = sol_hard.f[
        np.argmax(sol_hard.f * abs(sol_hard["DHARD_P.AC.i", "DHARD_P.AC.o"]))
    ]
    peak_freq_ch = sol_hard.f[
        np.argmax(sol_hard.f * abs(sol_hard["CHARD_P.AC.i", "CHARD_P.AC.o"]))
    ]
    peak_freq_ds = sol_soft.f[
        np.argmax(sol_soft.f * abs(sol_soft["DSOFT_P.AC.i", "DSOFT_P.AC.o"]))
    ]
    peak_freq_cs = sol_soft.f[
        np.argmax(sol_soft.f * abs(sol_soft["CSOFT_P.AC.i", "CSOFT_P.AC.o"]))
    ]
    power = out["Px"]

    return power, peak_freq_dh, peak_freq_ch, peak_freq_ds, peak_freq_cs


# %%
import sys

if "pytest" in sys.modules:
    # do reduced steps when this is being run by the pytest for the pipeliness
    N = 1
else:
    N = 20
# %%
Powers = 1e3 * np.linspace(200, 600, N)

power = []
peak_freq_dh = []
peak_freq_ds = []
peak_freq_ch = []
peak_freq_cs = []

for P in Powers:
    pp, pf_dh, pf_ch, pf_ds, pf_cs = compare_models(P, model_type="full_quad")
    power.append(pp)
    peak_freq_dh.append(pf_dh)
    peak_freq_ds.append(pf_ds)
    peak_freq_ch.append(pf_ch)
    peak_freq_cs.append(pf_cs)

# %%

Powers = 1e3 * np.linspace(200, 600, N)

power_double = []
peak_freq_double_dh = []
peak_freq_double_ds = []
peak_freq_double_ch = []
peak_freq_double_cs = []

for P in Powers:
    pp, pf_dh, pf_ch, pf_ds, pf_cs = compare_models(P, model_type="double_pendulum")
    power_double.append(pp)
    peak_freq_double_dh.append(pf_dh)
    peak_freq_double_ds.append(pf_ds)
    peak_freq_double_ch.append(pf_ch)
    peak_freq_double_cs.append(pf_cs)


# %%
fig, ax = plt.subplots()
ax.plot(power, peak_freq_dh, color="#0343df", label="DHARD, Full QUAD Model")
ax.plot(
    power_double,
    peak_freq_double_dh,
    "--",
    color="#0343df",
    label="DHARD, Double Pendulum Model",
)
ax.plot(power, peak_freq_ch, color="#ff000d", label="CHARD, Full QUAD Model")
ax.plot(
    power_double,
    peak_freq_double_ch,
    "--",
    color="#ff000d",
    label="CHARD, Double Pendulum Model",
)
ax.legend()
ax.set_title("HARD Pitch")
ax.set_xticks(1e3 * np.linspace(200, 600, 9))
ax.set_xticklabels(["200", "250", "300", "350", "400", "450", "500", "550", "600"])
ax.set_xlabel("Arm Power [kW]")
ax.set_ylabel("Highest Frequency Pole [Hz]")
ax.grid(True, which="both")


fig, ax = plt.subplots()
ax.plot(power, peak_freq_ds, color="#0343df", label="DSOFT Full QUAD Model")
ax.plot(
    power_double,
    peak_freq_double_ds,
    "--",
    color="#0343df",
    label="DSOFT Double Pendulum Model",
)
ax.plot(power, peak_freq_cs, color="#ff000d", label="CSOFT Full QUAD Model")
ax.plot(
    power_double,
    peak_freq_double_cs,
    "--",
    color="#ff000d",
    label="CSOFT Double Pendulum Model",
)
ax.legend()
ax.set_title("SOFT Pitch")
ax.set_xticks(1e3 * np.linspace(200, 600, 9))
ax.set_xticklabels(["200", "250", "300", "350", "400", "450", "500", "550", "600"])
ax.set_xlabel("Arm Power [kW]")
ax.set_ylabel("Highest Frequency Pole [Hz]")
ax.grid(True, which="both")

# %%
model = finesse.ligo.make_aligo(katscript=katfile)
# freq = np.geomspace(0.1, 10, 500)
freq = np.linspace(2.1, 3.4, 200)

# L2 torque in [Nm] to L3 angle [rad]
z_l2p_l3p = np.array([-1.795683e-01 + 2.878020e00j, -1.795683e-01 - 2.878020e00j])
p_l2p_l3p = np.array(
    [
        -1.380233e-01 + 2.687744e00j,
        -1.380233e-01 - 2.687744e00j,
        -9.424111e-02 + 3.546816e00j,
        -9.424111e-02 - 3.546816e00j,
        -2.672733e-01 + 9.355654e00j,
        -2.672733e-01 - 9.355654e00j,
    ]
)
k_l2p_l3p = 9.279149e01
__, l2p_l3p = sig.freqresp((z_l2p_l3p, p_l2p_l3p, k_l2p_l3p), 2.0 * np.pi * freq)

# L3 torque in [Nm] to L3 angle [rad]
z_l3p_l3p = np.array(
    [
        -1.679986e-01 + 2.806124e00j,
        -1.679986e-01 - 2.806124e00j,
        -2.576084e-01 + 6.978624e00j,
        -2.576084e-01 - 6.978624e00j,
    ]
)
p_l3p_l3p = np.array(
    [
        -1.223585e-01 + 2.670807e00j,
        -1.223585e-01 - 2.670807e00j,
        -9.436692e-02 + 3.554246e00j,
        -9.436692e-02 - 3.554246e00j,
        -2.840980e-01 + 9.335571e00j,
        -2.840980e-01 - 9.335571e00j,
    ]
)
k_l3p_l3p = 2.665177e00
__, l3p_l3p = sig.freqresp((z_l3p_l3p, p_l3p_l3p, k_l3p_l3p), 2.0 * np.pi * freq)

z_l2y_l3y = [-9.722684e-01 + 1.152619e01j, -9.722684e-01 - 1.152619e01j]
p_l2y_l3y = [
    -1.709761e-01 + 3.811943e00j,
    -1.709761e-01 - 3.811943e00j,
    -1.977740e-01 + 8.614734e00j,
    -1.977740e-01 - 8.614734e00j,
    -1.446690e00 + 1.702979e01j,
    -1.446690e00 - 1.702979e01j,
]
k_l2y_l3y = 1.281647e02
__, l2y_l3y = sig.freqresp((z_l2y_l3y, p_l2y_l3y, k_l2y_l3y), 2.0 * np.pi * freq)

z_l3y_l3y = [-2.162474e-01 + 6.886976e00j, -2.162474e-01 - 6.886976e00j]
p_l3y_l3y = [
    -1.776369e-01 + 3.815934e00j,
    -1.776369e-01 - 3.815934e00j,
    -2.184140e-01 + 8.600263e00j,
    -2.184140e-01 - 8.600263e00j,
]
k_l3y_l3y = 2.409108e00
__, l3y_l3y = sig.freqresp((z_l3y_l3y, p_l3y_l3y, k_l3y_l3y), 2.0 * np.pi * freq)

import importlib

data_path = importlib.resources.path(
    "finesse_ligo.data.suspensions",
    "quad_damped_zpk.h5",
)
zpk_plant = {}
with h5py.File(data_path, mode="r") as f:
    data = f["damped"]["zpk"]
    zpk_plant["L3_pitch", "L3_F_pitch"] = (
        data["L3.disp.P"]["L3.drive.P"]["z"][:],
        data["L3.disp.P"]["L3.drive.P"]["p"][:],
        data["L3.disp.P"]["L3.drive.P"]["k"][()],
    )
    zpk_plant["L3_yaw", "L3_F_yaw"] = (
        data["L3.disp.Y"]["L3.drive.Y"]["z"][:],
        data["L3.disp.Y"]["L3.drive.Y"]["p"][:],
        data["L3.disp.Y"]["L3.drive.Y"]["k"][()],
    )
    zpk_plant["L3_z", "L3_F_z"] = (
        data["L3.disp.L"]["L3.drive.L"]["z"][:],
        data["L3.disp.L"]["L3.drive.L"]["p"][:],
        data["L3.disp.L"]["L3.drive.L"]["k"][()],
    )

    zpk_plant["L3_pitch", "L2_F_pitch"] = (
        data["L3.disp.P"]["L2.drive.P"]["z"][:],
        data["L3.disp.P"]["L2.drive.P"]["p"][:],
        data["L3.disp.P"]["L2.drive.P"]["k"][()],
    )
    zpk_plant["L3_yaw", "L2_F_yaw"] = (
        data["L3.disp.Y"]["L2.drive.Y"]["z"][:],
        data["L3.disp.Y"]["L2.drive.Y"]["p"][:],
        data["L3.disp.Y"]["L2.drive.Y"]["k"][()],
    )
    zpk_plant["L3_z", "L2_F_z"] = (
        data["L3.disp.L"]["L2.drive.L"]["z"][:],
        data["L3.disp.L"]["L2.drive.L"]["p"][:],
        data["L3.disp.L"]["L2.drive.L"]["k"][()],
    )

__, L3p_L3p = sig.freqresp(zpk_plant["L3_pitch", "L3_F_pitch"], 2.0 * np.pi * freq)
__, L3y_L3y = sig.freqresp(zpk_plant["L3_yaw", "L3_F_yaw"], 2.0 * np.pi * freq)
__, L2p_L3p = sig.freqresp(zpk_plant["L3_pitch", "L2_F_pitch"], 2.0 * np.pi * freq)
__, L2y_L3y = sig.freqresp(zpk_plant["L3_yaw", "L2_F_yaw"], 2.0 * np.pi * freq)

c = 299792458  # speed of light in m/s
Power = 1e3 * np.linspace(200, 600, 20)
# Rh = 2*P/c * dydthH_

L = 3994.47  # m

ITM_Rc_D_per_W = -46e-6
ETM_Rc_D_per_W = -33.46e-6

poles_QUAD_p = []
poles_DOUB_p = []

for P in Power:
    Rc_itm = 2 / (2 / model.ITMX.Rc + ITM_Rc_D_per_W * P * 0.5e-6)
    Rc_etm = 2 / (2 / model.ETMY.Rc + ETM_Rc_D_per_W * P * 0.5e-6 * 3 / 5)

    g_i = 1 - (L / Rc_itm[0])
    g_e = 1 - (L / Rc_etm[0])

    dydthH_ = (L / 2) * ((g_e + g_i) - np.sqrt((g_e - g_i) ** 2 + 4)) / (g_e * g_i - 1)
    R = 2 * P / c * dydthH_
    sus_p_QUAD = L2p_L3p / (1 + R * L3p_L3p)
    poles_QUAD_p.append(freq[np.argmax(np.abs(sus_p_QUAD))])

    sus_p_DOUB = l2p_l3p / (1 + R * l3p_l3p)
    poles_DOUB_p.append(freq[np.argmax(np.abs(sus_p_DOUB))])


# %%
Power = 1e3 * np.linspace(200, 600, 20)
fig, ax = plt.subplots()
ax.plot(power, peak_freq_dh, color="#0343df", label="DHARD, Full QUAD Model")
ax.plot(
    power_double,
    peak_freq_double_dh,
    "--",
    color="#0343df",
    label="DHARD, Double Pendulum Model",
)
ax.plot(power, peak_freq_ch, color="#ff000d", label="CHARD, Full QUAD Model")
ax.plot(
    power_double,
    peak_freq_double_ch,
    "--",
    color="#ff000d",
    label="CHARD, Double Pendulum Model",
)
ax.plot(Power, poles_QUAD_p, color="#d2bd0a", label="No Recycling HARD QUAD Model")
ax.plot(
    Power,
    poles_DOUB_p,
    "--",
    color="#d2bd0a",
    label="No Recycling HARD Double Pendulum Model",
)
ax.legend()
ax.set_title("HARD Pitch")
ax.set_xticks(1e3 * np.linspace(200, 600, 9))
ax.set_xticklabels(["200", "250", "300", "350", "400", "450", "500", "550", "600"])
ax.set_xlabel("Arm Power [kW]")
ax.set_ylabel("Highest Frequency Pole [Hz]")
ax.grid(True, which="both")


# %%
