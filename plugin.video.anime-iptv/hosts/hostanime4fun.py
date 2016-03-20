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

def Page4fun(url, page, metamethod=''):
    html = nURL(url)
    Browse_Itemscen(html, page, metamethod)
    eod()


def Browse_Itemscen(html, name, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, '">Result Anime Search', '<div class="pagination"><', False)[1]
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html.encode("utf-8")
    data = re.compile('src="(.+?)" width(.+?)title="(.+?)"(.+?)href="(.+?)"><h2>(.+?)text_intro">(.+?)</p>').findall(html)
    ItemCount = len(data)
    for item in data:
        img = item[0].replace(' ', '%20')
        strona = 'http://animeonline.co' + item[4]
        name2 = item[2]
        plot = clean_html(item[6])
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
##
        pars = {'mode': 'Episodes4fun', 'site': site, 'section': section, 'title': name2, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name2, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'anime4fun':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name2
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# next page
    npage = url[:-1] + str(int(url[-1:]) + 1)
#    if -1 != html.find("do strony "):
    _addon.add_directory({'mode': 'Page4fun', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanart, img=nexticon)
    set_view(content, view_mode=addst('links-view'))
    eod()

def Browse_Episodes4fun(url,page='',content='episodes',view='515'):
    if url == '':
        return
    html = nURL(url)
    html = GetDataBeetwenMarkers(html, '<ul class="list-episode">', '</ul>', False)[1]
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace(' ', '')
    data = re.findall('<ahref="(.+?)"><liclass=(.+?)>(.+?)<spanclass=', html)
    ItemCount = len(data)
    for item in data:
        strona = 'http://animeonline.co/' + item[0]
        name = item[2]
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
        pars = {'mode': 'PlayAnime4fun', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
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


def Browse_PlayAnime4fun(url, page='', content='episodes', view='515'):
    if url == '':
        return
    players = GetDataBeetwenMarkers(nURL(url), '<div class="overvideo" id="tabs" style="border: none; width: auto;">', '<div class="button_share">')[1]
    hosts = re.findall('<li><a href="#(.+?)" class="tabserver">(.+?)</a></li>', players)
    hosts = [tuple(reversed(t)) for t in hosts]
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(hosts))
    if item != -1:
        player = str(hosts[item][1])
        players = players.replace('\'', '')
        players = players.replace('\n', '')
        players = players.replace(' ', '')
        players = re.findall('<divid="'+player+'"class="servername">(.+?)src="(.+?)"target="_blank">', players)
        for item in players:
            from common import PlayFromHost
            PlayFromHost(item[1])
    eod()








