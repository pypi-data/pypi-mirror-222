# %%
import finesse
import finesse.ligo
from finesse_ligo import lho
from finesse.analysis.actions.sensing import SensingMatrixDC
from finesse_ligo import suspension as sus
import numpy as np
from finesse.analysis.actions.lti import FrequencyResponse
import matplotlib.pyplot as plt

# from finesse.analysis.actions import Xaxis, OptimiseRFReadoutPhaseDC, Noxaxis
# from finesse.detectors import PowerDetector

# %%

finesse.init_plotting()

model = finesse.ligo.make_aligo()
model_lho = lho.make_O4_lho()

# model.ITMXlens.f = 26000
# model.ITMYlens.f = 26000

# add AS and REFL path
model = lho.add_AS_WFS(model)
model = lho.add_REFL_path(model)

# optimize the demod phase
model = lho.optimize_AS_WFS(model)
model = lho.optimize_REFL_WFS(model)

dofs_P = ("DHARD_P", "CHARD_P")
dofs_Y = ("DHARD_Y", "CHARD_Y")
refl_readouts_P = (
    "REFL_A_WFS9y",
    "REFL_A_WFS45y",
    "REFL_B_WFS9y",
    "REFL_B_WFS45y",
)
refl_readouts_Y = (
    "REFL_A_WFS9x",
    "REFL_A_WFS45x",
    "REFL_B_WFS9x",
    "REFL_B_WFS45x",
)

# set up intrix for HARD loops
model.parse(
    """
mathd IN_DHARD_P AS_A_WFS45y_Q
mathd IN_DHARD_Y AS_A_WFS45x_Q
mathd IN_CHARD_P REFL_B_WFS9y_I+REFL_B_WFS45y_I
mathd IN_CHARD_Y REFL_B_WFS9x_I+REFL_B_WFS45x_I
"""
)

# lock length loops
model.modes(maxtem=1)
sol = model.run("run_locks(exception_on_fail=False)")

# LHO O4 input power
model.L0.P = 60
out = model.run()
sol.plot_error_signals()
print("Power in: " + str(model.L0.P))
print("X arm power: " + str(round(out["Px"]) / 1e3) + " kW")
print("Y arm power: " + str(round(out["Py"]) / 1e3) + " kW")
print("PRG: " + str(round(out["PRG"], 1)))
# %%
# set up ASC locks
model.add(
    finesse.locks.Lock("DHARD_P_lock", model.IN_DHARD_P, model.DHARD_P.DC, 2e-6, 1e-6)
)
model.add(
    finesse.locks.Lock("DHARD_Y_lock", model.IN_DHARD_Y, model.DHARD_Y.DC, 2e-6, 1e-6)
)
model.add(
    finesse.locks.Lock("CHARD_P_lock", model.IN_CHARD_P, model.CHARD_P.DC, -6e-6, 1e-6)
)
model.add(
    finesse.locks.Lock("CHARD_Y_lock", model.IN_CHARD_Y, model.CHARD_Y.DC, -6e-6, 1e-6)
)

# %%
# misalign DHARD and lock
model.DHARD_P.DC = 5e-9
model.DHARD_Y.DC = 5e-9
model.CHARD_P.DC = 1e-9
model.CHARD_Y.DC = 1e-9

out0 = model.run(
    """
series(
    xaxis(DHARD_P.DC, lin, -10n, 10n, 100, relative=True, name='DHARD_P'),
    xaxis(DHARD_Y.DC, lin, -10n, 10n, 100, relative=True, name='DHARD_Y'),
    xaxis(CHARD_P.DC, lin, -10n, 10n, 100, relative=True, name='CHARD_P'),
    xaxis(CHARD_Y.DC, lin, -10n, 10n, 100, relative=True, name='CHARD_Y')
)
"""
)
sol2 = model.run(
    "run_locks(DHARD_P_lock, DHARD_Y_lock, CHARD_P_lock, CHARD_Y_lock, exception_on_fail=False)"
)
out = model.run(
    """
series(
    xaxis(DHARD_P.DC, lin, -10n, 10n, 100, relative=True, name='DHARD_P'),
    xaxis(DHARD_Y.DC, lin, -10n, 10n, 100, relative=True, name='DHARD_Y'),
    xaxis(CHARD_P.DC, lin, -10n, 10n, 100, relative=True, name='CHARD_P'),
    xaxis(CHARD_Y.DC, lin, -10n, 10n, 100, relative=True, name='CHARD_Y')
)
"""
)
sol2.plot_error_signals()

