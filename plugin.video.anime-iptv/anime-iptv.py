# -*- coding: utf-8 -*-

### Imports ###
import xbmc
import xbmcaddon
import os
import sys


### ##########################################################################
### ##########################################################################
SiteName = 'AnimeIPTV'
SiteTag = 'AnimeIPTV'
mainSite = 'http://diff-anime.pl/'
mainSite2 = 'http://animeonline.co/'
mainSite3 = 'http://anime-joy.tv/'
mainSite4 = 'http://anime-odcinki.pl/'
mainSite5 = 'http://shinden.pl/'
mainSite6 = 'http://animeon.pl/'

__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'hosts'))
sys.path.append(os.path.join(addonPath, 'resources/libs'))

from common import (_addon, addpr, eod, set_view, addst, cFL, PlayFromHost)
from favourites import (fav__COMMON__add, fav__COMMON__remove, Fav_List)

iconSite = addonPath + '/art/icon.png'
iconAnime4fun = addonPath + '/art/japan/anime4fun.jpg'
iconDiff = addonPath + '/art/japan/diffanime.jpg'
iconOdcinki = addonPath + '/art/japan/animeodcinki.jpg'
iconShniden = addonPath + '/art/japan/animeshniden.jpg'
iconAnimeon = addonPath + '/art/japan/animeon.jpg'
iconAnimejoy = addonPath + '/art/japan/animejoy.jpg'
iconFavs = addonPath + '/art/japan/ulubione.jpg'
fanartSite = addonPath + '/art/japan/fanart.jpg'
fanartIPTV = addonPath + '/art/japan/fanart.jpg'
fanartAnime4fun = addonPath + '/art/japan/fanart.jpg'
fanartAol = addonPath + '/art/japan/fanart.jpg'
nexticon = addonPath + '/art/next.png'
iconspychu ="http://yt3.ggpht.com/-AAAZ6bEqVMk/VMVVsE8SP5I/AAAAAAAAAEY/81QRnXbTEXs/w1060-fcrop64=1,00005a57ffffa5a8-nd/Banner%2Bdla%2BSpychaGOTOWY.png"

# logowanie
login = addst('username', '')
password = addst('password', '')
loginDrama = addst('username2', '')
passwordDrama = addst('password2', '')
ciastko = addonPath
###

colors = {'0': 'white', '1': 'red', '2': 'blue', '3': 'green', '4': 'yellow', '5': 'orange', '6': 'lime', '7': '', '8': 'cornflowerblue', '9': 'blueviolet', '10': 'hotpink', '11': 'pink', '12': 'tan'}
CR = '[CR]'
MyAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
AonlineAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '3', '9']
AonlineDrama = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Anime4funalphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

