# -*- coding: utf-8 -*-
import urllib, urllib2, re, xbmcplugin, xbmcgui, xbmcaddon, sys
mainSite = 'http://tvgry.pl/'
my_addon = xbmcaddon.Addon('plugin.video.tvgry')
addonPath = my_addon.getAddonInfo('path')
icon = addonPath + '/icon.png'
fanart = addonPath + '/fanart.jpg'


def CATEGORIES():
        addDir('Najnowsze', mainSite, 1, icon, fanart, '')
        addDir('Tematy', mainSite + 'tematy.asp', 2, icon, fanart, '')
        addDir('Gry z kosza', mainSite + 'temat.asp?ID=99', 3, icon, fanart, '')
        addDir('Wiedźmin', mainSite + 'temat.asp?ID=78', 3, icon, fanart, '')
        addDir('Samiec alfa', mainSite + 'temat.asp?ID=93', 3, icon, fanart, '')
        addDir('Trajlery', mainSite + 'trailery.asp', 4, icon, fanart, '')


def NAJNOWSZE(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div class="container h1-s1">')
        if idx == -1:
            return
        idx2 = html.find('</div><footer id="footer"></footer>', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        html = html.replace('\r\n', '')
        r = re.compile('itemprop="name"><a href="/?(.+?)">(.+?)/a>(.+?)itemprop="description">(.+?)</p>(.+?)<img src="(.+?).jpg').findall(html)
        for url, name, xx, plot, yy, img in r:
            url = 'http://tvgry.pl/player/playlist_union.asp' + url + '&QUALITY=2&SECTION=TV'
            name = name.decode('windows-1250').encode('utf-8')
            plot = plot.decode('windows-1250').encode('utf-8')
            img = img + ".jpg"
            fanart = img
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 5, img, fanart, plot)


def TEMATY(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div class="container h1-s1">')
        if idx == -1:
            return
        idx2 = html.find('<div class="pagination">', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        html = html.replace('\r\n', '')
        html = html.replace('</a><div class="desc-box"><h2 itemprop="name">', '')
        r = re.compile('<a href="(.+?)"(.+?)>(.+?)<(.+?)<img src="(.+?).jpg"').findall(html)
        for url, xx, title, yy, img in r:
            url = mainSite + url
            name = title.decode('windows-1250').encode('utf-8')
            name = name.replace('<p>', '')
            plot = ""
            img = img.replace('http://tvgry.pl', '')
            img = mainSite + img + '.jpg'
            fanart = img
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 3, img, fanart, plot)


def GRYZKOSZA(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div class="container h1-s1">')
        if idx == -1:
            return
        idx2 = html.find('<div class="pagination">', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        html = html.replace('\r\n', '')
        r = re.compile('<a href="/?(.+?)" class="hover-layer"></a><div class="desc-box"><h2 itemprop="name">(.+?)/h2><p itemprop="text" class="lead">(.+?)</p>	</div>			<img src="(.+?)" alt').findall(html)
        for url, title, plot, img in r:
            url = 'http://tvgry.pl/player/playlist_union.asp' + url + '&QUALITY=2&SECTION=TV'
            name = title.decode('windows-1250').encode('utf-8')
            plot = plot.decode('windows-1250').encode('utf-8')
            img = img
            fanart = img
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 5, img, fanart, plot)


def TRAJLERY(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html = response.read()
        response.close()
        idx = html.find('<div class="container h1-s1">')
        if idx == -1:
            return
        idx2 = html.find('<footer id="footer"></footer>', idx)
        if idx2 == -1:
            return
        html = html[idx:idx2]
        html = html.replace('\r\n', '')
        r = re.compile('<a href="/?(.+?)" class="hover-layer"></a><div class="desc-box"><h2 itemprop="name" style="margin-bottom:10px;">(.+?)</h2></div>			<img src="(.+?)" alt').findall(html)
        for url, title, img in r:
            url = url.replace('-', '')
            url = 'http://tvgry.pl/player/playlist_union.asp' + url + '&QUALITY=2&SECTION=GV'
            name = title.decode('windows-1250').encode('utf-8')
            plot = ''
            img = img
            fanart = img
            xbmcplugin.setContent(int(sys.argv[1]), 'movies')
            addDir(name, url, 5, img, fanart, plot)


def VIDEOLINKS(url, name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()
        match = re.compile(":file>(.+?)<").findall(link)
        addLink(name, match[0], '')


def addLink(name, url, iconimage):
        ok = True
        liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=icon)
        liz.setInfo(type="Video", infoLabels={"Title": name})
        liz.setProperty("Fanart_Image", fanart)
        ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=liz)
        return ok


def addDir(name, url, mode, iconimage, fanart, description):
        u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
        ok = True
        liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": description})
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
        NAJNOWSZE(url)

elif mode == 2:
        TEMATY(url)

elif mode == 3:
        GRYZKOSZA(url)
elif mode == 4:
        TRAJLERY(url)


elif mode == 5:
        VIDEOLINKS(url, name)


xbmcplugin.endOfDirectory(int(sys.argv[1]))