# %%
refl_readouts_Y_I = []
for name in refl_readouts_Y:
    refl_readouts_Y_I.append(name + "_I")
out = model.run("xaxis(CHARD_Y.DC, lin, -10n, 10n, 100)")
out.plot(refl_readouts_Y_I)

refl_readouts_P_I = []
for name in refl_readouts_P:
    refl_readouts_P_I.append(name + "_I")
out = model.run("xaxis(CHARD_P.DC, lin, -10n, 10n, 100)")
out.plot(refl_readouts_P_I)
# %%
refl_sensing_matrix_P = model.run(SensingMatrixDC(dofs_P, refl_readouts_P, d_dof=1e-10))
refl_sensing_matrix_P.plot(2, 2, figsize=(6, 6))
refl_sensing_matrix_Y = model.run(SensingMatrixDC(dofs_Y, refl_readouts_Y, d_dof=1e-10))
refl_sensing_matrix_Y.plot(2, 2, figsize=(6, 6))

# %%
refl_readouts_Y_I = []
for name in refl_readouts_Y:
    refl_readouts_Y_I.append(name + "_I")
out = model.run("xaxis(INP1_Y.DC, lin, -100n, 100n, 100)")
out.plot(refl_readouts_Y_I)

refl_readouts_P_I = []
for name in refl_readouts_P:
    refl_readouts_P_I.append(name + "_I")
out = model.run("xaxis(INP1_P.DC, lin, -100n, 100n, 100)")
out.plot(refl_readouts_P_I)

refl_readouts_Y_I = []
for name in refl_readouts_Y:
    refl_readouts_Y_I.append(name + "_I")
out = model.run("xaxis(PRC2_Y.DC, lin, -100n, 100n, 100)")
out.plot(refl_readouts_Y_I)

refl_readouts_P_I = []
for name in refl_readouts_P:
    refl_readouts_P_I.append(name + "_I")
out = model.run("xaxis(PRC2_P.DC, lin, -100n, 100n, 100)")
out.plot(refl_readouts_P_I)

# %%
refl_dofs_P = ("CHARD_P", "INP1_P", "PRC2_P")
refl_dofs_Y = ("CHARD_Y", "INP1_Y", "PRC2_Y")

refl_sensing_matrix_P = model.run(
    SensingMatrixDC(refl_dofs_P, refl_readouts_P, d_dof=1e-10)
)
refl_sensing_matrix_P.plot(2, 2, figsize=(6, 6))
refl_sensing_matrix_Y = model.run(
    SensingMatrixDC(refl_dofs_Y, refl_readouts_Y, d_dof=1e-10)
)
refl_sensing_matrix_Y.plot(2, 2, figsize=(6, 6))
# %%
# add double suspension to test masses

model.add(sus.SimplifiedQUAD("ITMX_sus", model.ITMX.mech))
model.add(sus.SimplifiedQUAD("ETMX_sus", model.ETMX.mech))
model.add(sus.SimplifiedQUAD("ITMY_sus", model.ITMY.mech))
model.add(sus.SimplifiedQUAD("ETMY_sus", model.ETMY.mech))

# %%

g_itmx = 1 - (3994.47 / np.abs(model.ITMX.Rc[0]))
g_etmx = 1 - (3994.47 / np.abs(model.ETMX.Rc[0]))
g_itmy = 1 - (3994.47 / np.abs(model.ITMY.Rc[0]))
g_etmy = 1 - (3994.47 / np.abs(model.ETMY.Rc[0]))

rx = 2 / ((g_itmx - g_etmx) + np.sqrt((g_etmx - g_itmx) ** 2 + 4))
ry = 2 / ((g_itmy - g_etmy) + np.sqrt((g_etmy - g_itmy) ** 2 + 4))

# converts from [CSOFT; CHARD; DSOFT; DHARD] to [IX; EX; IY; EY]
# but for pitch the signs need a minus sign for the ITMs as the positive coordinate
# system points towards the BS not into the cavity... the y vector flips from into
# to out of the the plane in the document
# ALL ITM SIGNS ARE FLIPPED RELATIVE TO THE LHO BASIS
cav_basis_P = np.array(
    [[-rx, 1, -rx, 1], [1, rx, 1, rx], [-ry, 1, ry, -1], [1, ry, -1, -ry]]
)

dof_to_arm_P = np.linalg.inv(cav_basis_P)
dof_to_arm_P = dof_to_arm_P / np.abs(dof_to_arm_P[0, 0])

