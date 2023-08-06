import os.path
from tempfile import TemporaryFile


class DirSetting:
    """Directory Settings

    User configuration settings.
    """

    tmpDirPath = os.path.dirname(TemporaryFile().name)
    defaultDirChmod = 0o700
