from .tools import make_aligo, make_arm, download
from . import thermal
from . import suspension
from . import actions
from . import maps
import importlib

# Set the Finesse.ligo version.
try:
    from ._version import version as __version__
except ImportError:
    raise Exception("Could not find version.py. Ensure you have run setup.")

aligo_katscript = importlib.resources.read_text("finesse_ligo.katscript", "aligo.kat")

try:
    # KATSPEC has been made a singleton in later versions
    from finesse.script.spec import KATSPEC as spec
except ImportError:
    from finesse.script.spec import KatSpec

    spec = KatSpec()  # grabs existing instance

from finesse.script.spec import make_element, make_analysis

spec.register_element(
    make_element(suspension.LIGOTripleSuspension, "ligo_triple"), overwrite=True
)
spec.register_element(
    make_element(suspension.LIGOQuadSuspension, "ligo_quad"), overwrite=True
)
spec.register_analysis(
    make_analysis(actions.DARM_RF_to_DC, "darm_rf_to_dc"), overwrite=True
)
spec.register_analysis(
    make_analysis(actions.DRFPMI_state, "drfpmi_state"), overwrite=True
)

__all__ = (
    "make_aligo",
    "make_arm",
    "download",
    "thermal",
    "suspension",
    "actions",
    "maps",
    "__version__",
)