cav_basis_Y = np.array(
    [[rx, 1, rx, 1], [-1, rx, -1, rx], [-ry, -1, ry, 1], [1, -ry, -1, ry]]
)

dof_to_arm_Y = np.linalg.inv(cav_basis_Y)
dof_to_arm_Y = dof_to_arm_Y / np.abs(dof_to_arm_Y[0, 0])

# %%
from types import SimpleNamespace
from finesse.components.general import LocalDegreeOfFreedom

dofs = SimpleNamespace()
dofs.ITMX = SimpleNamespace()
dofs.ETMX = SimpleNamespace()
dofs.ITMY = SimpleNamespace()
dofs.ETMY = SimpleNamespace()

dofs.ITMX.pitch = LocalDegreeOfFreedom(
    "dofs.ITMX.pitch", model.ITMX.ybeta, model.ITMX_sus.mech.L2_F_pitch, 1
)
dofs.ETMX.pitch = LocalDegreeOfFreedom(
    "dofs.ETMX.pitch", model.ETMX.ybeta, model.ETMX_sus.mech.L2_F_pitch, 1
)
dofs.ITMY.pitch = LocalDegreeOfFreedom(
    "dofs.ITMY.pitch", model.ITMY.ybeta, model.ITMY_sus.mech.L2_F_pitch, 1
)
dofs.ETMY.pitch = LocalDegreeOfFreedom(
    "dofs.ETMY.pitch", model.ETMY.ybeta, model.ETMY_sus.mech.L2_F_pitch, 1
)

dofs.ITMX.yaw = LocalDegreeOfFreedom(
    "dofs.ITMX.yaw", model.ITMX.xbeta, model.ITMX_sus.mech.L2_F_yaw, 1
)
dofs.ETMX.yaw = LocalDegreeOfFreedom(
    "dofs.ETMX.yaw", model.ETMX.xbeta, model.ETMX_sus.mech.L2_F_yaw, 1
)
dofs.ITMY.yaw = LocalDegreeOfFreedom(
    "dofs.ITMY.yaw", model.ITMY.xbeta, model.ITMY_sus.mech.L2_F_yaw, 1
)
dofs.ETMY.yaw = LocalDegreeOfFreedom(
    "dofs.ETMY.yaw", model.ETMY.xbeta, model.ETMY_sus.mech.L2_F_yaw, 1
)

model.CSOFT_P._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)
model.CHARD_P._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)
model.DSOFT_P._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)
model.DHARD_P._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)

model.CSOFT_Y._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)
model.CHARD_Y._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)
model.DSOFT_Y._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)
model.DHARD_Y._DegreeOfFreedom__drives = (
    dofs.ITMX.pitch,
    dofs.ETMX.pitch,
    dofs.ITMY.pitch,
    dofs.ETMY.pitch,
)

model.CSOFT_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[0])
model.CHARD_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[1])
model.DSOFT_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[2])
model.DHARD_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[3])

model.CSOFT_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[0])
model.CHARD_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[1])
model.DSOFT_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[2])
model.DHARD_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[3])

# %%
sol = model.run(
    FrequencyResponse(np.geomspace(0.1, 100000, 100), "DHARD_P", "AS_A_WFS45y.Q")
)

# %%
with model.temporary_parameters():
    model.L0.P = 100
    sol = model.run(
        FrequencyResponse(np.geomspace(0.1, 100, 300), "DHARD_P.AC", "AS_A_WFS45y.Q")
    )
plt.subplots(subplot_kw={"polar": False})
plt.loglog(sol.f, abs(sol["DHARD_P.AC", "AS_A_WFS45y.Q"]))
plt.xlabel("[Hz]")
# %%
with model.temporary_parameters():
    model.L0.P = 0
    sol = model.run(
        FrequencyResponse(
            np.geomspace(0.1, 10, 100),
            ["ETMX_sus.mech.L2_F_pitch", "ETMX_sus.mech.L3_F_pitch"],
            "ETMX_sus.mech.L3_pitch",
        )
    )
axs = finesse.plotting.bode(
    sol.f,
    sol["ETMX_sus.mech.L2_F_pitch", "ETMX_sus.mech.L3_pitch"],
    return_axes=True,
    label="L2->L3",
)
finesse.plotting.bode(
    sol.f,
    sol["ETMX_sus.mech.L3_F_pitch", "ETMX_sus.mech.L3_pitch"],
    axs=axs,
    label="L3->L3",
)
# %%
# %%
