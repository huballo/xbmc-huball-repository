# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime4fun
###############################################################################
###############################################################################
### Imports ###
import re
import xbmcaddon
from common import (_addon, addpr, nURL, eod, set_view, addst, GetDataBeetwenMarkers, tfalse)
from contextmenu import (ContextMenu_Series, ContextMenu_Episodes)
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
fanart = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
fanartAol = addonPath + '/art/japan/fanart.jpg'
host = 'Wbijam'


def Pagewbijam(url, page):
    html = nURL(url)
    Browse_Itemscen(html, '')
    eod()


def Browse_Itemscen(html, name2, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    html = html.encode('utf-8', '')
    html = re.sub('>Gry MMO anime</div>', '>Gry MMO anime', html)
    html = re.sub('>Polecane gry online</div', '>Polecane gry online', html)
    html = GetDataBeetwenMarkers(html, 'Menu Główne</div>', '<script type=', False, False)[1]
    data = re.findall('">(.+?)</div>', html)
    ItemCount = len(data)
    if len(data) > 0:
        for item in data:
            strona = item
            name = strona
            img = ''
            plot = ''
            fanart = fanartAol
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
##
            pars = {'mode': 'Browse_Itemslist', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Series(contextLabs)
            labs['title'] = name
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    eod()


def Browse_Itemslist(url, page='', content='episodes', view='515'):
    data = 'http://www.inne.wbijam.pl/'
    html = nURL(data)
    html = html.encode('utf-8', '')
    if 'Polecane serie anime' in url:
        data1 = '>Polecane serie anime</div>'
        data2 = '//inne.wbijam.pl/">Pozostałe serie</a>'
        link = ''
        mode = 'Browse_Episodeswijam'
    elif 'Lżejsze klimaty' in url:
        data1 = '>Lżejsze klimaty</div>'
        data2 = '>Gry MMO anime'
        link = 'http://www.inne.wbijam.pl/'
        mode = 'Browse_Episodeswijaminne'
    elif 'Akcja' in url:
        data1 = '>Akcja</div>'
        data2 = '>Lżejsze klimaty</div>'
        link = 'http://www.inne.wbijam.pl/'
        mode = 'Browse_Episodeswijaminne'
    data = GetDataBeetwenMarkers(html, data1, data2, False)[1]
    data = re.findall('<a href="(.+?)">(.+?)</a></li>', data)
    data.sort()
    ItemCount = len(data)
    if len(data) > 0:
        for item in data:
            strona = link + item[0]
            name = item[1]
### scrper
            if (tfalse(addst("wbij-thumbs")) == True):
                import scraper
                scrap = scraper.scraper_check(host, name)
                try:
                    if (name not in scrap):
                        html = nURL(strona)
                        data = re.findall('<img src="grafika/(.+?)">', html)
                        ItemCount = len(data)
                        if len(data) > 0:
                            for item in data:
                                img = url + '/grafika/' + item
                        else:
                            img = ''
                        plot = ''
                        scraper.scraper_add(host, name, img, plot, '')
                        scrap = scraper.scraper_check(host, name)
                except:
                    scrap = ''
                try:
                    img = scrap[1]
                except:
                    img = ''
                try:
                    plot = scrap[2]
                except:
                    plot = ''
            else:
                img = ''
                plot = ''
            fanart = fanartAol
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
    ##
            pars = {'mode': mode, 'site': site, 'section': section, 'title': name, 'url': strona, 'page': url, 'img': img, 'fanart': fanart}
            contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Series(contextLabs)
            labs['title'] = name
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))
    eod()


def Browse_Episodeswijam(url, page, content='episodes', view='515'):
    if url == '':
        return
    if 'blackclover'in url:
        html = nURL(url)
        print 'aaaaaaaaa', url
    else:
        html = nURL(url)
        html = html.encode('utf-8', '')
    if ('kolejnosc_ogladania.html' in html):
        data = GetDataBeetwenMarkers(html, 'html">Kolejność oglądania</a></li>', '</ul>', False)[1]
        data = re.findall('<a href="(.+?)">(.+?)</a>', data)
        ItemCount = len(data)
        if len(data) > 0:
            for item in data:
                strona = url + item[0]
                name = item[1]
                img = ''
                plot = ''
                fanart = fanartAol
                labs = {}
                try:
                    labs['plot'] = plot
                except:
                    labs['plot'] = ''
                pars = {'mode': 'Browse_Episodeswijaminne2', 'site': site, 'section': section, 'title': name, 'url': strona, 'page': url, 'img': img, 'fanart': fanart}
                contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
                contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
                labs['title'] = name
                _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
            eod()
    else:
        html2 = GetDataBeetwenMarkers(html, '>Odcinki anime online</div>', '</ul>', False)[1]
        data = re.findall('<a href="(.+?)">(.+?)</a>', html2)
        ItemCount = len(data)
        if len(data) > 0:
            for item in data:
                strona = url + item[0]
                name = item[1]
                img = ''
                plot = ''
                fanart = fanartAol
                labs = {}
                try:
                    labs['plot'] = plot
                except:
                    labs['plot'] = ''
                pars = {'mode': 'Browse_Episodeswijaminne2', 'site': site, 'section': section, 'title': name, 'url': strona, 'page': url, 'img': img, 'fanart': fanart}
                contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
                contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
                labs['title'] = name
                _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
        eod()


