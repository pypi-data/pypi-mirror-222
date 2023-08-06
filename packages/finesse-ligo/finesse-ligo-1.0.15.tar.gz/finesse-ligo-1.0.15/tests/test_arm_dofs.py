# %%
import finesse
import finesse.ligo
from finesse_ligo import lho
from finesse.analysis.actions.sensing import SensingMatrixDC

# from finesse_ligo import suspension as sus
import numpy as np

# from finesse.analysis.actions import Xaxis, OptimiseRFReadoutPhaseDC, Noxaxis
# from finesse.detectors import PowerDetector

finesse.init_plotting()
# %%
model = finesse.ligo.make_aligo()
# model_lho = lho.make_O4_lho()

# add AS and REFL path
model = lho.add_AS_WFS(model)
model = lho.add_REFL_path(model)

# optimize the demod phase
model = lho.optimize_AS_WFS(model)
model = lho.optimize_REFL_WFS(model)

dofs_P = ("DHARD_P", "CHARD_P", "CSOFT_P", "DSOFT_P")
dofs_Y = ("DHARD_Y", "CHARD_Y", "CSOFT_Y", "DSOFT_Y")
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

as_readouts_P = ("AS_A_WFS45y", "AS_B_WFS45y")
as_readouts_Y = ("AS_A_WFS45x", "AS_B_WFS45x")

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
# make separate model with different dof-to-mirror definitions for the arms

model_lho = model.deepcopy()

g_itmx = 1 - (3994.47 / np.abs(model_lho.ITMX.Rc[0]))
g_etmx = 1 - (3994.47 / np.abs(model_lho.ETMX.Rc[0]))
g_itmy = 1 - (3994.47 / np.abs(model_lho.ITMY.Rc[0]))
g_etmy = 1 - (3994.47 / np.abs(model_lho.ETMY.Rc[0]))

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
model_lho.CSOFT_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[0])
model_lho.CHARD_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[1])
model_lho.DSOFT_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[2])
model_lho.DHARD_P._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_P[3])

model_lho.CSOFT_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[0])
model_lho.CHARD_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[1])
model_lho.DSOFT_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[2])
model_lho.DHARD_Y._DegreeOfFreedom__amplitudes = tuple(dof_to_arm_Y[3])
# %%
# run sensing matrix for aligo drive dofs (0.73)
refl_sensing_matrix_P = model.run(SensingMatrixDC(dofs_P, refl_readouts_P, d_dof=1e-10))
refl_sensing_matrix_P.plot(2, 2, figsize=(6, 6))

refl_sensing_matrix_Y = model.run(SensingMatrixDC(dofs_Y, refl_readouts_Y, d_dof=1e-10))
refl_sensing_matrix_Y.plot(2, 2, figsize=(6, 6))

as_sensing_matrix_P = model.run(SensingMatrixDC(dofs_P, as_readouts_P, d_dof=1e-10))
as_sensing_matrix_P.plot(1, 2, figsize=(6, 6))

as_sensing_matrix_Y = model.run(SensingMatrixDC(dofs_Y, as_readouts_Y, d_dof=1e-10))
as_sensing_matrix_Y.plot(1, 2, figsize=(6, 6))
# %%
# run sensing matrix for lho ideal drive dofs (0.87)


refl_sensing_matrix_P = model_lho.run(
    SensingMatrixDC(dofs_P, refl_readouts_P, d_dof=1e-10)
)
refl_sensing_matrix_P.plot(2, 2, figsize=(6, 6))

refl_sensing_matrix_Y = model_lho.run(
    SensingMatrixDC(dofs_Y, refl_readouts_Y, d_dof=1e-10)
)
refl_sensing_matrix_Y.plot(2, 2, figsize=(6, 6))

as_sensing_matrix_P = model_lho.run(SensingMatrixDC(dofs_P, as_readouts_P, d_dof=1e-10))
as_sensing_matrix_P.plot(1, 2, figsize=(6, 6))

as_sensing_matrix_Y = model_lho.run(SensingMatrixDC(dofs_Y, as_readouts_Y, d_dof=1e-10))
as_sensing_matrix_Y.plot(1, 2, figsize=(6, 6))
# %%
