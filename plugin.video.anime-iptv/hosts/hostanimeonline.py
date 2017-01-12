# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Online
# THANKS for support to samsamsam !!!!
# Some part of code comes from iptvplugin https://gitlab.com/iptvplayer-for-e2/iptvplayer-for-e2
###############################################################################
###############################################################################
### Imports ###
import re
import xbmcaddon
import os
import sys

from common import (_addon, addpr, nURL, eod, set_view, addst, addonPath, GetDataBeetwenMarkers, byteify, clean_html, tfalse,ParseDescription)
from contextmenu import ( ContextMenu_Series, ContextMenu_Episodes)
try:
    import json
except:
    import simplejson as json

__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'crypto'))

from keyedHash.evp import EVP_BytesToKey
from cipher.aes_cbc import AES_CBC
from binascii import a2b_hex, a2b_base64
from hashlib import md5
####################################################
# Api keys
####################################################
youtube_api_key = 'AIzaSyBbDY0UzvF5Es77M7S1UChMzNp0KsbaDPI'
### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
mainSite4 = 'http://anime-odcinki.pl/'
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
host = 'AnimeOnline'


def Pageanimeonline(url, page, metamethod=''):
    html = nURL(url)
    Browse_ItemAol(html, page, metamethod)
    eod()


def Browse_ItemAol(html, page, metamethod='', content='movies', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, 'Tytu', '</table>', False)[1]
    page = page.lower()
    data = re.findall('<a href="http://anime-odcinki.pl/anime/' + page+ '(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    for item in data:
        strona =  'http://anime-odcinki.pl/anime/' + page + item[0]
        name = item[1].encode("utf-8")
        name = ParseDescription(name)
### scraper
        if (tfalse(addst("aodc-thumbs")) == True):
            import scraper
            scrap = scraper.scraper_check(host, name)
            try:
                if (name not in scrap):
                    if '?page=0'in strona:
                        strona2 = strona.replace('?page=0','')
                    else:
                        strona2 = strona
                    html = nURL(strona2)
                    html = GetDataBeetwenMarkers(html, 'field-name-field-okladka field-type-image field-label-above', '<p>&nbsp;</p>', False)[1]
                    data = re.findall('<img src="(.+?)"', html)
                    ItemCount = len(data)
                    if len(data) > 0:
                        for item in data:
                            img = item
                    else:
                        img = ''
                    data = re.findall('<p><p>(.+?)</p>', html)
                    ItemCount = len(data)
                    if len(data) > 0:
                        for item in data:
                            plot = ParseDescription(item)
                    else:
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
            plot =''
        fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        pars = {'mode': 'EpisodesAnime', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if section == 'animeonline':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesAnime(url, page='', content='episodes', view='515'):
    if url == '':
        return
    if '?page=0'in url:
        link = url.replace('?page=0','')
    else:
        link = url
    html = GetDataBeetwenMarkers(nURL(link), '<div id="block-views-lista-odcink-w-block', '</ul>', False)[1]
    data = re.findall('<a href="(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    for item in data:
        url2 = item[0]
        name = item[1].encode("utf-8")
        name = ParseDescription(name)
        img = ""
        fanart = fanartAol
        plot = ""
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
###
        contextLabs = {'title': name, 'year': '0000', 'url': url2, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
        contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
        pars = {'mode': 'PlayAnime', 'site': site, 'section': section, 'title': name, 'url': url2, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# next page
#    npage = url[:-1] + str(int(url[-1:]) + 1)
#    if -1 != html.find("do strony "):
#        _addon.add_directory({'mode': 'EpisodesAnime', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartAol, img=nexticon)
    set_view(content, view_mode=addst('links-view'))
    eod()


def encryptPlayerUrl(data):
    print("_encryptPlayerUrl data[%s]" % data)
    decrypted = ''
    try:
        data = byteify(json.loads(data))
        salt = a2b_hex(data["v"])
        key, iv = EVP_BytesToKey(md5, "s05z9Gpd=syG^7{", salt, 32, 16, 1)
        if iv != a2b_hex(data.get('b', '')):
            print("_encryptPlayerUrl IV mismatched")
        if 0:
            from Crypto.Cipher import AES
            aes = AES.new(key, AES.MODE_CBC, iv, segment_size=128)
            decrypted = aes.decrypt(a2b_base64(data["a"]))
            decrypted = decrypted[0:-ord(decrypted[-1])]
        else:
            kSize = len(key)
            alg = AES_CBC(key, keySize=kSize)
            decrypted = alg.decrypt(a2b_base64(data["a"]), iv=iv)
            decrypted = decrypted.split('\x00')[0]
        decrypted = "%s" % json.loads(decrypted).encode('utf-8')
    except:
        decrypted = ''
    return decrypted


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Browse_PlayAnime(url, page='', content='episodes', view='515'):
    if url == '':
        return
    players = GetDataBeetwenMarkers(nURL(url), '<div id="video-player-control">', "</center>")[1]
    players = players.replace('\n', '')
    players = players.replace('\r', '')
    players = players.replace('  ', '')
    lista = re.compile("data-hash='{(.+?)}'>(.+?)</div>").findall(players)
    lista = [tuple(reversed(t)) for t in lista]
    import xbmcgui
    d = xbmcgui.Dialog()
    item = d.select("Wybór jakości", getItemTitles(lista))
    if item != -1:
        player = str(lista[item][1])
        player = '{' + player + '}'
        item = encryptPlayerUrl(player)
        item = item.replace('https', '')
        item = item.replace('http', '')
        url = item.replace("&hd=3", "")
        url = "http" + url.replace("amp;", "")
        from common import PlayFromHost
        PlayFromHost(url)
    eod()


def Recenzje(url, page='', metamethod=''):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=UUcxW52ZGVQ8ThhwgpB-XPjQ&key=' + youtube_api_key
    html = nURL(url)
    Browse_ItemRecenzje(html, metamethod)
    eod()


def Browse_ItemRecenzje(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    data = byteify(json.loads(html))['items']
    ItemCount = len(data)
    for x in range(len(data)):
        item = data[x]
        name = item['snippet']['title']
        plot = item['snippet']['description']
        plot = clean_html(plot)
        img = item['snippet']['thumbnails']['high']['url']
        url = item['snippet']['resourceId']['videoId']
        strona = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url
        fanart = fanartAol
        labs = {}
        try:
            labs['plot'] = plot
        except:
            labs['plot'] = ''
        contextLabs = {'title': name, 'year': '0000', 'url': strona, 'img': img, 'fanart': fanart, 'DateAdded': '', 'plot': labs['plot']}
        contextMenuItems = ContextMenu_Episodes(labs=contextLabs)
        pars = {'mode': 'PlayFromHost', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=False, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
#    set_view(content, int(addst('links-view')))
    eod()





