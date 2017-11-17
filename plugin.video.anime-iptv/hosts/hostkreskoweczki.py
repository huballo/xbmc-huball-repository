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

from common import (_addon, addpr, nURL, eod, set_view, addst, addonPath, GetDataBeetwenMarkers, tfalse,ParseDescription)
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
mainSite = 'https://www.kreskoweczki.pl'
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
host = 'kreskoweczki'


def Pagekresk(url, page, metamethod=''):
    url = url.lower()
    html = nURL(url)
    Browse_ItemAol(html, url, metamethod)
    eod()


def Browse_ItemAol(html, url, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
    html = GetDataBeetwenMarkers(html, 'zaczynaj', '<header>Kresk', False)[1]
#    print html.encode('ascii','ignore')
    data = re.findall('href="/kreskowka/(.+?)"><div(.+?)<b class="larger white">(.+?)</b>', html)
    ItemCount = len(data)
    for item in data:
        strona = mainSite + '/kreskowka/' + item[0]
        name = item[2].encode("utf-8")
        name = ParseDescription(name)
### scraper
        if (tfalse(addst("kresk-thumbs")) == True):
            import scraper
            scrap = scraper.scraper_check(host, name)
            try:
                if (name not in scrap):
                    html = nURL(strona)
                    html = GetDataBeetwenMarkers(html, '>Serie</a>', '<div class="info-basic">', False)[1]
                    #print html.encode('ascii','ignore')
                    data = re.findall("/upload/cats/(.+?).jpg", html)
                    ItemCount = len(data)
                    if len(data) > 0:
                        for item in data:
                            img = mainSite + '/upload/cats/'+ item + '.jpg'
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
            plot =''
        fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        pars = {'mode': 'Episodeskresk', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'kreskoweczki':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))
    eod()


def Browse_Episodeskresk(mode, url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
    html = GetDataBeetwenMarkers(html, '<header>Spis odcin', '<header>Komentarze</header>', False)[1]
    data = re.findall('href="/kreskowka/(.+?)"><div(.+?)<b class="larger white">(.+?)</b>', html)
    ItemCount = len(data)
    for item in data:
        url2 = mainSite + '/kreskowka/' + item[0]
        name = item[2].encode("utf-8")
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
        pars = {'mode': 'PlayAnimekresk', 'site': site, 'section': section, 'title': name, 'url': url2, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    eod()


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Browse_PlayAnimekresk(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
#    print html.encode('ascii','ignore')
    html = GetDataBeetwenMarkers(html, '<header>Wybierz odtwarzacz:</header>', '<header>Recenzje', False)[1]
    data = re.findall('action="/fullscreen/(.+?)"', html)
    for item in data:
        strona = 'https://www.kreskoweczki.pl/fullscreen/' + item
    lista = re.compile('name="source_id" value="(.+?)"><div class="item disabled"><div class="item-name"><b class="white larger">(.+?)</b>').findall(html)
    lista = [tuple(reversed(t)) for t in lista]
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(lista))
    if item != -1:
        player = str(lista[item][1])
        data = {'source_id': player}
        import requests
        r = requests.post(strona, data=data)
        players = r.text
        #print players.encode('ascii','ignore')
        lista = re.compile('<a href="(.+?)" target="_blank" class="fake-player"></a>').findall(players)
        if len(lista) > 0:
            for item in lista:
                url = item

        else:
            lista = re.compile('src="//(.+?)" allowfullscreen').findall(players)
            for item in lista:
                url = 'https://' + item

        from common import PlayFromHost
        PlayFromHost(url)
    eod()











