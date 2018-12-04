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
    data = {'login': logindb, 'password': passworddb, 'signin': 'OK'}
    headers = {
    'authority': 'strefadb.pl',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    }
    s = requests.Session()
    r = s.get('https://strefadb.pl/', headers=headers)
    r = s.post('https://strefadb.pl/', data=data)
    r = s.get('https://strefadb.pl/', headers=headers)
    r = requests.post(url, data=data)
    html = r.text
    html = GetDataBeetwenMarkers(html, '<tbody>', '</tbody>')[1]
    html = re.sub('<td><span style="color: red;">Brak</span></td>', '', html)
    html = re.sub('<td><span style="color: red;">Nie</span></td>', '', html)
    html = re.sub('<td>Tak</td>', '<td> Lektor</td>', html)
    html = re.sub('</a></b></td><td>', ' - ', html)
    html = re.sub('p</td>', 'p</td>#', html)
    html = re.sub('</td><td>', ' - ', html)
    #text = html.encode('ascii', 'ignore')
    lista = re.findall('<a href="(.+?)" target="_blank" style="color: white;">(.+?)</td>#', html)
    lista = [tuple(reversed(t)) for t in lista]
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór hostingu", getItemTitles(lista))
    if item != -1:
        parametry = str(lista[item][1])
        url2 = 'https://strefadb.pl' + parametry
        r = requests.get(url2, cookies=s.cookies, headers=headers)
        urldata = r.url
        from common import PlayFromHost
        PlayFromHost(urldata)
    eod()