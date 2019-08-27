import xbmc
import xbmcgui
import xbmcaddon

__addon_id__= 'script.grab.fanart'
__Addon = xbmcaddon.Addon(__addon_id__)

def data_dir():
    return __Addon.getAddonInfo('profile')

def addon_dir():
    return __Addon.getAddonInfo('path')

def log(message,loglevel=xbmc.LOGDEBUG):
    xbmc.log(encode(__addon_id__ + ": " + message),level=loglevel)

def showNotification(message):
    xbmcgui.Dialog().notification(encode(getString(30010)),encode(message),time=4000,icon=xbmc.translatePath(__Addon.getAddonInfo('path') + "/resources/media/icon.png"))

def getSetting(name):
    return __Addon.getSetting(name)

def setSetting(name,value):
    __Addon.setSetting(name,value)
    
def getString(string_id):
    return __Addon.getLocalizedString(string_id)

def encode(string):
    return string.encode('UTF-8','replace')
