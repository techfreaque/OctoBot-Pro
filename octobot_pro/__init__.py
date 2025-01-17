PROJECT_NAME = "OctoBot-Pro"
AUTHOR = "Drakkar-Software"
VERSION = "0.0.1"  # major.minor.revision


def _use_module_local_tentacles():
    import sys
    import os
    import appdirs
    if os.getenv("USE_CUSTOM_TENTACLES", "").lower() == "true":
        # do not use octobot_pro/imports tentacles
        # WARNING: in this case, all the required tentacles imports still have to work
        # and therefore be bound to another tentacles folder
        return
    # import tentacles from user-appdirs/imports directory
    dirs = appdirs.AppDirs(PROJECT_NAME, AUTHOR, VERSION)
    internal_import_path = os.path.join(dirs.user_data_dir, "imports")
    sys.path.insert(0, internal_import_path)


# run this before any other code as only octobot_pro module-local tentacles should be used
_use_module_local_tentacles()

try:
    # import tentacles from octobot_pro/imports directory after "_use_local_tentacles()" call
    from tentacles.Meta.Keywords import *
    # populate tentacles config helpers
    import octobot_tentacles_manager.loaders as loaders
    import octobot_pro.internal.octobot_mocks as octobot_mocks
    loaders.reload_tentacle_by_tentacle_class(
        tentacles_path=octobot_mocks.get_imported_tentacles_path()
    )
    # do not expose those when importing this file
    loaders = octobot_mocks = None

except ImportError:
    # tentacles not available during first install
    pass

from octobot_pro.constants import *
from octobot_pro.api import *
from octobot_pro.model import *
