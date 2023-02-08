# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Wbijam.pl
###############################################################################
###############################################################################
### Imports ###
import re
import xbmcaddon
from common import (_addon, addpr, nURL, eod, addst, GetDataBeetwenMarkers, tfalse)
from contextmenu import (ContextMenu_Series, ContextMenu_Episodes)
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv-2.0")
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
    html = GetDataBeetwenMarkers(html, 'dropbtn">Lista anime', '</div>', False, False)[1]
    data = re.findall('<a href="(.+?)" class="sub_link" rel="(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    if len(data) > 0:
        for item in data:
            strona = item[0]
            name = item[2]
            img = ''
            plot = ''
            fanart = fanartAol
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
##
            pars = {'mode': 'Browse_Episodeswijam', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Series(contextLabs)
            labs['title'] = name
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    eod()


def Browse_Episodeswijam(url, page, content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    if ('kolejnosc_ogladania.html' in html):
        data = GetDataBeetwenMarkers(html, 'Kolejność oglądania</a>', '</div>', False)[1]
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


def Browse_Episodeswijaminne2(url, page, content='episodes', view='515'):
    url = url.replace('\" class=\"sub_inner_link', '')
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
        html = nURL(url)
        players = GetDataBeetwenMarkers(html, 'alt="">' + page + '</td>', '<td><img src=')[1]
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
            from common import PlayFromHost
            for item in players:
                if len(players) > 0:
                    for item in players:
                        if (tfalse(addst("download.opp")) == True):
                            ret = d.yesno('Download', 'Do you want to download?')
                            if ret == True:
                                PlayFromHost(item, 'download')
                            if ret == False:
                                PlayFromHost(item, 'play')
                        if (tfalse(addst("download.opp")) == False):
                            PlayFromHost(item, 'play')
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
                            PlayFromHost(item, 'download')
                        if ret == False:
                            PlayFromHost(item, 'play')
                    if (tfalse(addst("download.opp")) == False):
                        PlayFromHost(item, 'play')
            else:
                #print html.encode('ascii', 'ignore')
                if 'vk.com' in html:
                        players = re.findall('rel="(.+?)" id="(.+?)">', html)
                        for item in players:
                            item = 'https://vk.com/video' + item[0] + '_' + item[1]
                            if (tfalse(addst("download.opp")) == True):
                                ret = d.yesno('Download', 'Do you want to download?')
                                if ret == True:
                                    PlayFromHost(item, 'download')
                                if ret == False:
                                    PlayFromHost(item, 'play')
                            if (tfalse(addst("download.opp")) == False):
                                    PlayFromHost(item, 'play')
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