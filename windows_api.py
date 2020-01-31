import os
import ctypes
from ctypes import wintypes


def set_wallpaper( fileName ):
    SPI_SETDESKWALLPAPER  = 0x0014
    SPIF_UPDATEINIFILE    = 0x0001
    SPIF_SENDWININICHANGE = 0x0002

    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint, \
                                    ctypes.c_void_p,ctypes.c_uint
    SystemParametersInfo.restype = wintypes.BOOL
    path = os.path.abspath(fileName)
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)