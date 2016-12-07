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
intro = addonPath + '/intro.mp4'
isplayed = xbmc.getInfoLabel("Window(Home).Property(intro.isplayed)").lower() == "true"
site = 'http://xrxs.net/process.php'


def CATEGORIES():
    if my_addon.getSetting("use_PAC-12_intro") == "true":
        if not isplayed:
            li = xbmcgui.ListItem(label='PAC-12', iconImage=icon, thumbnailImage=icon)
            xbmc.Player().play(intro, li)
            xbmcgui.Window(10000).setProperty("intro.isplayed", "true")
    addDir('Pac National', 'p12netw', 1, icon, fanart, 'Pac-12')
    addDir('Arizona', 'p12ariz', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-arizona.jpg', fanart, 'Pac-12 Arizona')
    addDir('Bay Area', 'p12baya', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-bayarea.jpg', fanart, 'Pac-12 Bay Area')
    addDir('Los Angeles', 'p12losa', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-losangeles.jpg', fanart, 'Pac-12 Los Angeles')
    addDir('Mountain', 'p12moun', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-mountain.jpg', fanart, 'Pac-12 Mountain')
    addDir('Oregon', 'p12oreg', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-oregon.jpg', fanart, 'Pac-12 Oregon')
    addDir('Washington', 'p12wash', 1, 'http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/network-washington.jpg', fanart, 'Pac-12 Washington')
    if '//' in my_addon.getSetting("BTN"):
        addDir('BTN', my_addon.getSetting("BTN"), 2, iconbtn, fanartbtn, 'Big Ten')


def addDir(name, url, mode, iconimage, fanart, description):
    #try:
        #if (len(description) == 0):
            #title = ''
        #else:
            #req = urllib2.Request('http://tvgo.xfinity.com/watch-live-tv')
            #response = urllib2.urlopen(req)
            #html = response.read()
            #response.close()
            #idx = html.find('<div id="sports" class="jump-anchor" >')
            #if idx == -1:
                #return
            #idx2 = html.find('<div id="family-kids" class="jump-anchor" >', idx)
            #if idx2 == -1:
                #return
            #html = html[idx:idx2]
            #html = html.replace('\n', '')
            #html = html.replace('  ', '')
            #try:
                #title = re.compile('alt="'+ description +'" class(.+?)<h2>(.+?)</h2>(.+?)"description">(.+?)</p>').findall(html)
                #if len(title) > 0:
                    #for xx, title, yy, title2 in title:
                        #title = ' - ' + title + ' - ' + title2
            #except:
                #print 'problemy'
    #except:
        #title = ''
        #print "problemy z opisem"
    title = ''
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
    ok = True
    liz = xbmcgui.ListItem(name + '[I]' + title + '[/I]', iconImage="DefaultFolder.png", thumbnailImage=iconimage)
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
    if my_addon.getSetting("use_custom_links") == "true":
        lista = [['1080p', '4728.m3u8'], ['720p', '2328.m3u8'], ['SD', '1164.m3u8']]
        lista2 = [['1080p', 'index_4728_av-p.m3u8'], ['720p', 'index_2328_av-b.m3u8'], ['SD', 'index_1164_av-b.m3u8']]
        d = xbmcgui.Dialog()
        item = d.select("Select Quality", getItemTitles(lista))
        if item != -1:
            if 'p12netw' in url:
                url = my_addon.getSetting("National")
            elif 'p12ariz' in url:
                url = my_addon.getSetting("Arizona")
            elif 'p12baya' in url:
                url = my_addon.getSetting("Bay")
            elif 'p12losa' in url:
                url = my_addon.getSetting("Angeles")
            elif 'p12moun' in url:
                url = my_addon.getSetting("Mountain")
            elif 'p12oreg' in url:
                url = my_addon.getSetting("Oregon")
            elif 'p12wash' in url:
                url = my_addon.getSetting("Washington")
            print url
            if 'xrxs' in url:
                url = url + str(lista[item][1])
            else:
                url = url + str(lista2[item][1])
            li = xbmcgui.ListItem(label=name, iconImage=icon, thumbnailImage=icon, path="")
            xbmc.Player().play(item=url, listitem=li)
        exit()
    else:
        lista = [['1080p', '4728.m3u8'], ['720p', '2328.m3u8'], ['SD', '1164.m3u8']]
        d = xbmcgui.Dialog()
        item = d.select("Select Quality", getItemTitles(lista))
        if item != -1:
            try:
                quality = str(lista[item][1])
                query_args = {'page': 'links', 'network': url, 'bitrate': quality}
                encoded_args = urllib.urlencode(query_args)
                request = urllib2.Request(site)
                request.add_header('User-agent', 'Mozilla/5.0')
                response = urllib2.urlopen(request, encoded_args)
                data = response.read()
                response.close()
                link = re.compile('<input value="(.+?)" class=').findall(data)
                if len(link) > 0:
                    for url in link:
                        url = url.replace('.m3u8.m3u8' , '.m3u8')
                        li = xbmcgui.ListItem(label=name, iconImage=icon, thumbnailImage=icon, path="")
                        xbmc.Player().play(item=url, listitem=li)
                        exit()
                else:
                    addonname = my_addon.getAddonInfo('name')
                    line1 = "Try custom links"
                    line2 = "Greetings, huball"
                    xbmcgui.Dialog().ok(addonname, line1, line2)
            except:
                    addonname = my_addon.getAddonInfo('name')
                    line1 = "http://xrxs.net/ probably is offline"
                    line2 = "Try custom links"
                    line3 = "Greetings, huball"
                    xbmcgui.Dialog().ok(addonname, line1, line2, line3)


def Playbtn(url, name, icon):
    li = xbmcgui.ListItem(label=name, iconImage=iconbtn, thumbnailImage=iconbtn, path="")
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

xbmcplugin.endOfDirectory(int(sys.argv[1]))
xbmcgui.Window(10000).setProperty("intro.isplayed", "false")

