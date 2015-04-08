# -*- coding: utf-8 -*-
import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmcaddon, sys, xbmc
mainSite2 = 'http://www.anime4fun.com/'
my_addon = xbmcaddon.Addon('plugin.video.animejoy')
addonPath = my_addon.getAddonInfo('path')
icon2 = addonPath + '/icon2.png'
fanartlogo = addonPath + '/fanart.jpg'
MyAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
###############################################################################
# Anime4fun
###############################################################################


def Anime4fun():
        addDir('Anime list', mainSite2 + 'category/anime-list/', 'AZ4fun', icon2, fanartlogo, '')
#        addDir('Anime movies', mainSite2 + 'animemovies', 'Animelist', icon, fanartlogo, '')


def AZ4fun(url):
        addDir(az, url, 'Anime4funlist', icon2, fanartlogo, '')


def Anime4funlist(name, url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        r = re.compile('<a href="http://www.anime4fun.com/category/anime-list/(.+?)">'+ name + '(.+?)</a>').findall(html)
        for url, name2 in r:
            url = 'http://www.anime4fun.com/category/anime-list/' + url
            plot = ''
            img = icon2
            fanart = fanartlogo
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name + name2, url, 'Anime4funEpisodes', img, fanart, plot)


def Anime4funEpisodes(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<ul class="list-episode">')
        if idx == -1:
            return
        idx2 = html.find('</ul>', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        html = html.replace('\'', '')
        r = re.compile('<a href="(.+?)"><li class=(.+?)>(.+?)<span class=').findall(html)
        for url, xx, name in r:
            url = url
            name = name
            plot = ''
            img = icon2
            fanart = fanartlogo
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 'Anime4funPlayers', img, fanart, plot)


def Anime4funPlayers(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div id="video_inner">')
        if idx == -1:
            return
        idx2 = html.find('<div class="button_share">', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        r = re.compile('src="(.+?)" target=').findall(html)
        for url in r:
            url = url
            if ('mp4upload' in url):
                name = 'Mp4upload'
            else:
                name = 'Standard'
            plot = ''
            img = icon2
            fanart = fanartlogo
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 'Anime4funVIDEOLINKS', img, fanart, plot)


def  Anime4funVIDEOLINKS(url, name):
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
            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            html = response.read()
            response.close()
            HD = re.compile('<source src="(.+?)" type=').findall(html)[0]
            if HD == []:
                return
            url = HD
            name = "Player"
        li = xbmcgui.ListItem(label=name, iconImage=icon2, thumbnailImage=icon2, path="")
        xbmc.Player().play(item=url, listitem=li)
        exit()
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

if mode == 'Anime4fun':
        Anime4fun()

elif mode == 'AZ4fun':
    for az in MyAlphabet:
        AZ4fun(url)

elif mode == 'Anime4funlist':
        Anime4funlist(name, url)

elif mode == 'Anime4funEpisodes':
        Anime4funEpisodes(url)

elif mode == 'Anime4funPlayers':
        Anime4funPlayers(url)

elif mode == 'Anime4funVIDEOLINKS':
        Anime4funVIDEOLINKS(url, name)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
