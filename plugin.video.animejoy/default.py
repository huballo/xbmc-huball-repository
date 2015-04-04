# -*- coding: utf-8 -*-
import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmcaddon, sys, xbmc
mainSite = 'http://animejoy.tv/'
my_addon = xbmcaddon.Addon('plugin.video.animejoy')
addonPath = my_addon.getAddonInfo('path')
icon = addonPath + '/icon.png'
fanartlogo = addonPath + '/fanart.jpg'


def CATEGORIES():
        addDir('Anime list', mainSite + 'animelist', 1, icon, fanartlogo, '')
        addDir('Anime movies', mainSite + 'animemovies', 1, icon, fanartlogo, '')


def Animelist(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        r = re.compile('<div class="anim"><a href="(.+?)">(.+?)</a>').findall(html)
        for url, name in r:
            url = mainSite + url
            name = name
            plot = ''
            img = icon
            fanart = fanartlogo
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 5, img, fanart, plot)


def Episodes(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div class="episodes">')
        if idx == -1:
            return
        idx2 = html.find('<div class="right">', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        r = re.compile('<div class="ep"><a href="(.+?)">(.+?)</a>').findall(html)
        for url, name in r:
            url = url
            name = name
            plot = ''
            img = icon
            fanart = fanartlogo
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 6, img, fanart, plot)


def Players(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div class="row">')
        if idx == -1:
            return
        idx2 = html.find('<div id="wrapped-content">', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        r = re.compile('href="http://animejoy.tv/watch/(.+?)">(.+?)</a>').findall(html)
        for url, name in r:
            url = 'http://animejoy.tv/watch/' + url
            name = name
            plot = ''
            img = icon
            fanart = fanartlogo
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 7, img, fanart, plot)


def VIDEOLINKS(url, name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div id="video_container_div" style="display:none;">')
        if idx == -1:
            return
        idx2 = html.find('</div>', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        r = re.compile('src="(.+?)"').findall(html)
        for url in r:
            url =url
        if ('mp4upload' in url):
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            html = response.read()
            response.close()
            HD = re.compile("'file': '(.+?)'").findall(html)[0]
            if HD == []:
                return
            url = HD
            name = 'Mp4upload'
        else:
            name = "HD 1"
#        addLink(name, url, '')
        li = xbmcgui.ListItem(label=name, iconImage=icon, thumbnailImage=icon, path="")
        xbmc.Player().play(item=url, listitem=li)
        exit()



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
        Animelist(url)

elif mode == 5:
        Episodes(url)

elif mode == 6:
        Players(url)

elif mode == 7:
        VIDEOLINKS(url, name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
