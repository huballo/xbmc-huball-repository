# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Shinden
###############################################################################
###############################################################################
### Imports ###
import re
import os
from common import (_addon, addpr, nURL, eod, ContextMenu_Movies, ContextMenu_Series, ContextMenu_Episodes, set_view, addst, addonPath, html_entity_decode, GetDataBeetwenMarkers)
from metahandler import metahandlers
import time
import xbmc
import xbmcaddon
#from metahandler import metacontainers
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
metaget = metahandlers.MetaData(preparezip=False)
fanartAol = addonPath + '/art/japan/fanart.jpg'
iconShniden = addonPath + '/art/japan/animeshniden.jpg'
mainSite5 = 'http://shinden.pl'
cookiepath = 'cookies.lwp'
__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('id')
dataroot = xbmc.translatePath('special://profile/addon_data/%s' % __addonname__).decode('utf-8')
cookie = (os.path.join(dataroot, cookiepath))
nexticon = addonPath + '/art/next.png'


def Pageshniden(url, page='', metamethod=''):
    html = nURL(url)
    Browse_ItemShniden(html, metamethod)
    eod()


def Browse_ItemShniden(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, 'data-view-table-cover', '<nav class="pagination">', False)[1]
    html = html.replace('\r\n', '')
    html = html.replace(' ', '')
    data = re.findall('src="(.+?)"/></td><tdclass="desc-col"><h3><ahref="(.+?)">(.+?)</a></h3>', html)
    ItemCount = len(data)
    for item in data:
        strona = mainSite5 + item[1]
        name = html_entity_decode(item[2])
        img = (mainSite5 + item[0]).replace('/resources/images/100x100/','/resources/images/genuine/')
        img = img.replace('100x100', '225x350')
        print img
        plot = ''
        fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        pars = {'mode': 'EpisodesShniden', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if   section == 'movie':
            contextMenuItems = ContextMenu_Movies(contextLabs)
        elif section == 'shnidenodc':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# next page
    npage = url[:-1] + str(int(url[-1:]) + 1)
#    if -1 != html.find("do strony "):
    _addon.add_directory({'mode': 'Pageshniden', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartAol, img=nexticon)
    set_view(content, view_mode=addst('links-view'))
    eod()


def Browse_GenreShniden(url, content='episodes'):
    if url == '':
        return
    html = nURL(url)
    r = re.compile('<input id=".+?"  type="checkbox" name="genre.." value="(.+?)">\n(.+?)</label').findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for title, xx in r:
            _url = mainSite5 + 'animelist/index.php?genre[]=' + title
            _name = title
            print _name
            _title = _name
            img = iconShniden
            labs = {}
            strona = _url
            contextLabs = {'title': _name, 'year': '0000', 'url': _url, 'img': img, 'fanart': fanartAol, 'DateAdded': ''}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'Pageshniden', 'site': site, 'section': section, 'title': _name, 'url': strona, 'fanart': fanartAol}
            labs['title'] = _title
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanartAol, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()


def Browse_EpisodesShniden(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url + '/episodes')
    html = GetDataBeetwenMarkers(html, 'list-episode-checkboxes', '</tbody>', False)[1]
    html = html.replace('\r\n', '')
    html = html.replace(' ', '')
    data = re.findall('<td>(.+?)</td>(.+?)<ahref="(.+?)"class="buttonactive">', html)
    ItemCount = len(data)
    for item in data:
        strona = mainSite5 + item[2]
        name = "Odcinek " + html_entity_decode(item[0])
        img = ''
        fanart = fanartAol
        plot = ""
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        contextLabs = {'title': name, 'year': '0000', 'url': strona, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
        contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
        pars = {'mode': 'PlayShniden', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()


def Browse_PlayShniden(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    r = re.compile('{"online_id":"(.+?)","player":"(.+?)"').findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url, player in r:
            url = _url
            strona = url
            _name = player
            _title = player
            fanart = fanartAol
            labs = {}
            img=''
            contextLabs = {'title': _name, 'year': '0000', 'url': _url, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': ''}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayShniden2', 'site': site, 'section': section, 'title': _name, 'url': strona, 'img': img, 'fanart': fanart}
            labs['title'] = _title
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()



def Browse_PlayShniden2(url, page='', content='episodes', view='515'):
    if url == '':
        return
    urlload ='http://shinden.pl/xhr/'+ url +'/player_load'
    header = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'
    nURL(urlload, User_Agent=header, cookie_file=cookie, load_cookie='', save_cookie=True)
    time.sleep(5)
    url = 'http://shinden.pl/xhr/'+ url +'/player_show'
    data = nURL(url, User_Agent=header, cookie_file=cookie, load_cookie=True)
    r = re.compile("flashvars=.+?hd\.file=(.+?)&").findall(data)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url in r:
            url = _url
    r = re.compile('<iframe src="http://(.+?)"').findall(data)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url in r:
            url = _url
    r = re.compile('<embed src="http://(.+?) quality="high" ').findall(data)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url in r:
            url = _url
    r = re.compile('flashvars="streamer=(.+?)"').findall(data)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url in r:
            url = _url
    r = re.compile('src="(.+?)"').findall(data)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url in r:
            print _url
            url = _url
            print url
            if ('vk' in url):
                _name = 'VK'
            elif ('google' in url):
                _name = 'Google video'
            elif ('video.sibnet.ru' in url):
                url = url.replace('swf', 'php')
                print url
                _name = 'Sibnet.ru'
            elif ('mp4upload.com' in url):
                _name = 'Mp4upload'
            elif ('dailymotion' in url):
                _name = 'Dailymotion'
            elif ('tune.pk' in url):
                _name = 'Tune'
            elif ('archive.org' in url):
                _name = 'Archive'
                url = url.replace('http:', '')
                url = 'http:' + url
            elif ('www.wrzuta.pl' in url):
                _name = 'Wrzuta'
            elif ('http://myvi.ru/' in url):
                _name = 'Myvi.ru - brak obsługi'
            elif ('anime-shinden.info/player' in url):
                _name = 'AnimeShniden player'
            elif ('peteava.ro' in url):
                _name = 'Peteava'
            elif ('vplay.ro' in url):
                _name = 'Vplay'
            else:
                _name = 'Inny Host'
            fanart = fanartAol
            labs = {}
            contextLabs = {'title': _name, 'year': '0000', 'url': _url, 'img':'', 'fanart': fanart, 'DateAdded': '', 'plot': ''}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': _name, 'url': url, 'img': '', 'fanart': fanart}
            labs['title'] = _name
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img='', contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()
