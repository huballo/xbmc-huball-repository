# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Centrum
###############################################################################
###############################################################################
### Imports ###
import re
import urllib
from common import (_addon, addpr, nURL, eod, ContextMenu_Movies, ContextMenu_Series, ContextMenu_Episodes, set_view, messupText, addst, cFL_)

### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')


def PageCentrum(url, page='', metamethod=''):
    html = nURL(url)
    Browse_Itemscen(html, metamethod)
    eod()


def Browse_Itemscen(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    r = re.compile('<a href="http://anime-centrum.net/(.+?)" class="tip-(.+?) tip-style-2"').findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for _url, _x in r:
            strona = 'http://anime-centrum.net/' + _url
            html2 = nURL(strona)
#  nazwa
            tytul = re.compile('<meta property="og:title" content="(.+?)" />').findall(html2)
            ItemCount = len(tytul)
            if len(tytul) > 0:
                for _tytul in tytul:
                    _name2 = _tytul.encode('utf-8')
#  grafika
            image = re.compile('<meta property="og:image" content="(.+?)" />').findall(html2)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    img = foto
            else:
                img = ""
#  fanart
            image2 = re.compile('<!--dle_image_begin:(.+?)</a><!--dle_image_end-->').findall(html2)
            ItemCount = len(image2)
            if len(image2) > 0:
                for foto2 in image2:
                    strona2 = foto2
                    image3 = re.compile('http:(.+?).jpg').findall(strona2)
                    ItemCount = len(image3)
                    if len(image3) > 0:
                        for foto3 in image3:
                            fanart = "http:" + foto3 + ".jpg"
                    else:
                        fanart = img
#  opis
            opis = re.compile('<strong>Opis:</strong>(.+)').findall(html2)
            ItemCount = len(opis)
            if len(opis) > 0:
                for desc in opis:
                    plot = desc
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
###
            pars = {'mode': 'EpisodesCentrum', 'site': site, 'section': section, 'title': _name2, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': _name2, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            if   section == 'movie':
                contextMenuItems = ContextMenu_Movies(contextLabs)
            elif section == 'animecentrum':
                contextMenuItems = ContextMenu_Series(contextLabs)
            else:
                contextMenuItems = []
            labs['title'] = _name2
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesCentrum(url,page='',content='episodes',view='515'):
    if url == '':
        return
    html = nURL(url)
    html = messupText(html, True, True)
    s = '<a href="http://(.+?)">Odcinek(.+?)</a>'
    matches = re.compile(s).findall(html)
    ItemCount = len(matches)
    if ItemCount > 0:
        for _url, _nazwa in matches:
            _url2 = 'http://' + urllib.quote(_url)
            _name = 'Odcinek' + _nazwa
            _title = '' + cFL_(_name)
#  grafika
            image = re.compile('<meta property="og:image" content="(.+?)" />').findall(html)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    img = foto
            else:
                img = ""
#  fanart
            image2 = re.compile('<!--dle_image_begin:(.+?)</a><!--dle_image_end-->').findall(html)
            ItemCount = len(image2)
            if len(image2) > 0:
                for foto2 in image2:
                    strona2 = foto2
                    image3 = re.compile('http:(.+?).jpg').findall(strona2)
                    ItemCount = len(image3)
                    if len(image3) > 0:
                        for foto3 in image3:
                            fanart = "http:" + foto3 + ".jpg"
                    else:
                        fanart = img
#  opis
            opis = re.compile('<strong>Opis:</strong>(.+)').findall(html)
            ItemCount = len(opis)
            if len(opis) > 0:
                for desc in opis:
                    plot = desc
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
#  wyciąganie linku do mp4
            html2 = nURL(_url2)
            _link = re.compile("<source src='(.+?)' type='video/mp4' />").findall(html2)
            ItemCount = len(_link)
            if len(_link) > 0:
                for link in _link:
                    strona = link.replace(' ', '%20')
###
            contextLabs = {'title': _name, 'year': '0000', 'url': _url2, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': _name, 'url': strona, 'img': img, 'fanart': fanart}
            labs['title'] = _title
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()

