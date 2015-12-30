# -*- coding: utf-8 -*-
###############################################################################
###############################################################################
# Anime-Online
# THANKS for support do samsamsam !!!!
# Some part of code comes from iptvplugin https://gitlab.com/iptvplayer-for-e2/iptvplayer-for-e2
###############################################################################
###############################################################################
### Imports ###
import re
import xbmcaddon
import os
import sys

from common import (_addon, addpr, nURL, eod, ContextMenu_Movies, ContextMenu_Series, ContextMenu_Episodes, set_view, addst, addonPath, GetDataBeetwenMarkers, byteify)
from metahandler import metahandlers
try:
    import json
except:
    import simplejson as json

__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'crypto'))

from keyedHash.evp import EVP_BytesToKey
from cipher.aes_cbc  import AES_CBC
from binascii import a2b_hex, a2b_base64
from hashlib import md5

### ##########################################################################
### ##########################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
mainSite4 = 'http://anime-odcinki.pl/'
metaget = metahandlers.MetaData(preparezip=False)
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'


def Pageanimeonline(url, page='', metamethod=''):
    html = nURL(url)
    Browse_ItemAol(html, metamethod)
    eod()


def Browse_ItemAol(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, 'Tytu', '</table>', False)[1]
    data = re.findall('<a href="/(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    for item in data:
        strona = mainSite4 + item[0] + '?page=0'
        name = item[1].encode("utf-8")
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
        pars = {'mode': 'EpisodesAnime', 'site': site, 'section': section, 'title': name, 'url': strona, 'img': img, 'fanart': fanart}
        contextLabs = {'title': name, 'url': strona, 'img': img, 'fanart': fanart, 'todoparams': _addon.build_plugin_url(pars), 'site': site, 'section': section, 'plot': labs['plot']}
        if   section == 'movie':
            contextMenuItems = ContextMenu_Movies(contextLabs)
        elif section == 'animeonline':
            contextMenuItems = ContextMenu_Series(contextLabs)
        elif section == 'animedrama':
            contextMenuItems = ContextMenu_Series(contextLabs)
        else:
            contextMenuItems = []
        labs['title'] = name
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
    set_view(content, view_mode=addst('tvshows-view'))


def Browse_EpisodesAnime(url, page='', content='episodes', view='515'):
    if url == '':
        return
    html = GetDataBeetwenMarkers(nURL(url), '<div class="views-row views-row-1 views-row-odd views-row-first">', '</section> <!-- /.block -->', False)[1]
    data = re.findall('<div class="field-content lista_odc_tytul_pozycja"><a href="/(.+?)">(.+?)</a>', html)
    ItemCount = len(data)
    print data
    for item in data:
        url2 = mainSite4 + item[0]
        name = item[1].encode("utf-8")
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
        _addon.add_directory(pars, labs, is_folder=True, fanart=fanart, img=img, contextmenu_items=contextMenuItems, total_items=ItemCount)
# next page
    npage = url[:-1] + str(int(url[-1:]) + 1)

    if -1 != html.find("do strony "):
        _addon.add_directory({'mode': 'EpisodesAnime', 'site': site, 'section': section, 'url': npage, 'page': npage}, {'title': "Next page"}, is_folder=True, fanart=fanartAol, img=nexticon)
    set_view(content, view_mode=addst('links-view'))
    eod()

# eccryptPlayerUrl from iptvplayer https://gitlab.com/iptvplayer-for-e2/iptvplayer-for-e2
def encryptPlayerUrl(data):
    print("_encryptPlayerUrl data[%s]" % data)
    decrypted = ''
    try:
        data = byteify( json.loads(data) )
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
        decrypted = "%s" % json.loads( decrypted ).encode('utf-8')
    except:
        decrypted = ''
    return decrypted


def Browse_PlayAnime(url, page='', content='episodes', view='515'):
    if url == '':
        return
    players = GetDataBeetwenMarkers(nURL(url), '<div class="content">', "<ul")[1]
    players = re.findall('<div class="field-item even">{(.+?)}</div></div>', players)
    ItemCount = len(players)
    for item in players:
        player = '{' + item + '}'
        item = encryptPlayerUrl(player)
        item = item.replace('https', '')
        item = item.replace('http', '')
        url = item.replace("&hd=3", "")
        url = "http" + url.replace("amp;", "")
        print url
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
        elif ('vshare' in url):
            _name = 'Vshare'
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


def Recenzje(url, page='', metamethod=''):
    html = nURL(url)
    Browse_ItemRecenzje(html, metamethod)
    eod()


def Browse_ItemRecenzje(html, metamethod='', content='tvshows', view='515'):
    if (len(html) == 0):
        return
    html = GetDataBeetwenMarkers(html, '<div class="yt-lockup-content">', '<span class="yt-spinner">', False)[1]
    data = re.findall('href="(.+?)">(.+?)</a><span class="accessible-description"', html)
    ItemCount = len(data)
    for item in data:
        strona = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % item[0].replace('/watch?v=', '')
        name = item[1].encode("ascii",'replace')
        fanart = fanartAol
        img = 'https://i.ytimg.com/vi_webp/'+ item[0].replace('/watch?v=', '') +'/mqdefault.webp'
        plot = ''
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
    set_view(content, int(addst('links-view')))
    eod()