MyBrowser = ['User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

###############################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
nmr = addpr('nmr', '')
sections = {'diffanime': 'diffanime', 'anime4fun': 'anime4fun', 'animejoy': 'animejoy', 'Dramadrama': 'Dramadrama', 'Dramamovie': 'Dramamovie','animeonline': 'animeonline','animeodc': 'animeodc', 'aktualnosci': "aktualnosci", 'movies': 'movies', 'animeshinden': 'animeshinden', 'shnidenodc': 'shnidenodc', 'shnidengat': 'shnidengat', 'animeon': 'animeon'}
thumbnail = addpr('img', '')
fanart = addpr('fanart', '')
page = addpr('page', '')
addonInfo = xbmcaddon.Addon().getAddonInfo
lang = xbmcaddon.Addon().getLocalizedString

###############################################################################
###############################################################################
# Anime4fun
###############################################################################
###############################################################################
def Anime4fun(mode, url, page):
    import hostanime4fun
    if mode == "Page4fun":
        hostanime4fun.Page4fun(url, page)
    elif mode == "Episodes4fun":
        hostanime4fun.Browse_Episodes4fun(url, page)
    elif mode == "PlayAnime4fun":
        hostanime4fun.Browse_PlayAnime4fun(url, page)


###############################################################################
###############################################################################
#Anime-joy
###############################################################################
###############################################################################
def Animejoy(mode, url, page):
    import hostanimejoy
    if mode == "Pagejoy":
        hostanimejoy.Pagejoy(url, page)
    elif mode == "Episodesjoy":
        hostanimejoy.Browse_Episodesjoy(url, page)
    elif mode == "PlayAnimejoy":
        hostanimejoy.Browse_PlayAnimejoy(url, page)


###############################################################################
###############################################################################
# Anime-Online
###############################################################################
###############################################################################
def AnimeOnline(mode, url, page):
    import hostanimeonline
    if mode == "Pageanimeonline":
        hostanimeonline.Pageanimeonline(url, page)
    elif mode == "EpisodesAnime":
        hostanimeonline.Browse_EpisodesAnime(url, page)
    elif mode == "PlayAnime":
        hostanimeonline.Browse_PlayAnime(url, page)
    elif mode == "recenzje":
        hostanimeonline.Recenzje(url)
    else:
        return
###############################################################################


def SubSubMenu():
###Anime-Online###
    if section == 'animeonline':
        tUrl = mainSite4 + 'anime'
        for az, xy in zip(AonlineAlphabet, AonlineAlphabet):
            _addon.add_directory({'mode': 'Pageanimeonline', 'site': site, 'section': section, 'url': tUrl, 'page' : xy}, {'title': az}, is_folder=True, fanart=fanartAol, img=addonPath + '/art/'+ az +'.png')
    if section == 'animedrama':
        tUrl = mainSite4 + 'Drama/viewpage.php?page_id='
        for az, xy in zip(MyAlphabet, AonlineDrama):
            _addon.add_directory({'mode': 'Pageanimeonline', 'site': site, 'section': section, 'url': tUrl + xy}, {'title': az}, is_folder=True, fanart=fanartAol, img=addonPath + '/art/'+ az +'.png')
    set_view('list', view_mode=addst('default-view'))
    eod()


def SubMenu():
###Anime4fun###
    if section == 'anime4fun':
        tUrl = mainSite2
        _addon.add_directory({'mode': 'Page4fun', 'site': site, 'section': section, 'url': tUrl + 'list-special' + '?page=1'}, {'title': '#'}, is_folder=True, fanart=fanartAnime4fun, img=addonPath + '/art/znak.png')
        for az in Anime4funalphabet:
            _addon.add_directory({'mode': 'Page4fun', 'site': site, 'section': section, 'url': tUrl + 'list-' + az + '?page=1', 'page': az}, {'title': az}, is_folder=True, fanart=fanartAnime4fun, img=addonPath + '/art/'+ az +'.png')
###animejoy##
    if section == 'animejoy':
        tUrl = mainSite3 + 'animelist#'
        _addon.add_directory({'mode': 'Pagejoy', 'site': site, 'section': section, 'url': tUrl + '1'}, {'title': '#'}, is_folder=True, fanart=fanartAnime4fun, img=addonPath + '/art/znak.png')
        for az in MyAlphabet:
            _addon.add_directory({'mode': 'Pagejoy', 'site': site, 'section': section, 'url': tUrl + az, 'page': az}, {'title': az}, is_folder=True, fanart=fanartAnime4fun, img=addonPath + '/art/'+ az +'.png')
###Anime-Online###
    if section == 'animeonline':
        _addon.add_directory({'mode': 'SubSubMenu', 'site': site, 'section': 'animeonline'}, {'title': "Odcinki Anime"}, is_folder=True, fanart=fanartAol, img=iconOdcinki)
#        _addon.add_directory({'mode': 'SubSubMenu', 'site': site, 'section': 'animedrama'}, {'title': "Drama Anime"}, is_folder=True, fanart=fanartAol, img=iconOdcinki)
        _addon.add_directory({'mode': 'recenzje', 'site': site, 'section': section, 'url': ''}, {'title': "Recenzje Spycha"}, is_folder=True, fanart=fanartAol, img=iconspychu)
    set_view('list', view_mode=addst('default-view'))
    eod()


def SectionMenu():
###Anime4fun###
        if __settings__.getSetting("Anime4fun") == "true":
            _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'anime4fun'}, {'title': cFL('Animeonline EN', 'blue')}, is_folder=True, fanart=fanartAnime4fun, img=iconAnime4fun)
