# -*- coding: utf-8 -*-

### Imports ###
import xbmc
import xbmcaddon
import os
import sys
import xbmcgui

# logowanie
import weblogin

### ##########################################################################
### ##########################################################################
SiteName = 'AnimeIPTV'
SiteTag = 'AnimeIPTV'
mainSite = 'http://diff-anime.pl/'
mainSite2 = 'http://anime-centrum.net/'
mainSite3 = 'http://www.dramaqueen.pl/'
mainSite4 = 'http://anime-odcinki.pl/'
mainSite5 = 'http://shinden.pl/'
mainSite6 = 'http://animeon.pl/'

__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'hosts'))
from config import ps
from common import (_addon, addpr, eod, set_view, addst, cFL_, cFL, fav__COMMON__list_fetcher, myNote, ContextMenu_Favorites, PlayFromHost, fav__COMMON__add, fav__COMMON__remove)

iconSite = addonPath + '/art/icon.png'
iconCentrum = addonPath + '/art/japan/animecentrum.jpg'
iconDiff = addonPath + '/art/japan/diffanime.jpg'
iconOdcinki = addonPath + '/art/japan/animeodcinki.jpg'
iconShniden = addonPath + '/art/japan/animeshniden.jpg'
iconAnimeon = addonPath + '/art/japan/animeon.jpg'
iconFavs = addonPath + '/art/japan/ulubione.jpg'
fanartSite = addonPath + '/art/japan/fanart.jpg'
fanartIPTV = addonPath + '/art/japan/fanart.jpg'
fanartSiteCentrum = addonPath + '/art/japan/fanart.jpg'
fanartDrama = addonPath + '/art/japan/fanart.jpg'
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
AonlineAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '3', '5']
AonlineDrama = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
AnimeonAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

MyBrowser = ['User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']

###############################################################################
site = addpr('site', '')
section = addpr('section', '')
url = addpr('url', '')
nmr = addpr('nmr', '')
sections = {'diffanime': 'diffanime', 'animecentrum': "animecentrum", 'DramaQueen': 'DramaQueen', 'Dramadrama': 'Dramadrama', 'Dramamovie': 'Dramamovie','animeonline': 'animeonline','animeodc': 'animeodc', 'aktualnosci': "aktualnosci", 'movies': 'movies', 'animeshinden': 'animeshinden', 'shnidenodc': 'shnidenodc', 'shnidengat': 'shnidengat', 'animeon': 'animeon'}
thumbnail = addpr('img', '')
fanart = addpr('fanart', '')
page = addpr('page', '')


###############################################################################
###############################################################################
# Anime-Centrum
###############################################################################
###############################################################################
def Browse_PageCentrum(url, page='', metamethod=''):
    from hostanimecentrum import PageCentrum
    PageCentrum(url)


def Browse_EpisodesCentrum(url, page):
    from hostanimecentrum import Browse_EpisodesCentrum
    Browse_EpisodesCentrum(url, page)


###############################################################################
###############################################################################
# Diff-anime
###############################################################################
###############################################################################
def Browse_PageDiff(url, page='', metamethod=''):
    from hostdiffanime import PageDiff
    PageDiff(url)


def Browse_EpisodesDiff(url, page):
    from hostdiffanime import Browse_EpisodesDiff
    Browse_EpisodesDiff(url, page)


def Browse_PageDiffAKT(url, page):
    from hostdiffanime import Browse_PageDiffAKT
    Browse_PageDiffAKT(url, page)


###############################################################################
###############################################################################
#DramaQueen
###############################################################################
###############################################################################
def Browse_PageDramaQueen_drama(url, page='', metamethod=''):
    from hostdramaqueen import PageDramaQueen_drama
    PageDramaQueen_drama(url)


###############################################################################
###############################################################################
# Anime-Online
###############################################################################
###############################################################################
def Browse_Pageanimeonline(url, page='', metamethod=''):
    from hostanimeonline import Pageanimeonline
    Pageanimeonline(url)


