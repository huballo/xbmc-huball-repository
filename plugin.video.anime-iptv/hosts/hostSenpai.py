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
import urllib2

from common import (_addon, addpr, nURL, eod, set_view, addst, addonPath, GetDataBeetwenMarkers, tfalse, ParseDescription)
from contextmenu import ( ContextMenu_Series, ContextMenu_Episodes)


__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'crypto'))

### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
mainSite = 'http://senpai.com.pl/anime/'
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
host = 'Senpai'


def PageSenpai(url, page, metamethod=''):
    html = nURL(url)
    Browse_ItemSenpai(html, page, metamethod)
    eod()


def Browse_ItemSenpai(html, page, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, '<h4>Lista anime</h4>', '<footer class="page-footer indigo">', False)[1]
    data = re.findall('href="\/anime\/' + page + '(.+?)">\n(\s+)<img src="/Resources/anime/covers/(.+?)"', html)
    ItemCount = len(data)
    for item in data:
        strona = mainSite + page + item[0]
        name = urllib2.unquote(page + item[0].encode("utf-8"))
        name = ParseDescription(name)
### scraper
        if (tfalse(addst("aodc-thumbs")) == True):
            import scraper
            scrap = scraper.scraper_check(host, name)
            try:
                if (name not in scrap):
                    img = 'http://senpai.com.pl/Resources/anime/covers/' + urllib2.quote(item[2])
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
        fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        pars = {'mode': 'EpisodesSenpai', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'senpai':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesSenpai(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = GetDataBeetwenMarkers(nURL(url), '<div class="collection row anime-col">', '<footer class="page-footer indigo">', False)[1]
    data = re.findall('href="/anime/(.+?)">', html)
    ItemCount = len(data)
    for item in data:
        url2 = mainSite + item
        name = urllib2.unquote(item).replace('/', ' - ')
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
        pars = {'mode': 'PlaySenpai', 'site': site, 'section': section, 'title': name, 'url': url2, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# next page
#    npage = url[:-1] + str(int(url[-1:]) + 1)
#    if -1 != html.find("do strony "):
#        _addon.add_directory({'mode': 'EpisodesAnime', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartAol, img=nexticon)
    eod()


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Browse_PlaySenpai(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    players = GetDataBeetwenMarkers(html, '<div class="container">', "<h5>Napisy do pobrania</h5>")[1]
    players = players.replace('IFRAME SRC', 'iframe src')
    players = players.replace('https', 'http')
    lista = re.compile('<iframe src="http://(.+?)/(.+?)"').findall(players)
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(lista))
    if item != -1:
        host = str(lista[item][0])
        player = str(lista[item][1])
        url2 = 'http://'+ host + '/' + player
        if 'openload' in url:
            url2 = url.replace('openload.co', 'oload.info')
            url2 = url.replace('http', 'https')
        from common import PlayFromHost
        PlayFromHost(url2, url)
    eod()