# %%
import finesse.ligo.lho
from finesse.ligo.tools import set_lock_gains
from finesse.analysis.actions import (
    Maximize,
    Minimize,
    PseudoLockCavity,
    Series,
    Change,
    Noxaxis,
    OptimiseRFReadoutPhaseDC,
    SetLockGains,
)

# %%
lho = finesse.ligo.lho.make_O4_lho()
lho.modes("even", maxtem=4)

# %%
sol = lho.run(
    Series(
        Change(
            {
                "PRM.misaligned": True,
                "SRM.misaligned": True,
            }
        ),
        # Lock each arm cavity to the lowest loss mode
        PseudoLockCavity("cavXARM", mode=[0, 0], feedback="XARM.DC"),
        PseudoLockCavity("cavYARM", mode=[0, 0], feedback="YARM.DC"),
        # Put mich on dark fringe
        Minimize("Pas_carrier", "MICH2.DC"),
        # Realign the PRM
        Change({"PRM.misaligned": False}),
        # get the PRC in roughly the right place whilst keeping arms on resonance
        Maximize("PRG", "PRCL.DC"),
        # get the PRC in roughly the right place whilst keeping arms on resonance
        Maximize("cost_prcl", ["PRCL.DC", "CARM.DC"]),
        Noxaxis(name="after PRC"),
        # Realign SRM
        Change({"SRM.misaligned": False}),
        Minimize("Pprc_45", "SRCL.DC"),
        Noxaxis(name="after SRC"),
        OptimiseRFReadoutPhaseDC(
            "CARM",
            "REFL9",
            "PRCL",
            "POP9",
            "SRCL",
            "POP45",
            "DARM",
            "AS45",
            "MICH2",
            "REFL45",
        ),
        SetLockGains(d_dof_gain=1e-10, optimize_phase=False),
    )
)
# %%
set_lock_gains(lho)
# %%
print("PRG", sol["after SRC"]["PRG"])
print("PRG9", sol["after SRC"]["PRG9"])
print("PRG45", sol["after SRC"]["PRG45"])
print("9 PRC [W]", sol["after SRC"]["Pprc_9"])
print("45 PRC [W]", sol["after SRC"]["Pprc_45"])
lho.run("run_locks()")
assert sol["after SRC"]["PRG"] > 50
# %%