def Browse_EpisodesAnime(url, page):
    from hostanimeonline import Browse_EpisodesAnime
    Browse_EpisodesAnime(url, page)


def Browse_PlayAnime(url, page):
    from hostanimeonline import Browse_PlayAnime
    Browse_PlayAnime(url, page)


def Browse_Recenzje(url, page='', metamethod=''):
    from hostanimeonline import Recenzje
    Recenzje(url)
###############################################################################
###############################################################################
# Anime-Shinden
###############################################################################
###############################################################################
def Browse_Pageshniden(url, nmr, page='', metamethod=''):
    from hostanimeshniden import Pageshniden
    Pageshniden(url, nmr)


def Browse_GenreShniden(url):
    from hostanimeshniden import Browse_GenreShniden
    Browse_GenreShniden(url, page)


def Browse_EpisodesShniden(url, page):
    from hostanimeshniden import Browse_EpisodesShniden
    Browse_EpisodesShniden(url, page)


def Browse_PlayShniden(url, page):
    from hostanimeshniden import Browse_PlayShniden
    Browse_PlayShniden(url, page)

def Browse_PlayShniden2(url, page):
    from hostanimeshniden import Browse_PlayShniden2
    Browse_PlayShniden2(url, page)
###############################################################################
###############################################################################
# Anime-On
###############################################################################
###############################################################################
def Browse_Pageanimeon(url, page='', metamethod=''):
    from hostanimeon import Pageanimeon
    Pageanimeon(url,nmr)


def Browse_EpisodesAnimeon(url, page):
    from hostanimeon import Browse_EpisodesAnimeon
    Browse_EpisodesAnimeon(url, page)


def Browse_Version(url, page):
    from hostanimeon import Browse_Version
    Browse_Version(url, page)
###############################################################################


#  ulubione
def Fav_List(site='', section='', subfav=''):
    favs = fav__COMMON__list_fetcher(site=site, section='diffanime', subfav=subfav)
    favs2 = fav__COMMON__list_fetcher(site=site, section='animecentrum', subfav=subfav)
    favs3 = fav__COMMON__list_fetcher(site=site, section='animeon', subfav=subfav)
    favs4 = fav__COMMON__list_fetcher(site=site, section='animeonline', subfav=subfav)
    favs5 = fav__COMMON__list_fetcher(site=site, section='animedrama', subfav=subfav)
    favs6 = fav__COMMON__list_fetcher(site=site, section='shnidenodc', subfav=subfav)
    ItemCount = len(favs) and len(favs2) and len(favs3) and len(favs4) and len(favs5) and len(favs6)
    if len(favs) == 0 and len(favs2) == 0 and len(favs3) == 0 and len(favs4) == 0 and len(favs5) == 0and len(favs6) == 0:
        myNote('Favorites', 'None Found')
        eod()
        return
    if len(favs) == 0:
            favs = []
    if len(favs) > 0:
            logged_inDiff = weblogin.doLogin(addonPath, login, password)
    if len(favs2) == 0:
            favs2 = []
    if len(favs3) == 0:
            favs3 = []
    if len(favs4) == 0:
            favs4 = []
    if len(favs5) == 0:
            favs5 = []
    if len(favs6) == 0:
            favs6 = []
    favs += favs2
    favs += favs3
    favs += favs4
    favs += favs5
    favs += favs6
    for (_name, _year, _img, _fanart, _Country, _Url, _plot, _Genres, _site, _subfav, _section, _ToDoParams, _commonID, _commonID2) in favs:
        if _img > 0:
            img = _img
        else:
            img = iconSite
        if _fanart > 0:
            fimg = _fanart
        else:
            fimg = fanartSite
        pars = _addon.parse_query(_ToDoParams)
        _section
        _title = _name
        if _section == 'diffanime':
            host = cFL(' (D-A)', 'blueviolet')
            _title = _title + host
        if _section == 'animecentrum':
            host = cFL(' (A-C)', 'blue')
            _title = _title + host
        if _section == 'animeon':
            host = cFL(' (A-ON)', 'lime')
            _title = _title + host
        if _section == 'animeonline':
            host = cFL(' (A-O)', 'orange')
            _title = _title + host
        if _section == 'animedrama':
            host = cFL(' (A-D)', 'red')
            _title = _title + host
        if _section == 'shnidenodc':
            host = cFL(' (A-S)', 'yellow')
            _title = _title + host
        if (len(_year) > 0) and (not _year == '0000'):
            _title += cFL('  (' + cFL(_year, 'deeppink') + ')', 'pink')
        if len(_Country) > 0:
            _title += cFL('  [' + cFL(_Country, 'deeppink') + ']', 'pink')
        contextLabs = {'title': _name, 'year': _year, 'img': _img, 'fanart': _fanart, 'country': _Country, 'url': _Url, 'plot': _plot, 'genres': _Genres, 'site': _site, 'subfav': _subfav, 'section': _section, 'todoparams': _ToDoParams, 'commonid': _commonID, 'commonid2': _commonID2}
        contextMenuItems = ContextMenu_Favorites(contextLabs)
        _addon.add_directory(pars, {'title': _title, 'plot': _plot}, is_folder=True, fanart=fimg, img=img, total_items=ItemCount, contextmenu_items=contextMenuItems)
    if 'movie' in section.lower():
        content = 'movies'
    else:
        content = 'tvshows'
    set_view(content, view_mode=int(addst('tvshows-view')))
    eod()


