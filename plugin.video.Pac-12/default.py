# -*- coding: utf-8 -*-
import urllib
import urllib2
import xbmcplugin
import xbmcgui
import xbmcaddon
import sys
import xbmc
import re

my_addon = xbmcaddon.Addon('plugin.video.Pac-12')
addonPath = my_addon.getAddonInfo('path')
icon = addonPath + '/icon.png'
fanart = addonPath + '/fanart.jpg'
iconbtn = addonPath + '/iconbtn.png'
fanartbtn = addonPath + '/fanartbtn.jpg'
fanarttsn = addonPath + '/fanarttsn.jpg'
icontsn = addonPath + '/TSN_logo.png'


def CATEGORIES():
    addDir('Pac National', 'http://xrxs.net/video/live-p12netw-', 1, icon, fanart, 'http://sports.the-antinet.net/pac12/pac12zap-2xml.php')
    addDir('Arizona', 'http://xrxs.net/video/live-p12ariz-', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-arizona.jpg', fanart, 'http://sports.the-antinet.net/pac12/pac12azzap-2xml.php')
    addDir('Bay Area', 'http://xrxs.net/video/live-p12baya-', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-bayarea.jpg', fanart, 'http://sports.the-antinet.net/pac12/pac12bazap-2xml.php')
    addDir('Los Angeles', 'http://xrxs.net/video/live-p12losa-', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-losangeles.jpg', fanart, 'http://sports.the-antinet.net/pac12/pac12lazap-2xml.php')
    addDir('Mountain', 'http://xrxs.net/video/live-p12moun-', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-mountain.jpg', fanart, 'http://sports.the-antinet.net/pac12/pac12mtnzap-2xml.php')
    addDir('Oregon', 'http://xrxs.net/video/live-p12oreg-', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-oregon.jpg', fanart, 'http://sports.the-antinet.net/pac12/pac12orzap-2xml.php')
    addDir('Washington', 'http://xrxs.net/video/live-p12wash-', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-washington.jpg', fanart, 'http://sports.the-antinet.net/pac12/pac12wazap-2xml.php')
    addDir('Big Ten Network', 'http://bigten247.cdnak.bigtenhd.neulion.com/nlds/btn2go/btnnetwork/as/live/btnnetwork_hd_3000.m3u8', 2, iconbtn, fanartbtn, '')
#    addDir('TSN1', 'http://ams-lp5.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/tsnOpen8.m3u8', 3, 'http://www.bellaliant.net/binaries/small/content/gallery/common_en/tv/channel-logos/tsn_1_aug2014.png', fanarttsn, '')
#    addDir('TSN2', 'http://ams-lp7.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN2Open8.m3u8', 3, 'http://www.bellaliant.net/binaries/small/content/gallery/common_en/tv/channel-logos/tsn_2_aug2014.png', fanarttsn, '')
#    addDir('TSN3', 'http://ams-lp1.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN3Open8.m3u8', 3, 'http://www.bellaliant.net/binaries/small/content/gallery/common_en/tv/channel-logos/tsn_3_aug2014.png', fanarttsn, '')
#    addDir('TSN4', 'http://ams-lp2.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN4Open8.m3u8', 3, 'http://www.bellaliant.net/binaries/small/content/gallery/common_en/tv/channel-logos/tsn_4_aug2014.png', fanarttsn, '')
#    addDir('TSN5', 'http://ams-lp3.9c9media.com/hls-live/livepkgr/_definst_/liveeventNoDRM/TSN5Open8.m3u8', 3, 'http://www.bellaliant.net/binaries/small/content/gallery/common_en/tv/channel-logos/tsn_5_aug2014.png', fanarttsn, '')

def addDir(name, url, mode, iconimage, fanart, description):
#        if (len(description) == 0):
#            title = ''
#        else:
#            req = urllib2.Request(description)
#            response = urllib2.urlopen(req)
#            html = response.read()
#            response.close()
#            title = re.compile("><title>(.+?)</title></").findall(html)
#            ItemCount = len(title)
#            for title in title:
#                title = ' - ' +title
        title = ''
        u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
        ok = True
        liz = xbmcgui.ListItem(name + title, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": ''})
        liz.setProperty("Fanart_Image", fanart)
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
        return ok


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Play(url, name, icon):
    lista = [['1080p', '4728.m3u8'], ['720p', '2328.m3u8']]
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(lista))
    if item != -1:
        url = url + str(lista[item][1])
        li = xbmcgui.ListItem(label=name, iconImage=icon, thumbnailImage=icon, path="")
        xbmc.Player().play(item=url, listitem=li)
    exit()


def Playbtn(url, name, icon):
    li = xbmcgui.ListItem(label=name, iconImage=iconbtn, thumbnailImage=iconbtn, path="")
    xbmc.Player().play(item=url, listitem=li)
    exit()


def PlayTSN(url, name, icon):
    li = xbmcgui.ListItem(label=name, iconImage=icontsn, thumbnailImage=icontsn, path="")
    xbmc.Player().play(item=url, listitem=li)
    exit()


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
        mode = int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode == None or url == None or len(url) < 1:
        print ""
        CATEGORIES()

elif mode == 1:
        Play(url, name, icon)

elif mode == 2:
        Playbtn(url, name, icon)

elif mode == 3:
        PlayTSN(url, name, icon)
xbmcplugin.endOfDirectory(int(sys.argv[1]))