###Animejoy###
        if __settings__.getSetting("Animejoy") == "true":
            _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'animejoy'}, {'title': cFL('Anime-joy EN', 'blue')}, is_folder=True, fanart=fanartAnime4fun, img=iconAnimejoy)
###Anime-Online###
        if __settings__.getSetting("AnimeOnline") == "true":
            _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'animeonline'}, {'title': cFL('Anime-Odcinki PL', 'blue')}, is_folder=True, fanart=fanartAol, img=iconOdcinki)
###Ulubione###
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': ''}, {'title': (lang(30001).encode('utf-8') + addst('fav.tv.1.name'))}, fanart=fanartIPTV, img=iconFavs)
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': '', 'subfav': '2'}, {'title': (lang(30001).encode('utf-8') + addst('fav.tv.2.name'))}, fanart=fanartIPTV, img=iconFavs)
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': '', 'subfav': '3'}, {'title': (lang(30001).encode('utf-8') + addst('fav.tv.3.name'))}, fanart=fanartIPTV, img=iconFavs)
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': '', 'subfav': '4'}, {'title': (lang(30001).encode('utf-8') + addst('fav.tv.4.name'))}, fanart=fanartIPTV, img=iconFavs)
        set_view('list', view_mode=addst('default-view'))
        eod()


##############################################################################
def mode_subcheck(mode='', site='', section='', url=''):
    if (mode == 'SectionMenu'):
        SectionMenu()
    elif (mode == '') or (mode == 'main') or (mode == 'MainMenu'):
        SectionMenu()
    elif (mode == 'SubMenu'):
        SubMenu()
    elif (mode == 'SubSubMenu'):
        SubSubMenu()
# ANIME4FUN
    elif (mode == 'Page4fun'):
        Anime4fun(mode=mode, url=url, page=page)
    elif (mode == 'Episodes4fun'):
        Anime4fun(mode, url, page)
    elif (mode == 'PlayAnime4fun'):
        Anime4fun(mode, url, page)
# ANIME-ONLINE
    elif (mode == 'Pageanimeonline'):
        AnimeOnline(mode=mode, url=url, page=page)
    elif (mode == 'EpisodesAnime'):
        AnimeOnline(mode, url, page)
    elif (mode == 'PlayAnime'):
        AnimeOnline(mode, url, page)
    elif (mode == 'recenzje'):
        AnimeOnline(mode, url=url, page=page)
# ANIME-JOY
    elif (mode == 'Pagejoy'):
        Animejoy(mode=mode, url=url, page=page)
    elif (mode == 'Episodesjoy'):
        Animejoy(mode, url, page)
    elif (mode == 'PlayAnimejoy'):
        Animejoy(mode, url, page)
# PLAY FROM HOST
    elif (mode == 'PlayFromHost'):
        PlayFromHost(url)
# ULUBIONE
    elif (mode == 'FavoritesList'):
        Fav_List(site=site, section=section, subfav=addpr('subfav', ''))
    elif (mode == 'cFavoritesEmpty'):
        fav__COMMON__empty(site=site, section=section, subfav=addpr('subfav', '') ); xbmc.executebuiltin("XBMC.Container.Refresh");
    elif (mode == 'cFavoritesRemove'):
        fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
    elif (mode == 'cFavoritesAdd'):
        fav__COMMON__add(site=site, section=section, subfav=addpr('subfav', ''), name=addpr('title', ''), year=addpr('year', ''), img=addpr('img', ''), fanart=addpr('fanart', ''), plot=addpr('plot', ''), commonID=addpr('commonID', ''), commonID2=addpr('commonID2', ''), ToDoParams=addpr('todoparams', ''), Country=addpr('country', ''), Genres=addpr('genres', ''), Url=url)
    elif (mode == 'addView'):
        from common import addView
        addView('movies')
    elif (mode == 'delete_table'):
        from scraper import delete_table
        delete_table()
mode_subcheck(addpr('mode', ''), addpr('site', ''), addpr('section', ''), addpr('url', ''))
##############################################################################

