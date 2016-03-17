# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Diff-anime
###############################################################################
###############################################################################
### Imports ###
import re
from common import (_addon, addpr, nURL, eod, ContextMenu_Movies, ContextMenu_Series, ContextMenu_Episodes, set_view, addst, addonPath, messupText,clean_html)
import weblogin
import gethtml
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
fanartSite = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'

# logowanie
login = addst('username', '')
password = addst('password', '')
loginDrama = addst('username2', '')
passwordDrama = addst('password2', '')
ciastko = addonPath


def PageDiff(url, page='', metamethod=''):
    logged_inDiff = weblogin.doLogin(addonPath, login, password)
    html = nURL(url)
    Browse_Items(html, metamethod)
    eod()


def Browse_Items(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    r = re.compile("</a><div class='con'><a href='/(.+?)'>(.+?)</a><p>").findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for _url, _name in r:
            strona = 'http://diff-anime.pl/' + _url
            html2 = nURL(strona)
            _name2 = _name
#  grafika
            image = re.compile("</div><div class='content'><div class='con'><a href='(.+?)' class='fbox'>").findall(html2)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    img = "http://diff-anime.pl" + foto
            else:
                    img = ""
#  fanart
            if "Nie dodano kadrów do tej serii." in html2:
                fanart = fanartSite
            else:
                    image2 = re.compile("<h2>Kadry</h2></div><div class='content'><a href='(.+?)' class='fbox'>").findall(html2)
                    ItemCount = len(image)
                    if len(image) > 0:
                        for _fanart in image2:
                            fanart = "http://diff-anime.pl" + _fanart
                    else:
                            fanart = img
#  opis
            opis = re.compile("<h2>Opis anime</h2></div><div class='content'><div class='con'>(.+?)</div>").findall(html2)
            ItemCount = len(opis)
            if len(opis) > 0:
                for desc in opis:
                    plot = unicode(desc,"utf-8")
            else:
                    opis = re.compile("<h2>Opis anime</h2></div><div class='content'><div class='con'>(.+?)<").findall(html2)
                    ItemCount = len(opis)
                    if len(opis) > 0:
                        for desc in opis:
                            plot = unicode(desc,"utf-8")
                    else:
                            opis = re.compile("<div id='pDesc' class='panel'><div class='head'><h2>Opis anime</h2></div><div class='content'><div class='con'>(.+?)<br />").findall(html2)
                            ItemCount = len(opis)
                            if len(opis) > 0:
                                for desc in opis:
                                    plot = unicode(desc,"utf-8")
                            else:
                                    plot = "Nie dodano jeszcze opisu do tej serii."
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
###
            pars = {'mode': 'EpisodesDiff', 'site': site, 'section': section, 'title': _name2, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': _name2, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            if   section == 'movie':
                contextMenuItems = ContextMenu_Movies(contextLabs)
            elif section == 'diffanime':
                contextMenuItems = ContextMenu_Series(contextLabs)
            else:
                contextMenuItems = []
            labs['title'] = _name2
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# szukanie następnej strony
    npage = url[:-2] + str(int(url[-2:]) + 10)
    if -1 != html.find("div class='pagenav") and -1 != html.find("class='img"):
            _addon.add_directory({'mode': 'Page', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartSite, img=nexticon)
    set_view(content, view_mode=addst('tvshows-view'))


# listowanie odcinków
def Browse_EpisodesDiff(url, page='', content='episodes', view='515'):
    html = gethtml.get(url + '/odcinki', addonPath)
    htmlplot = gethtml.get(url , addonPath)
    html = messupText(html, ciastko, True, True)
    s = "#(.+?)</div><div class=.+?</div><div class='con3'><a href='(.+?)' class='i'>"
    matches = re.compile(s).findall(html)
    ItemCount = len(matches)
    if ItemCount > 0:
        for  _nazwa, _url in matches:
            _url2 = 'http://diff-anime.pl' + _url
            _name = 'Odcinek' + _nazwa
            _title = '' + _name
#  grafika
            image = re.compile("</div><div class='content'><div class='con'><a href='(.+?)' class='fbox'>").findall(html)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    img = "http://diff-anime.pl" + foto
            else:
                    img = ""
#  fanart
            if "Nie dodano kadrów do tej serii." in html:
                fanart = fanartSite
            else:
                image2 = re.compile("<h2>Kadry</h2></div><div class='content'><a href='(.+?)' class='fbox'>").findall(html)
                ItemCount = len(image)
                if len(image) > 0:
                    for _fanart in image2:
                        fanart = "http://diff-anime.pl" + _fanart
                else:
                        fanart = img
#  opis
            opis = re.compile("<h2>Opis anime</h2></div><div class='content'><div class='con'>(.+?)</div>").findall(htmlplot)
            ItemCount = len(opis)
            if len(opis) > 0:
                for desc in opis:
                    plot = unicode(desc,"utf-8")
            else:
                    opis = re.compile("<h2>Opis anime</h2></div><div class='content'><div class='con'>(.+?)<").findall(htmlplot)
                    ItemCount = len(opis)
                    if len(opis) > 0:
                        for desc in opis:
                            plot = unicode(desc,"utf-8")
                    else:
                            opis = re.compile("<div id='pDesc' class='panel'><div class='head'><h2>Opis anime</h2></div><div class='content'><div class='con'>(.+?)<br />").findall(htmlplot)
                            ItemCount = len(opis)
                            if len(opis) > 0:
                                for desc in opis:
                                    plot = unicode(desc,"utf-8")
                            else:
                                    plot = ""
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
#  wyciąganie linku do mp4
            html2 = gethtml.get(_url2, addonPath)
            _link = re.compile("'file': '(.+?)',").findall(html2)
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
##Aktualnosci


def Browse_PageDiffAKT(url, page='', metamethod=''):
    html = nURL(url)
    Browse_Aktualnosci(html, metamethod)
    eod()


def Browse_Aktualnosci(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    r = re.compile("<div class='head'><h2><a href='/news/(.+?)'>(.+?)</a>").findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for _url, _name in r:
            strona = 'http://diff-anime.pl' + '/news/' + _url
            html2 = nURL(strona)
            _name2 = clean_html(_name)
            _name2 = _name.replace(";", "")
#
            idx = html2.find("class='news-category' />")
            if idx == -1:
                return
            idx2 = html2.find("</div>", idx)
            if idx2 == -1:
                return
            plot = html2[idx:idx2]
            plot = clean_html(plot)
            plot = plot.replace("class='news-category' />", "")

#
            image = re.compile("<div class='content'><img src='(.+?)' alt='(.+?)' class='news-category' />(.+?).<br />").findall(html2)
            ItemCount = len(image)
            if len(image) > 0:
                for foto, plot1, plot2 in image:
                    img = "http://diff-anime.pl" + foto
            fanart = fanartSite
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
# YOUTUBE LINK
            _link = re.compile('src="//www.youtube.com/embed/(.+?)"').findall(html2)
            ItemCount = len(_link)
            if len(_link) > 0:
                for link in _link:
                    _url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % link
            contextLabs = {'title': _name2, 'year': '0000', 'url': strona, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': _name2, 'url': _url, 'img': img, 'fanart': fanart}
            labs['title'] = _name2
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('tvshows-view')))
    eod()