#  lista ABC
def Browse_AZ():
###Diff-Anime###
    if section == 'diffanime':
        tUrl = mainSite + 'lista-anime'
        _addon.add_directory({'mode': 'Page', 'site': site, 'section': section, 'url': tUrl + '?letter=0&rowstart=00'}, {'title': '#'}, is_folder=True, fanart=fanartSite, img=addonPath + '/art/znak.png')
        for az in MyAlphabet:
            _addon.add_directory({'mode': 'Page', 'site': site, 'section': section, 'url': tUrl + '?letter='+ az + '&rowstart=00' }, {'title': az}, is_folder=True, fanart=fanartSite, img=addonPath + '/art/'+ az +'.png')
        if (len(addst('username' '')) == 0) or (len(addst('password', '')) == 0):
            d = xbmcgui.Dialog()
            d.ok('Komunikat', "Musisz się zalogować, aby móc oglądać odcinki.")
    set_view('list', view_mode=addst('default-view'))
    eod()


def SubSubMenu():
###DramaQueen###
    if section == 'Dramadrama':
        _addon.add_directory({'mode': 'dramaqueen_drama', 'site': site, 'section': section, 'url': mainSite3 + 'drama/japonskie/'}, {'title': "Japońskie"}, is_folder=True, fanart=fanartDrama, img=iconSite)
        _addon.add_directory({'mode': 'dramaqueen_drama', 'site': site, 'section': section, 'url': mainSite3 + 'drama/koreanska/'}, {'title': "Koreańskie"}, is_folder=True, fanart=fanartDrama, img=iconSite)
        _addon.add_directory({'mode': 'dramaqueen_drama', 'site': site, 'section': section, 'url': mainSite3 + '/drama/tajwanska/'}, {'title': "Tajwańskie"}, is_folder=True, fanart=fanartDrama, img=iconSite)
    if section == 'Dramamovie':
        _addon.add_directory({'mode': 'dramaqueen_drama_movie', 'site': site, 'section': section, 'url': mainSite3 + 'drama/film/japonski/'}, {'title': "Film - japoński"}, is_folder=True, fanart=fanartDrama, img=iconSite)
        _addon.add_directory({'mode': 'dramaqueen_drama_movie', 'site': site, 'section': section, 'url': mainSite3 + 'drama/film/koreanski/'}, {'title': "Film - koreański"}, is_folder=True, fanart=fanartDrama, img=iconSite)
