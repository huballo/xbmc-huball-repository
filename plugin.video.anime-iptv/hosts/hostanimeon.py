# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-On
###############################################################################
###############################################################################
### Imports ###
import re
from common import (_addon, addpr, nURL, eod, ContextMenu_Movies, ContextMenu_Series, ContextMenu_Episodes, set_view, addst, addonPath)
from metahandler import metahandlers
#from metahandler import metacontainers
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
mainSite = 'http://animeon.pl/'
metaget = metahandlers.MetaData(preparezip=False)
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'


def Pageanimeon(url, page='', metamethod=''):
    html = nURL(url)
    Browse_ItemAon(html, metamethod)
    eod()


def Browse_ItemAon(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    r = re.compile("overflow: hidden;'><strong><a href='(.+?)'>(.+?)</a></strong>").findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for _url, _name in r:
            strona = _url
            plot = ""
            img = ""
            fanart = fanartAol
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
###
            pars = {'mode': 'EpisodesAnimeon', 'site': site, 'section': section, 'title': _name, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': _name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            if   section == 'movie':
                contextMenuItems = ContextMenu_Movies(contextLabs)
            elif section == 'animeon':
                contextMenuItems = ContextMenu_Series(contextLabs)
            else:
                contextMenuItems = []
            labs['title'] = _name
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# szukanie następnej strony
    npage = url[:-2] + str(int(url[-2:]) + 20)
    if -1 != html.find("div class='pagenav"):
            _addon.add_directory({'mode': 'Pageanimeon', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartAol, img=nexticon)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesAnimeon(url, page='', content='episodes', view='515'):
#    print url
    if url == '':
        return
    html = nURL(url)
    idx = html.find("<div class='anime-desc-title'><h2>Odcinki</h2></div>")
    if idx == -1:
        return
    idx2 = html.find('<div class="float-left"><h2 class="commentsFormH">Komentarze</h2></div>', idx)
    if idx2 == -1:
        return
    htmllink = html[idx:idx2]
    r = re.compile("<a href='(.+?)'><b>(.+?)</b> - (.+?)</a>").findall(htmllink)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url, xx, _tytul in r:
            _name = _tytul.replace('o', 'O')
            image = re.compile("<img src='http://(.+?)' style='margin:2px").findall(html)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    img = "http://" + foto
            else:
                image = re.compile("<img src='(.+?)' style='margin:").findall(html)
                ItemCount = len(image)
                if len(image) > 0:
                    for foto in image:
                        img = mainSite + foto
                else:
                    img = ""
            fanart = fanartAol
            plot = ""
            strona = _url
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
###
            contextLabs = {'title': _name, 'year': '0000', 'url': _url, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'Version', 'site': site, 'section': section, 'title': _name, 'url': strona, 'img': img, 'fanart': fanart}
            labs['title'] = _name
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()


def Browse_Version(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    idx = html.find("<div class='version-list'><ul>")
    if idx == -1:
        return
    idx2 = html.find("<a>Oznacz jako obejrzany</a>", idx)
    if idx2 == -1:
        return
    htmllink = html[idx:idx2]
    r = re.compile("<li><a href='(.+?)'>Wersja (.+?)</a><li>").findall(htmllink)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url, wersja in r:
            _url = _url.replace('http://animeon.com.pl/', '')
            _name = wersja
            _url = mainSite + _url
            fanart = fanartAol
            plot = ""
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
            html = nURL(_url)
            idx = html.find("<div class='float-left player-container' style='display: none'><center>")
            if idx == -1:
                return
            idx2 = html.find("<br><br>", idx)
            if idx2 == -1:
                return
            htmllink = html[idx:idx2]
            r = re.compile("src='(.+?)'").findall(htmllink)
            ItemCount = len(r)
            if len(r) > 0:
                for  _url in r:
                    url2 = _url
                    if ('video.sibnet.ru' in url2):
                        url2 = url2.replace('swf', 'php')
                    elif ('archive.org' in url2):
                        url2 = url2.replace('http:', '')
                        url2 = 'http:' + url2
                    elif ('animeon.com.pl/episodes/players/vk.php' in url2):
                        html = nURL(url2)
                        r = re.compile("src='(.+?)'").findall(html)
                        ItemCount = len(r)
                        if len(r) > 0:
                            for  url in r:
                                url2 = url
###
            contextLabs = {'title': _name, 'year': '0000', 'url': url, 'fanart': fanart, 'DateAdded': ''}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': _name, 'url': url2, 'fanart': fanart}
            labs['title'] = _name
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('tvshows-view')))
    eod()




