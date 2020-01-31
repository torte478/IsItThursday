import datetime;
import os
import ctypes
from ctypes import wintypes


def get_is_thursday_value():
    THURSDAY_INDEX = 3
    weekday = datetime.date.today().weekday();
    return weekday == THURSDAY_INDEX


def get_image_name( thursday ):
    return "thursday.jpg" if thursday else "other.jpg"


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


    

thursday = get_is_thursday_value()
image = get_image_name(thursday)
set_wallpaper(image)