###Anime-Online###
    if section == 'animeonline':
        tUrl = mainSite4 + 'lista-anime/'
        for az, xy in zip(AonlineAlphabet, AonlineAlphabet):
            _addon.add_directory({'mode': 'Pageanimeonline', 'site': site, 'section': section, 'url': tUrl + xy}, {'title': az}, is_folder=True, fanart=fanartAol, img=addonPath + '/art/'+ az +'.png')
    if section == 'animedrama':
        tUrl = mainSite4 + 'Drama/viewpage.php?page_id='
        for az, xy in zip(MyAlphabet, AonlineDrama):
            _addon.add_directory({'mode': 'Pageanimeonline', 'site': site, 'section': section, 'url': tUrl + xy}, {'title': az}, is_folder=True, fanart=fanartAol, img=addonPath + '/art/'+ az +'.png')
###Anime-Shniden###
    if section == 'shnidenodc':
        tUrl = mainSite5 + 'anime?letter='
        _addon.add_directory({'mode': 'Pageshniden', 'site': site, 'section': section, 'url': tUrl + '0'}, {'title': '#'}, is_folder=True, fanart=fanartSite, img=addonPath + '/art/znak.png')
        for az in MyAlphabet:
            _addon.add_directory({'mode': 'Pageshniden', 'site': site, 'section': section, 'url': tUrl + az + "&page=",'nmr':'1'}, {'title': az}, is_folder=True, fanart=fanartSite, img=addonPath + '/art/'+ az +'.png')
    set_view('list', view_mode=addst('default-view'))
    eod()

def SubMenu():
###Anime-Centrum###
    if section == 'animecentrum':
        tUrl = mainSite2 + 'anime-online/'
        _addon.add_directory({'mode': 'PageCentrum', 'site': site, 'section': section, 'url': tUrl + 'others'}, {'title': '#'}, is_folder=True, fanart=fanartSiteCentrum, img=addonPath + '/art/znak.png')
        for az in MyAlphabet:
            _addon.add_directory({'mode': 'PageCentrum', 'site': site, 'section': section, 'url': tUrl + az + '.html'}, {'title': az}, is_folder=True, fanart=fanartSiteCentrum, img=addonPath + '/art/'+ az +'.png')
###Diff-Anime###
    if section == 'diffanime':
        _addon.add_directory({'mode': 'AZ', 'site': site, 'section': section}, {'title': "Lista anime A-Z."}, is_folder=True, fanart=fanartSite, img=iconDiff)
        _addon.add_directory({'mode': 'aktualnosci', 'site': site, 'section': section, 'url': 'http://diff-anime.pl/newsy'}, {'title': "Aktualności"}, is_folder=True, fanart=fanartSiteCentrum, img=iconDiff)
###DramaQueen###
    if section == 'DramaQueen':
        _addon.add_directory({'mode': 'SubSubMenu', 'site': site, 'section': 'Dramadrama', 'url': mainSite3 + 'drama/'}, {'title': "Drama"}, is_folder=True, fanart=fanartDrama, img=iconSite)
        _addon.add_directory({'mode': 'SubSubMenu', 'site': site, 'section': 'Dramamovie'}, {'title': 'Film'}, is_folder=True, fanart=fanartDrama, img=iconSite)
