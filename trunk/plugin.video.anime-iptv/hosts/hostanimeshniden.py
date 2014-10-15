# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Shinden
###############################################################################
###############################################################################
### Imports ###
import re
from common import (_addon, addpr, nURL, eod, ContextMenu_Movies, ContextMenu_Series, ContextMenu_Episodes, set_view, addst, addonPath, html_entity_decode)
from metahandler import metahandlers
#from metahandler import metacontainers
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
metaget = metahandlers.MetaData(preparezip=False)
fanartAol = addonPath + '/art/japan/fanart.jpg'
iconShniden = addonPath + '/art/japan/animeshniden.jpg'
mainSite5 = 'http://www.anime-shinden.info/'

def Pageshniden(url, page='', metamethod=''):
    html = nURL(url)
    Browse_ItemShniden(html, metamethod)
    eod()


def Browse_ItemShniden(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    idx = html.find('<dl class="sub-nav">')
    if idx == -1:
        return
    idx2 = html.find('</body>', idx)
    if idx2 == -1:
        return
    html = html[idx:idx2]
    r = re.compile('<a href="(.+?.html)">(.+?) </a>').findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for _url, _tytul in r:
            _name2 = html_entity_decode(_tytul)
            strona = _url
### scraper
            meta = metaget.get_meta('tvshow', _name2)
            fanart = str(meta['backdrop_url']).replace('u','')
            img = str(meta['cover_url']).replace('u','')
            plot = meta['plot']
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
###
            pars = {'mode': 'EpisodesShniden', 'site': site, 'section': section, 'title': _name2, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': _name2, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            if   section == 'movie':
                contextMenuItems = ContextMenu_Movies(contextLabs)
            elif section == 'shnidenodc':
                contextMenuItems = ContextMenu_Series(contextLabs)
            else:
                contextMenuItems = []
            labs['title'] = _name2
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_GenreShniden(url,content='episodes'):
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
    html = nURL(url)
    idx = html.find('><div id="news-id')
    if idx == -1:
        return
    idx2 = html.find('</td>', idx)
    if idx2 == -1:
        return
    htmllink = html[idx:idx2]
    r = re.compile('<a href=".+?(/.+?.html)".+?>(?:<b>)*(.+?)(?:</b>)*</a>').findall(htmllink)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url, _tytul in r:
            _name = _tytul
            _url =  'http:' + _url
            _title = _name
#            image = re.compile("<img src='http://(.+?)' style='margin:2px").findall(html)
 #           ItemCount = len(image)
  ##             for foto in image:
    #                img = "http://" + foto
     #       else:
      #          image = re.compile("<img src='(.+?)' style='margin:").findall(html)
       #         ItemCount = len(image)
        ####     else:
            #        img = ""
            img = ''
            fanart = fanartAol
#            opis = re.compile('<font face="Trebuchet MS">(.+?)</font>').findall(html)
#            ItemCount = len(opis)
#            if len(opis) > 0:
#                for desc in opis:
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
            pars = {'mode': 'PlayShniden', 'site': site, 'section': section, 'title': _name, 'url': strona, 'img': img, 'fanart': fanart}
            labs['title'] = _title
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()


def Browse_PlayShniden(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    idx = html.find('<!-- tab containers -->')
    if idx == -1:
        return
    idx2 = html.find("<script>", idx)
    if idx2 == -1:
        return
    data = html[idx:idx2]
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
            contextLabs = {'title': _name, 'year': '0000', 'url': url, 'fanart': fanart, 'DateAdded': ''}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': _name, 'url': url, 'fanart': fanart}
            labs['title'] = _name
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('tvshows-view')))
    eod()