def Browse_Episodeswijaminne(url, page, content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    html = GetDataBeetwenMarkers(html, '<table class="lista">', '<center>', False)[1]
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
    html = html.replace('  ', '')
    #print html.encode('ascii', 'ignore')
    data = re.findall('alt="">(.+?)</td>', html)
    ItemCount = len(data)
    for item in data:
        strona = ''
        name = item.encode('utf-8')
        name = name.replace('</a>','')
        plot = ''
        img = ''
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        contextLabs = {'title': name, 'year': '0000', 'url': strona, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
        contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
        pars = {'mode': 'Browse_PlayWbijam', 'site': site, 'section': section, 'title': name, 'url': url,'page': name, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    eod()


def Browse_Episodeswijaminne2(url, page, content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    html = GetDataBeetwenMarkers(html, '<table class="lista">', '</table>', False)[1]
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
    html = html.replace('  ', '')
    #print html.encode('ascii', 'ignore')
    data = re.findall('<a href="(.+?)"(.+?)alt="">(.+?)<\/a>', html)
    ItemCount = len(data)
    for item in data:
        strona = page + item[0]
        name = item[2].encode('utf-8')
        plot = ''
        img = ''
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        contextLabs = {'title': name, 'year': '0000', 'url': strona, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
        contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
        pars = {'mode': 'Browse_PlayWbijam', 'site': site, 'section': section, 'title': name, 'url': strona,'page': url, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    eod()


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Browse_PlayWbijam(url, page, content='episodes', view='515'):
    url = url.replace('/kolejnosc_ogladania.html', '')
    page = page.replace('/kolejnosc_ogladania.html', '')
    if url == '':
        return
    elif ('http://www.inne.wbijam.pl' in url):
        html = nURL(url).encode('utf-8')
        players = GetDataBeetwenMarkers(html, 'alt="">'+page+'</td>', '<td><img src=')[1]
        players = players.replace('\'', '')
        players = players.replace('\n', '')
        players = players.replace('\r', '')
        players = players.replace('\t', '')
        players = players.replace('  ', '')
        #print players.decode('ascii', 'ignore')
        hosts = re.findall('<span class="odtwarzacz_link" rel="(.+?)">(.+?)<', players)
        hosts = [tuple(reversed(t)) for t in hosts]
        import xbmcgui
        d = xbmcgui.Dialog()
        item = d.select("Wybór playera", getItemTitles(hosts))
        if item != -1:
            player = str(hosts[item][1])
            player = 'http://www.inne.wbijam.pl/odtwarzacz-' + player + ".html"
            player = nURL(player)
            players = re.findall('<iframe src="(.+?)"', player)
            for item in players:
                from common import PlayFromHost
                PlayFromHost(item)
        eod()
    else:
        players = GetDataBeetwenMarkers(nURL(url), '<table class="lista">', '</table>')[1]
        players = players.replace('\'', '')
        players = players.replace('\n', '')
        players = players.replace('\r', '')
        players = players.replace('\t', '')
        players = players.replace('  ', '')
        players = players.replace('</td><td class="center">', ' ')
        players = players.replace('</td> <td class="center">', ' ')
        #print players.encode('ascii', 'ignore')
        hosts = re.findall(' ONLINE (.+?) <span class="odtwarzacz_link" rel="(.+?)"', players)
        import xbmcgui
        d = xbmcgui.Dialog()
        item = d.select("Wybór playera", getItemTitles(hosts))
        if item != -1:
            player = str(hosts[item][1])
            #page = page.split(".pl/")
            player = 'http://www.accelworld.wbijam.pl/odtwarzacz-' + player + ".html"
            html = nURL(player)
            html = html.replace('swf', 'php')
            from common import PlayFromHost
            players = re.findall('<iframe src="(.+?)"', html)
            if len(players) > 0:
                for item in players:
                    if (tfalse(addst("download.opp")) == True):
                        ret = d.yesno('Download', 'Do you want to download?')
                        if ret == True:
                            PlayFromHost(url, 'download')
                        if ret == False:
                            PlayFromHost(url, 'play')
                    if (tfalse(addst("download.opp")) == False):
                        PlayFromHost(url, 'play')
            else:
                #print html.encode('ascii', 'ignore')
                if 'vk.com' in html:
                        players = re.findall('rel="(.+?)" id="(.+?)">', html)
                        for item in players:
                            players = 'https://vk.com/video' + item[0] + '_' + item[1]
                            if (tfalse(addst("download.opp")) == True):
                                ret = d.yesno('Download', 'Do you want to download?')
                                if ret == True:
                                    PlayFromHost(players, 'download')
                                if ret == False:
                                    PlayFromHost(players, 'play')
                            if (tfalse(addst("download.opp")) == False):
                                    PlayFromHost(players, 'play')
                else:
                    players = re.findall('src="https://video.sibnet.ru/(.+?)"', html)
                    for item in players:
                        item = 'https://video.sibnet.ru/' + item
                        if (tfalse(addst("download.opp")) == True):
                            ret = d.yesno('Download', 'Do you want to download?')
                            if ret == True:
                                PlayFromHost(item, 'download')
                            if ret == False:
                                PlayFromHost(item, 'play')
                        if (tfalse(addst("download.opp")) == False):
                            PlayFromHost(item, 'play')
        eod()