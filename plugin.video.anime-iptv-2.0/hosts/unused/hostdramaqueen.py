# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
#DramaQueen
###############################################################################
###############################################################################
### Imports ###
from common import *
from common import (_addon)
import weblogin2
import gethtml2
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


def PageDramaQueen_drama(url, page='', metamethod=''):
    logged_inDrama = weblogin2.doLogin(addonPath, loginDrama, passwordDrama)
    html = nURL(url)
    html = html.encode('utf-8')
    Browse_ItemsDramaQueen_drama(html, metamethod)
    eod()


def Browse_ItemsDramaQueen_drama(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    idx = html.find("<div id='main' data-scroll-offset='88'>")
    if idx == -1:
        return
    idx2 = html.find('<span class="seperator extralight-border">', idx)
    if idx2 == -1:
        return
    html = html[idx:idx2]
    html = html.replace("\"", "\'")
    r = re.compile("uploads(.+?)'(.+?)href='(.+?)' title='(.+?)'>").findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for img, xxx, _url, _name in r:
            strona = _url
            _name2 = _name
            html2 = nURL(strona)
            image = re.compile("<img src='http://www.dramaqueen.pl/wp-content/uploads/(.+?)' width").findall(html2)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    fanart = "http://www.dramaqueen.pl/wp-content/uploads/" + foto
            else:
                    fanart = ""
            img = "http://www.dramaqueen.pl/wp-content/uploads/" + img
#szukanie opisu
            idx = html2.find('<footer class="entry-footer"></footer></article>')
            if idx == -1:
                return
            idx2 = html2.find('</div>    </div>', idx)
            if idx2 == -1:
                return
            desc = html2[idx:idx2]
            desc = desc.replace("\n", "")
            opis = re.compile('itemprop="text" ><p><em>(.+?)</em></p>').findall(desc)
            ItemCount = len(opis)
            if len(opis) > 0:
                for desc in opis:
                    plot = clean_html(desc)
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
            pars = {'mode': 'EpisodesDramaQueen_drama', 'site': site, 'section': section, 'title': _name2, 'url': strona, 'img': img, 'fanart': fanart}
            contextLabs = {'title': _name2, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
            if   section == 'movie':
                contextMenuItems = ContextMenu_Movies(contextLabs)
            elif section == 'Dramadrama':
                contextMenuItems = ContextMenu_Series(contextLabs)
            else:
                contextMenuItems = []
            labs['title'] = _name2
            _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesDramaQueen_drama(url,page='',content='episodes',view='515'):
    html = gethtml2.get(url, addonPath)
    html = messupText(html, ciastko, True, True)
    idx = html.find('<div class="togglecontainer toggle_close_all')
    if idx == -1:
        return
    idx2 = html.find("</div></div></div>", idx)
    if idx2 == -1:
        return
    html2 = html[idx:idx2]
    html2 = html2.replace("\n", "")
    html2 = html2.replace("#038;", "")
    html2 = html2.replace("&hd=3", "")
    s = '>Odcinek(.+?)<(.+?)src="(.+?)"'
    matches = re.compile(s).findall(html2)
    ItemCount = len(matches)
    if ItemCount > 0:
        for _name, xxx, _url in matches:
            _url2 = _url
            _name = "Odcinek" + _name
            _title = _name
            strona = _url2
            image = re.compile("<img src='http://www.dramaqueen.pl/wp-content/uploads/(.+?)' width").findall(html)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    fanart = "http://www.dramaqueen.pl/wp-content/uploads/" + foto
            else:
                    fanart = ""
            img = fanart
#wyciąganie opisu
            idx = html.find('itemprop="text" ><p><em>')
            if idx == -1:
                return
            idx2 = html.find("</em></p>", idx)
            if idx2 == -1:
                return
            plot = html[idx:idx2]
            plot = plot.decode("utf-8")
            plot = clean_html(plot)
            plot = plot.replace('itemprop="text" >', '')
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''

            contextLabs = {'title': _name, 'year': '0000', 'url': _url2, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': _name, 'url': strona, 'img': img, 'fanart': fanart}
            labs['title'] = _title
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('links-view')))
    eod()

#Drama Queen movie#
def Browse_PageDramaQueen_dramamovie(url, page='', metamethod=''):
    logged_inDrama = weblogin2.doLogin(addonPath, loginDrama, passwordDrama)
    html = nURL(url)
    html = html.encode('utf-8')
    Browse_ItemsDramaQueen_dramamovie(html, metamethod)
    eod()


def Browse_ItemsDramaQueen_dramamovie(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    idx = html.find("<div id='main' data-scroll-offset='88'>")
    if idx == -1:
        return
    idx2 = html.find('<span class="seperator extralight-border">', idx)
    if idx2 == -1:
        return
    html = html[idx:idx2]
    html = html.replace("\"", "\'")
    r = re.compile("uploads(.+?)'(.+?)href='(.+?)' title='(.+?)'>").findall(html)
    ItemCount = len(r)
    if len(r) > 0:
        for img, xxx, _url, _name in r:
            strona = _url
            _name2 = _name
            html2 = gethtml2.get(strona, addonPath)
            html2 = messupText(html2, ciastko, True, True)
            image = re.compile("<img src='http://www.dramaqueen.pl/wp-content/uploads/(.+?)' width").findall(html2)
            ItemCount = len(image)
            if len(image) > 0:
                for foto in image:
                    fanart = "http://www.dramaqueen.pl/wp-content/uploads/" + foto
            else:
                    fanart = ""
            img = "http://www.dramaqueen.pl/wp-content/uploads/" + img
#wyciąganie opisu
            idx = html2.find('itemprop="text" ><p><em>')
            if idx == -1:
                return
            idx2 = html2.find("</em></p>", idx)
            if idx2 == -1:
                return
            plot = html2[idx:idx2]
            plot = plot.decode("utf-8")
            plot = clean_html(plot)
            plot = plot.replace('itemprop="text" >', '')
            labs = {}
            try:
                labs['plot'] = plot
            except:
                labs['plot'] = ''
#wyciąganie linku do filmu
            s = '<iframe src="http://vk.com/(.+?)"'
            matches = re.compile(s).findall(html2)
            ItemCount = len(matches)
            if ItemCount > 0:
                for _url in matches:
                    _url = 'http://vk.com/' + _url
                    _url = _url.replace("#038;", "")
                    _url = _url.replace("&hd=3", "")
            contextLabs = {'title': _name2, 'year': '0000', 'url': strona, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
            contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
            pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': _name2, 'url': _url, 'img': img, 'fanart': fanart}
            labs['title'] = _name2
            _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, int(addst('tvshows-view')))
    eod()