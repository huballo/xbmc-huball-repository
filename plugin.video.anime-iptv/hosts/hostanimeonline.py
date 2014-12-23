# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Online
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
mainSite4 = 'http://anime-odcinki.pl/'
metaget = metahandlers.MetaData(preparezip=False)
fanartAol = addonPath + '/art/japan/fanart.jpg'

def Pageanimeonline(url, page='', metamethod=''):
    html = nURL(url)
    Browse_ItemAol(html, metamethod)
    eod()


def Browse_ItemAol(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    idx = html.find('<h1>Anime na liter')
    if idx == -1:
        return
    idx2 = html.find('</strong>', idx)
    if idx2 == -1:
        return
    html = html[idx:idx2]
    html = html.replace('C&#179;-bu','')
    r = re.compile('<a href="(.+?).php(.+?)" title="(.+?)">(.+?) \((.+?)\)</a>').findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for xx, _url, _name, _tytul, year in r:
            _name2 = (_tytul + " (" + year + ")").encode("utf-8")
            name = _tytul.encode("utf-8")
            if "Drama" in xx:
                strona = mainSite4 + 'Drama/articles.php' + _url
            else:
                strona = mainSite4 + 'articles.php' + _url
### scraper
            meta = metaget.get_meta('tvshow', name)
            fanart = str(meta['backdrop_url']).replace('u','')
            img = str(meta['cover_url']).replace('u','')
            plot = meta['plot']
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
###
            pars = {'mode': 'EpisodesAnime', 'site': site, 'section': section, 'title': _name2, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': _name2, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            if   section == 'movie':
                contextMenuItems = ContextMenu_Movies(contextLabs)
            elif section == 'animeonline':
                contextMenuItems = ContextMenu_Series(contextLabs)
            elif section == 'animedrama':
                contextMenuItems = ContextMenu_Series(contextLabs)
            else:
                contextMenuItems = []
            labs['title'] = _name2
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesAnime(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    idx = html.find("align='center'><center><h")
    if idx == -1:
        return
    idx2 = html.find('</div>', idx)
    if idx2 == -1:
        return
    htmllink = html[idx:idx2]
    r = re.compile("<a href=(.+?) target='_blank'>(.+?)</a>").findall(htmllink)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url, _tytul in r:
            _name = _tytul.encode("utf-8")
            _url = _url.replace('\'', '')
            _url2 = 'http://anime-odcinki.pl' + _url.replace('http://anime-odcinki.pl','')
            _title = _name
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
                        img = mainSite4 + foto
                else:
                    img = ""
            fanart = fanartAol
#            opis = re.compile('<font face="Trebuchet MS">(.+?)</font>').findall(html)
#            ItemCount = len(opis)
#            if len(opis) > 0:
#                for desc in opis:
            plot = ""
            strona = _url2
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
###
            contextLabs = {'title': _name, 'year': '0000', 'url': _url2, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayAnime', 'site': site, 'section': section, 'title': _name, 'url': strona, 'img': img, 'fanart': fanart}
            labs['title'] = _title
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()


def Browse_PlayAnime(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = nURL(url)
    idx = html.find('<div id="switcher-panel"></div>')
    if idx == -1:
        return
    idx2 = html.find("<div class=", idx)
    if idx2 == -1:
        return
    htmllink = html[idx:idx2]
    htmllink = htmllink.lower()
    r = re.compile('src="(.+?)"').findall(htmllink)
    ItemCount = len(r)
    if len(r) > 0:
        for  _url in r:
            url = _url.replace("&hd=3", "")
            if ('vk' in url):
                _name = 'VK'
            elif ('google' in url):
                _name = 'Google video'
            elif ('video.sibnet.ru' in url):
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
            elif ('vidfile' in url):
                _name = 'Vidfile'
            elif ('cloudy.ec' in url):
                _name = 'Cloudy'
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