###Anime-Online###
    if section == 'animeonline':
        _addon.add_directory({'mode': 'SubSubMenu', 'site': site, 'section': 'animeonline'}, {'title': "Odcinki Anime"}, is_folder=True, fanart=fanartAol, img=iconOdcinki)
        _addon.add_directory({'mode': 'SubSubMenu', 'site': site, 'section': 'animedrama'}, {'title': "Drama Anime"}, is_folder=True, fanart=fanartAol, img=iconOdcinki)
        _addon.add_directory({'mode': 'recenzje', 'site': site, 'section': section, 'url': 'https://www.youtube.com/user/Spychu91/videos?sort=dd&shelf_id=0&view=0'}, {'title': "Recenzje Spycha"}, is_folder=True, fanart=fanartAol, img=iconspychu)
###Anime-Shinden###
    if section == 'animeshinden':
        _addon.add_directory({'mode': 'SubSubMenu', 'site': site, 'section': 'shnidenodc'}, {'title': "Alfabetycznie."}, is_folder=True, fanart=fanartAol, img=iconShniden)
        url = mainSite5 + 'animelist/index.php'
        _addon.add_directory({'mode': 'Browse_GenreShniden', 'site': site, 'section': 'shnidengat', 'url': url }, {'title': "Lista wg gatunku."}, is_folder=True, fanart=fanartAol, img=iconShniden)
###Anime-On###
    if section == 'animeon':
        tUrl = mainSite6 + 'anime.php?letter='
        for az in AnimeonAlphabet:
            _addon.add_directory({'mode': 'Pageanimeon', 'site': site, 'section': section, 'url': tUrl + az + '&rowstart=00'}, {'title': az}, is_folder=True, fanart=fanartSiteCentrum, img=addonPath + '/art/'+ az +'.png')
    set_view('list', view_mode=addst('default-view'))
    eod()


def SectionMenu():
###Anime-Centrum###
        _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'animecentrum'}, {'title': cFL('Anime-Centrum', 'blue')}, is_folder=True, fanart=fanartSiteCentrum, img=iconCentrum)
###Diff-Anime###
#        _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'diffanime'}, {'title': cFL('Diff-Anime', 'blue')}, is_folder=True, fanart=fanartSite, img=iconDiff)
###DramaQueen###
#        _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'DramaQueen'}, {'title': cFL('DramaQueen', 'blue')}, is_folder=True, fanart=fanartDrama, img=iconSite)
###Anime-Online###
        _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'animeonline'}, {'title': cFL('Anime-Odcinki', 'blue')}, is_folder=True, fanart=fanartAol, img=iconOdcinki)
###Anime-Shinden###
        _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'animeshinden'}, {'title': cFL('Anime-Shinden', 'blue')}, is_folder=True, fanart=fanartAol, img=iconShniden)
###Anime-On###
        _addon.add_directory({'mode': 'SubMenu', 'site': site, 'section': 'animeon'}, {'title': cFL('Anime-On', 'blue')}, is_folder=True, fanart=fanartAol, img=iconAnimeon)
###Ulubione###
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': ''}, {'title': cFL_(ps('WhatRFavsCalled') + addst('fav.tv.1.name'), ps('cFL_color3'))}, fanart=fanartIPTV, img=iconFavs)
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': '', 'subfav': '2'}, {'title': cFL_(ps('WhatRFavsCalled') + addst('fav.tv.2.name'), ps('cFL_color3'))}, fanart=fanartIPTV, img=iconFavs)
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': '', 'subfav': '3'}, {'title': cFL_(ps('WhatRFavsCalled') + addst('fav.tv.3.name'), ps('cFL_color3'))}, fanart=fanartIPTV, img=iconFavs)
        _addon.add_directory({'mode': 'FavoritesList', 'site': site, 'section': '', 'subfav': '4'}, {'title': cFL_(ps('WhatRFavsCalled') + addst('fav.tv.4.name'), ps('cFL_color3'))}, fanart=fanartIPTV, img=iconFavs)
        set_view('list', view_mode=addst('default-view'))
        eod()


### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
    if (mode=='SectionMenu'):         SectionMenu()
    elif (mode=='') or (mode=='main') or (mode=='MainMenu'): SectionMenu()
    elif (mode=='SubMenu'):             SubMenu()
    elif (mode=='SubSubMenu'):             SubSubMenu()
    elif (mode=='AZ'):                         Browse_AZ()
