# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Online
# THANKS for support to samsamsam !!!!
# Some part of code comes from iptvplugin https://gitlab.com/iptvplayer-for-e2/iptvplayer-for-e2
###############################################################################
###############################################################################
### Imports ###
import re
import xbmcaddon
import os
import sys

from common import (_addon, addpr, nURL, eod, addst, addonPath, GetDataBeetwenMarkers, tfalse,ParseDescription)
from contextmenu import ( ContextMenu_Series, ContextMenu_Episodes)
try:
    import json
except:
    import simplejson as json

__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'crypto'))



### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
mainSite7 = 'http://www.animezone.pl'
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
host = 'AnimeZone'


def Pagezone(url, page, metamethod=''):
    print 'zzzzzz',url
    html = nURL(url)
    Browse_ItemAol(html, url, metamethod)
    eod()


def Browse_ItemAol(html, url, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, 'Anime na liter', '<ul class="pagination">', False)[1]
    data = re.findall('<a href="(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    for item in data:
        strona =  mainSite7 + item[0]
        name = item[1].encode("utf-8")
        name = ParseDescription(name)
### scraper
        if (tfalse(addst("zone-thumbs")) == True):
            import scraper
            scrap = scraper.scraper_check(host, name)
            try:
                if (name not in scrap):
                    html = nURL(strona)
                    html = GetDataBeetwenMarkers(html, 'og:image', '<h5>Odcinki</h5>', False)[1]
                    html = html.replace('\'', '')
                    html = html.replace('\n', '')
                    html = html.replace('\r', '')
                    html = html.replace('\t', '')
                    print html.encode('ascii','ignore')
                    data = re.findall('content="(.+?)"></head>', html)
                    ItemCount = len(data)
                    if len(data) > 0:
                        for item in data:
                            img = item
                    else:
                        img = ''
                    data = re.findall('summary">(.+?)<div class', html)
                    ItemCount = len(data)
                    if len(data) > 0:
                        for item in data:
                            plot = ParseDescription(item)
                    else:
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
            plot =''
        fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        pars = {'mode': 'Episodeszone', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'animezone':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# next page
    npage = url[:-1] + str(int(url[-1:]) + 1)
#    if -1 != html.find("do strony "):
    _addon.add_directory({'mode': 'Pagezone', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartAol, img=nexticon)


def Browse_Episodeszone(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = GetDataBeetwenMarkers(nURL(url), '<h5>Odcinki</h5>', '</table>', False)[1]
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
    html = html.replace(' ', '')
    data = re.findall('<strong>(.+?)</strong></td><tdclass="episode-title">', html)
    ItemCount = len(data)
    for item in data:
        url2 = url + '/' + item
        name = 'Odcinek '+ item
        name = ParseDescription(name)
        img = ""
        fanart = fanartAol
        plot = ""
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        contextLabs = {'title': name, 'year': '0000', 'url': url2, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
        contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
        pars = {'mode': 'PlayAnimezone', 'site': site, 'section': section, 'title': name, 'url': url2, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    eod()


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        if 'Google' in value[0]:
            value = 'Google'
            out.append(value)
        else:
            out.append(value[0])
    return out


def Browse_PlayAnimezone(url, page='', content='episodes', view='515'):
    if url == '':
        return
    import requests
    headers = {
        'Pragma': 'no-cache',
        'Origin': 'http://www.animezone.pl',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': url,
    }
    s = requests.Session()
    s.get('http://www.animezone.pl/images/statistics.gif')
    players = s.get(url, headers=headers)
    players = players.text
    players = GetDataBeetwenMarkers(players, '<tbody>', "</table>")[1]
    players = players.replace('\'', '')
    players = players.replace('\n', '')
    players = players.replace('\r', '')
    players = players.replace('\t', '')
    players = players.replace(' ', '')
#    print players.encode('ascii','ignore')
    lista = re.compile('<td>(.+?)</td><tdclass(.+?)"data(.+?)="(.+?)"><iclass').findall(players)
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(lista))
    if item != -1:
        player = str(lista[item][3])
        data = {'data': player}
        r = s.post(url, headers=headers, data=data)
        players = r.text
        players = players.lower()
        print players.encode('ascii','ignore')
        lista = re.compile('<iframe src="(.+?)"').findall(players)
        for item in lista:
            url = item
            from common import PlayFromHost
            PlayFromHost(url)
    eod()











