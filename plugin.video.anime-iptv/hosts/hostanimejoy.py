# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime4fun
###############################################################################
###############################################################################
### Imports ###
import re
import xbmcaddon
from common import (_addon, addpr, nURL, eod, set_view, addst, GetDataBeetwenMarkers, clean_html)
from contextmenu import ( ContextMenu_Series, ContextMenu_Episodes)
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
fanart = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'

def Pagejoy(url, page, metamethod=''):
    html = nURL(url)
    Browse_Itemscen(html, page, metamethod)
    eod()


def Browse_Itemscen(html, name, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    data = re.compile('<div class="anim"><a href="(.+?)">  '+name+'(.+?)</a>').findall(html)
    ItemCount = len(data)
    for item in data:
        strona = 'http://anime-joy.tv/' + item[0]
        name2 = name + item[1]
        plot = ''
        img = ''
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
##
        pars = {'mode': 'Episodesjoy', 'site': site, 'section': section, 'title': name2, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name2, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'animejoy':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name2
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('links-view'))
    eod()

def Browse_Episodesjoy(url,page='',content='episodes',view='515'):
    if url == '':
        return
    html = nURL(url)
    html = GetDataBeetwenMarkers(html, '<div class="episodes">', '<div class="right">', False)[1]
    data = re.findall('<div class="ep"><a href="(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    for item in data:
        strona = item[0]
        name = item[1]
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
        pars = {'mode': 'PlayAnimejoy', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('links-view'))
    eod()


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Browse_PlayAnimejoy(url, page='', content='episodes', view='515'):
    if url == '':
        return
    players = GetDataBeetwenMarkers(nURL(url), '<div class="row">', '<div id="wrapped-content">')[1]
    hosts = re.findall('href="http:(.+?)">(.+?)</a>', players)
    hosts = [tuple(reversed(t)) for t in hosts]
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(hosts))
    if item != -1:
        player = str(hosts[item][1])
        player = 'http:' + player
        print player
        player = GetDataBeetwenMarkers(nURL(player), '<div id="video_container_div" style="display:none;">', '</div>')[1]
        print player
        players = re.findall('src="(.+?)"', player)
        for item in players:
            from common import PlayFromHost
            print item
            PlayFromHost(item)
    eod()








