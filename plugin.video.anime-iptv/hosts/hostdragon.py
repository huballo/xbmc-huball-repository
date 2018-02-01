# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# STREFADB.PL
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

from common import (_addon, addpr, nURL, eod, set_view, addst, addonPath, GetDataBeetwenMarkers, tfalse, ParseDescription)
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
mainSite = 'https://strefadb.pl/'
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
host = 'dragon'
logindb = addst('usernamedb', '')
passworddb = addst('passworddb', '')


def Pagedragon(url, page, metamethod=''):
    html = nURL(url)

    Browse_Itemdragon(html, page, metamethod)
    eod()


def Browse_Itemdragon(html, url, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, '<ul class="lista-odcinkow">', '<div class="kontener">')[1]
    data = re.findall('<li>(.+?)</li>\n<li><a href="(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    for item in data:
        strona = mainSite + item[1]
        name = item[0] + " - " + item[2]
        name = name.encode("utf-8")
        img = ''
        plot = ''
        fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        pars = {'mode': 'Playdragon', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'dragonball':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Browse_Playdragon(url, page='', content='episodes', view='515'):
    if url == '':
        return
    lista = [('Napisy', '?typ=napisy'), ('Lektor', '?typ=lektor')]
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(lista))
    if item != -1:
        link = str(lista[item][1])
        link = url + link
    data = {'login': logindb, 'password': passworddb, 'signin': 'OK'}
    r = requests.post(link, data=data)
    lista = re.compile('<iframe src="(.+?).mp4"').findall(r.text)
    for item in lista:
        url = item + '.mp4'
        from common import PlayFromHost
        PlayFromHost(url)
    eod()