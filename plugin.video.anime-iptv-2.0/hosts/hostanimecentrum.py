# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Centrum
# THANKS for support to samsamsam !!!!
# Some part of code comes from iptvplugin https://gitlab.com/iptvplayer-for-e2/iptvplayer-for-e2
###############################################################################
###############################################################################
### Imports ###
import re
import xbmcaddon
import os
import sys
import requests

from common import (_addon, addpr, nURL, eod, set_view, addst, addonPath, GetDataBeetwenMarkers, tfalse)
from contextmenu import ( ContextMenu_Series, ContextMenu_Episodes)
try:
    import json
except:
    import simplejson as json

__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv-2.0")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'crypto'))


### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
mainSite = 'http://anime-centrum.pl'
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
host = 'animecentrum'


def Pageanimecentrum(url, page, metamethod=''):
    headers = {
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
    }
    s = requests.Session()
    r = s.get('http://anime-centrum.pl/', headers=headers)
    lista = re.compile('<meta name="csrf-token" content="(.+?)">').findall(r.text)
    for item in lista:
        token = item
    headers = {
            'Pragma': 'no-cache',
            'Origin': 'http://anime-centrum.pl',
            'Accept-Encoding': 'gzip, deflate',
            'X-CSRF-TOKEN': token,
            'Accept-Language': 'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cache-Control': 'no-cache',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'http://anime-centrum.pl/',
    }
    data = [
          ('title', 'none'),
          ('letter', page),
          ('species', ''),
          ('type', 'none'),
          ('season', 'none'),
          ('year', 'none'),
        ]
    r = requests.post('https://anime-centrum.pl/anime/online/pl/list/search', headers=headers, cookies=s.cookies, data=data)
    r = r.text
    r = r.replace('\\n', '')
    r = r.replace('\\t', '')
    r = r.replace('\\', '')
    Browse_ItemAnimecentrum(r, url, metamethod)
    eod()


def Browse_ItemAnimecentrum(html, url, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    data = re.findall('tb-cell"><a href="(.+?)">(?:.+?)<img src="(.+?)" alt="(.+?)"', html)
    ItemCount = len(data)
    for item in data:
        strona = mainSite + item[0]
        strona = strona + '?page=1'
        name = item[2]
### scraper
        if (tfalse(addst("acentr-thumbs")) == True):
            import scraper
            scrap = scraper.scraper_check(host, name)
            if (name in scrap):
                try:
                    img = scrap[1]
                except:
                    img = ''
                try:
                    plot = scrap[2]
                except:
                    plot = ''
                try:
                    fanart = scrap[3]
                except:
                    fanart = fanartAol
            else:
                API_key = 'f090bb54758cabf231fb605d3e3e0468'
                query = 'https://api.themoviedb.org/3/search/tv?api_key=' + API_key + '&language=pl-PL&query=' + name + '&page=1'
                data = requests.get(query).json()
                total_results = data['total_results']
                if total_results > 0:
                    try:
                        for i in (requests.get(query).json()['results']):
                            genre = (i['genre_ids'])
                            if 16 in genre:
                                ID = (i['id'])
                                ID = ID[0]
                    except:
                        print ('')
                    try:
                        query = 'https://api.themoviedb.org/3/tv/' + str(ID) + '?api_key=' + API_key + '&language=pl-PL'
                        data = (requests.get(query).json())
                        plot = data['overview']
                        fanart = 'https://image.tmdb.org/t/p/original' + data['backdrop_path']
                        img = 'https://image.tmdb.org/t/p/original' + data['poster_path']
                    except:
                        plot = ''
                        img = ''
                        fanart = fanartAol
                    scraper.scraper_add(host, name, img, plot, fanart)
                    scrap = scraper.scraper_check(host, name)
                else:
                    plot = ''
                    img = ''
                    fanart = fanartAol
        else:
            img = ''
            plot = ''
            fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        pars = {'mode': 'EpisodesAnimecentrum', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'animecentrum':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesAnimecentrum(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    html = GetDataBeetwenMarkers(html, 'ul class="list-2">', '<ul class="pagination">', False)[1]
    data = re.findall('<a href="(.+?)" title="(.+?)">', html)
    ItemCount = len(data)
    for item in data:
        url2 = mainSite + item[0]
        name = item[1]
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
        pars = {'mode': 'PlayAnimecentrum', 'site': site, 'section': section, 'title': name, 'url': url2, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# next page
    npage = url[:-1] + str(int(url[-1:]) + 1)
    if -1 != html.find("pagination"):
        _addon.add_directory({'mode': 'EpisodesAnimecentrum', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartAol, img=nexticon)
    eod()


def Browse_PlayAnimecentrum(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    data = re.compile('<source src="(.+?)" type="video/mp4">').findall(html)
    for item in data:
        from common import PlayFromHost
        PlayFromHost(item, 'play')
    eod()