# ANIME-CENTRUM
    elif (mode=='PageCentrum'):                     Browse_PageCentrum(url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
    elif (mode=='EpisodesCentrum'):             Browse_EpisodesCentrum(url,page)
# DIFF-ANIME
    elif (mode=='Page'):                     Browse_PageDiff(url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
    elif (mode=='EpisodesDiff'):             Browse_EpisodesDiff(url,page)
    elif (mode=='aktualnosci'):             Browse_PageDiffAKT(url,page)
    elif (mode=='nextpage'):             Browse_EpisodesDiff(url,page)
# ANIME-ONLINE
    elif (mode=='Pageanimeonline'):                     Browse_Pageanimeonline(url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
    elif (mode=='EpisodesAnime'):             Browse_EpisodesAnime(url,page)
    elif (mode=='PlayAnime'):             Browse_PlayAnime(url,page)
    elif (mode=='recenzje'):                     Browse_Recenzje(url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
# ANIME-SHNIDEN
    elif (mode=='Pageshniden'):                     Browse_Pageshniden(url=url,nmr=nmr,page=page,metamethod=addpr('metamethod','')) #(site,section)
    elif (mode=='EpisodesShniden'):             Browse_EpisodesShniden(url,page)
    elif (mode=='Browse_GenreShniden'):             Browse_GenreShniden(url)
    elif (mode=='PlayShniden'):             Browse_PlayShniden(url,page)
    elif (mode=='PlayShniden2'):             Browse_PlayShniden2(url,page)
# DRAMA-QUEEN
    elif (mode=='EpisodesDramaQueen_drama'):             Browse_EpisodesDramaQueen_drama(url,page)
    elif (mode=='dramaqueen_drama'):             Browse_PageDramaQueen_drama(url,page)
    elif (mode=='dramaqueen_drama_movie'):             Browse_PageDramaQueen_dramamovie(url,page)
# ANIME-ON
    elif (mode=='Pageanimeon'):                     Browse_Pageanimeon(url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
    elif (mode=='EpisodesAnimeon'):             Browse_EpisodesAnimeon(url,page)
    elif (mode=='Version'):             Browse_Version(url,page)
# PLAY FROM HOST
    elif (mode=='PlayFromHost'):     PlayFromHost(url)
# ULUBIONE
    elif (mode=='FavoritesList'): Fav_List(site=site,section=section,subfav=addpr('subfav',''))
    elif (mode=='cFavoritesEmpty'):      fav__COMMON__empty( site=site,section=section,subfav=addpr('subfav','') ); xbmc.executebuiltin("XBMC.Container.Refresh");
    elif (mode=='cFavoritesRemove'):  fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
    elif (mode=='cFavoritesAdd'):          fav__COMMON__add( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year',''),img=addpr('img',''),fanart=addpr('fanart',''),plot=addpr('plot',''),commonID=addpr('commonID',''),commonID2=addpr('commonID2',''),ToDoParams=addpr('todoparams',''),Country=addpr('country',''),Genres=addpr('genres',''),Url=url ) #,=addpr('',''),=addpr('','')



#    elif (mode=='ResolverSettings'):         import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
#    elif (mode=='AddVisit'):
#        try: visited_add(addpr('title')); RefreshList();
#        except: pass
#    elif (mode=='RemoveVisit'):
#        try: visited_remove(addpr('title')); RefreshList();
#        except: pass
#    elif (mode=='EmptyVisit'):
#        try: visited_empty(); RefreshList();
#        except: pass
#    elif (mode=='refresh_meta'):            refresh_meta(addpr('video_type',''),TagAnimeName(addpr('title','')),addpr('imdb_id',''),addpr('alt_id',''),addpr('year',''))
#    else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
#    #
mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
