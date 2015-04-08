# -*- coding: utf-8 -*-
import urllib, xbmcplugin, xbmcgui, xbmcaddon, sys, os
mainSite = 'http://animejoy.tv/'
mainSite2 = 'http://www.anime4fun.com/'
my_addon = xbmcaddon.Addon('plugin.video.animejoy')
addonPath = my_addon.getAddonInfo('path')
icon = addonPath + '/icon.png'
icon2 = addonPath + '/icon2.png'
fanartlogo = addonPath + '/fanart.jpg'
MyAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sys.path.append(os.path.join(addonPath, 'hosts'))

def CATEGORIES():
        addDir('Animejoy', mainSite, 'Animejoy', icon, fanartlogo, '')
        addDir('Anime4fun', mainSite2, 'Anime4fun', icon2, fanartlogo, '')
##################################


def addDir(name, url, mode, iconimage, fanart, description):
        u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
        ok = True
        liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": "escription"})
        liz.setProperty("Fanart_Image", fanart)
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
        return ok


def get_params():
        param = []
        paramstring = sys.argv[2]
        if len(paramstring) >= 2:
                params = sys.argv[2]
                cleanedparams = params.replace('?', '')
                if (params[len(params) - 1] == '/'):
                        params = params[0:len(params) - 2]
                pairsofparams = cleanedparams.split('&')
                param = {}
                for i in range(len(pairsofparams)):
                        splitparams = {}
                        splitparams = pairsofparams[i].split('=')
                        if (len(splitparams)) == 2:
                                param[splitparams[0]] = splitparams[1]
        return param


params = get_params()
url = None
name = None
mode = None

try:
        url = urllib.unquote_plus(params["url"])
except:
        pass
try:
        name = urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode = urllib.unquote_plus(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode == None or url == None or len(url) < 1:
        print ""
        CATEGORIES()

elif mode == 'Animejoy':
        from hostanimejoy import Animejoy
        Animejoy()

elif mode == 'AZ':
    for az in MyAlphabet:
        from hostanimejoy import AZ
        AZ(url)

elif mode == 'Animelist':
        from hostanimejoy import Animelist
        Animelist(name, url)

elif mode == 'Episodes':
        from hostanimejoy import Episodes
        Episodes(url)

elif mode == 'Players':
        from hostanimejoy import Players
        Players(url)

elif mode == 'VIDEOLINKS':
        from hostanimejoy import VIDEOLINKS
        VIDEOLINKS(url, name)

elif mode == 'Anime4fun':
        from hostanime4fun import Anime4fun
        Anime4fun()

elif mode == 'AZ4fun':
    for az in MyAlphabet:
        from hostanime4fun import AZ4fun
        AZ4fun(url)

elif mode == 'Anime4funlist':
        from hostanime4fun import Anime4funlist
        Anime4funlist(name, url)

elif mode == 'Anime4funEpisodes':
        from hostanime4fun import Anime4funEpisodes
        Anime4funEpisodes(url)

elif mode == 'Anime4funPlayers':
        from hostanime4fun import Anime4funPlayers
        Anime4funPlayers(url)

elif mode == 'Anime4funVIDEOLINKS':
        from hostanime4fun import Anime4funVIDEOLINKS
        Anime4funVIDEOLINKS(url, name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
