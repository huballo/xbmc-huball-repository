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
    Browse_Itemscen(html, page)
    eod()


def Browse_Itemscen(html, name2, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    data = GetDataBeetwenMarkers(html, '<div id="tresc">', '.<br />', False)[1]
#    print data.encode('ascii', 'ignore')
    data = re.findall('<a href="(.+?)">(.+?)</a>', data)
    ItemCount = len(data)
    if len(data) > 0:
        for item in data:
            strona = item[0]
            name = item[1].encode('utf-8', '')
### scraper
            if (tfalse(addst("wbij-thumbs")) == True):
                import scraper
                scrap = scraper.scraper_check(host, name)
                try:
                    if (name not in scrap):
                        html = nURL(strona)
                        html = html.replace('\'', '')
                        html = html.replace('\n', '')
                        html = html.replace('\r', '')
                        html = html.replace('\t', '')
                        html = html.replace(' ', '')
                        data = re.findall('<br/><br/><center><imgsrc="(.+?)"', html)
                        ItemCount = len(data)
                        if len(data) > 0:
                            for item in data:
                                img = strona + '/' + item
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
            pars = {'mode': 'Browse_Itemslist', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Series(contextLabs)
            labs['title'] = name
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('links-view'))
    eod()


def Browse_Itemslist(url, page='', content='episodes', view='515'):
    if url == '':
        return
    elif url == 'http://www.inne.wbijam.pl':
        html = nURL(url)
        data = GetDataBeetwenMarkers(html, 'pmenu_naglowek_red', '</ul>', False)[1]
        data = re.findall('<a href="(.+?)">(.+?)</a></li>', data)
        ItemCount = len(data)
        if len(data) > 0:
            for item in data:
                strona = url + '/' + item[0]
                name = item[1].encode('utf-8', '')
### scraper
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
                                    print img
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
                pars = {'mode': 'Browse_Episodeswijaminne', 'site': site, 'section': section, 'title': name, 'url': strona, 'page': url, 'img': img, 'fanart': fanart}
                contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
                contextMenuItems = ContextMenu_Series(contextLabs)
                labs['title'] = name
                _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
        set_view(content, view_mode=addst('links-view'))
        eod()
    else:
        html = nURL(url)
        data = GetDataBeetwenMarkers(html, 'pmenu_naglowek_red', '</ul>', False)[1]
        data = re.findall('<a href="(.+?)">(.+?)</a>(|.+?)</li>', data)
        ItemCount = len(data)
        if len(data) > 0:
            for item in data:
                strona = url + '/' + item[0]
                name = item[1].encode('utf-8','')
                img = ''
                plot = ''
                fanart = fanartAol
                labs = {}
                try:
                    labs['plot'] = plot
                except:
                    labs['plot'] = ''
    ##
                pars = {'mode': 'Browse_Episodeswijam', 'site': site, 'section': section, 'title': name, 'url': strona, 'page': url, 'img': img, 'fanart': fanart}
                contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
                contextMenuItems = []
                labs['title'] = name
                _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
        set_view(content, view_mode=addst('links-view'))
        eod()


def Browse_Episodeswijam(url, page, content='episodes', view='515'):
    if url == '':
        return
    if ('kolejnosc_ogladania.html' in url):
        html = nURL(url)
        data = GetDataBeetwenMarkers(html, '<p class="pod_naglowek">', '<div id="stopka">', False)[1]
        data = re.findall('<a href="(.+?)">(.+?)</a>', data)
        ItemCount = len(data)
        if len(data) > 0:
            for item in data:
                strona = page + '/' + item[0]
                name = item[1].encode('utf-8', '')
                img = ''
                plot = ''
                fanart = fanartAol
                labs = {}
                try:
                    labs['plot'] = plot
                except:
                    labs['plot'] = ''
                pars = {'mode': 'Browse_Episodeswijam', 'site': site, 'section': section, 'title': name, 'url': strona, 'page': url, 'img': img, 'fanart': fanart}
                contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
                contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
                labs['title'] = name
                _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
        set_view(content, view_mode=addst('links-view'))
        eod()
    else:
        html = nURL(url)
        html = GetDataBeetwenMarkers(html, '<table class="lista">', '</table>', False)[1]
        data = re.findall('<td><a href="(.+?)"><img src="images/artykul_info.gif" alt="">(.+?)</a></td>', html)
        ItemCount = len(data)
        for item in data:
            strona = page + '/' + item[0]
            name = item[1].encode('utf-8')
            plot = ''
            img = ''
            fanart = ''
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
    ###
            contextLabs = {'title': name, 'year': '0000', 'url': strona, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'Browse_PlayWbijam', 'site': site, 'section': section, 'title': name, 'url': strona,'page': page, 'img': img, 'fanart': fanart}
            labs['title'] = name
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
        set_view(content, view_mode=addst('links-view'))
        eod()


def Browse_Episodeswijaminne(url, page, content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    html = GetDataBeetwenMarkers(html, '<table class="lista">', '</table>', False)[1]
    html = html.replace('\'', '')
    html = html.replace('\n', '')
    html = html.replace('\r', '')
    html = html.replace('\t', '')
    html = html.replace('  ', '')
    data = re.findall('alt="">(.+?)</td>', html)
    ItemCount = len(data)
    for item in data:
        strona = ''
        name = item.encode('utf-8')
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
    set_view(content, view_mode=addst('links-view'))
    eod()


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Browse_PlayWbijam(url, page, content='episodes', view='515'):
    url = url.replace('/kolejnosc_ogladania.html','')
    page = page.replace('/kolejnosc_ogladania.html','')
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
        hosts = re.findall('<a href="(.+?)">(.+?)</a>', players)
        hosts = [tuple(reversed(t)) for t in hosts]
        import xbmcgui
        d = xbmcgui.Dialog()
        item = d.select("Wybór playera", getItemTitles(hosts))
        if item != -1:
            player = str(hosts[item][1])
            player = 'http://www.inne.wbijam.pl/' + player
            player = GetDataBeetwenMarkers(nURL(player), '<p class="pod_naglowek">Ogl', '</center>')[1]
            players = re.findall('src="(.+?)"', player)
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
        hosts = re.findall(' ONLINE (.+?)<a href="(.+?)">', players)
        import xbmcgui
        d = xbmcgui.Dialog()
        item = d.select("Wybór playera", getItemTitles(hosts))
        if item != -1:
            player = str(hosts[item][1])
            player = page + '/' + player
            html = nURL(player)
            html= html.replace('swf', 'php')
#            print html.encode('ascii', 'ignore')
            player = GetDataBeetwenMarkers(html, '<a href="pomoc_techniczna.html" target=', '</center>')[1]
            players = re.findall('src="(.+?)"', player)

            for item in players:
                from common import PlayFromHost
                if 'sibnet.ru' in item:
                    item = 'http:' + item
                print 'sssssssssssssss', item
                PlayFromHost(item)
        eod()








