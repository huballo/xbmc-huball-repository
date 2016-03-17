# -*- coding: utf-8 -*-

### Imports ###
import os
import re
import sys
import xbmc
import xbmcaddon

from addon.common.addon import Addon  # może trzeba więcej
#######
__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
sys.path.append(os.path.join(addonPath, 'resources/libs'))
from favourites import (fav__COMMON__check)
##########
_addon = Addon('plugin.video.anime-iptv', sys.argv)
###########


def addpr(r, s=''):
    return _addon.queries.get(r, s)


def addst(r, s=''):
    return _addon.get_setting(r)


def tfalse(r, d=False):
    if   (r.lower() == 'true') or (r.lower() == 't') or (r.lower() == 'y') or (r.lower() == '1') or (r.lower() == 'yes'):
        return True
    elif (r.lower() == 'false') or (r.lower() == 'f') or (r.lower() == 'n') or (r.lower() == '0') or (r.lower() == 'no'):
        return False
    else:
        return d


def DoLabs2LB(labs, subfav=''):
    LB = {}
    n = 'title'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'year'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'img'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'fanart'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'plot'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'url'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'country'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'genres'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'todoparams'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'commonid'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'commonid2'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'plot'
    try:
        LB[n] = str(labs[n])
    except:
        LB[n] = ''
    n = 'site'
    try:
        LB[n] = labs[n]
    except:
        try:
            LB[n] = addpr(n, '')
        except:
            LB[n] = ''
    n = 'section'
    try:
        LB[n] = labs[n]
    except:
        try:
            LB[n] = addpr(n, '')
        except:
            LB[n] = ''
    return LB


def filename_filter_out_year(name=''):
    years = re.compile(' \((\d+)\)').findall('__' + name + '__')
    for year in years:
        name = name.replace(' (' + year + ')', '')
    name = name.strip()
    return name


def ContextMenu_Movies(labs={}):
    contextMenuItems = []
    nameonly = filename_filter_out_year(labs['title'])
    try:
        site = labs['site']
    except:
        site = addpr('site', '')
    try:
        section = labs['section']
    except:
        section = addpr('section', '')
    if tfalse(addst("CMI_ShowInfo")) == True:
        contextMenuItems.append(('Movie Info', 'XBMC.Action(Info)'))
    if labs == {}:
        return contextMenuItems
    if (tfalse(addst("CMI_SearchKissAnime")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.kissanime')):
        contextMenuItems.append(('Search KissAnime', 'XBMC.Container.Update(%s?mode=%s&pageno=1&pagecount=1&title=%s)' % ('plugin://plugin.video.kissanime/', 'Search', nameonly)))
    if (tfalse(addst("CMI_SearchSolarMovieso")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.solarmovie.so')):
        contextMenuItems.append(('Search Solarmovie.so', 'XBMC.Container.Update(%s?mode=%s&section=%s&title=%s)' % ('plugin://plugin.video.solarmovie.so/', 'Search', 'movies', nameonly)))
    if (tfalse(addst("CMI_Search1Channel")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.1channel')):
        contextMenuItems.append(('Search 1Channel', 'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)' % ('plugin://plugin.video.1channel/', 'movies', nameonly)))
    try:
        WRFC = 'Ulubione: '
        LB = DoLabs2LB(labs)
        LB['mode'] = 'cFavoritesAdd'
        P1 = 'XBMC.RunPlugin(%s)'
        LB['subfav'] = ''
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((WRFC + addst('fav.movies.1.name'), Pars))
        LB['subfav'] = '2'
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((WRFC + addst('fav.movies.2.name'), Pars))
        LB['subfav'] = '3'
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((WRFC + addst('fav.movies.3.name'), Pars))
        LB['subfav'] = '4'
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((WRFC + addst('fav.movies.4.name'), Pars))
        LB['subfav'] = '5'
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((WRFC + addst('fav.movies.5.name'), Pars))
        LB['subfav'] = '6'
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((WRFC + addst('fav.movies.6.name'), Pars))
        LB['subfav'] = '7'
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((WRFC + addst('fav.movies.7.name'), Pars))
    except:
        pass


def ContextMenu_Series(labs={}):
    contextMenuItems = []
    nameonly = filename_filter_out_year(labs['title'])
    try:
        site = labs['site']
    except:
        site = addpr('site','')
    try:
        section = labs['section']
    except:
        section = addpr('section', '')
    if tfalse(addst("CMI_ShowInfo")) == True:
        contextMenuItems.append(('Show Info', 'XBMC.Action(Info)'))
    if labs == {}:
        return contextMenuItems
#    if (tfalse(addst("CMI_FindAirDates")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.solarmovie.so')):
#        contextMenuItems.append(('Find AirDates', 'XBMC.Container.Update(%s?mode=%s&title=%s)' % ('plugin://plugin.video.solarmovie.so/', 'SearchForAirDates', labs['title'])))
#    if (tfalse(addst("CMI_SearchKissAnime")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.kissanime')):
#        contextMenuItems.append(('Search KissAnime', 'XBMC.Container.Update(%s?mode=%s&pageno=1&pagecount=1&title=%s)' % ('plugin://plugin.video.kissanime/', 'Search', nameonly)))
#    if (tfalse(addst("CMI_SearchSolarMovieso")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.solarmovie.so')):
#        contextMenuItems.append(('Search Solarmovie.so', 'XBMC.Container.Update(%s?mode=%s&section=%s&title=%s)' % ('plugin://plugin.video.solarmovie.so/', 'Search', 'tv', nameonly)))
#    if (tfalse(addst("CMI_Search1Channel")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.1channel')):
#        contextMenuItems.append(('Search 1Channel', 'XBMC.Container.Update(%s?mode=7000&section=%s&query=%s)' % ('plugin://plugin.video.1channel/', 'tv', nameonly)))
#    if (tfalse(addst("CMI_SearchMerDBru")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.merdb')):
#        contextMenuItems.append(('Search MerDB', 'XBMC.Container.Update(%s?mode=%s&section=%s&url=%s&title=%s)' % ('plugin://plugin.video.merdb/', 'Search', 'tvshows', urllib.quote_plus('http://merdb.ru/tvshow/'), nameonly)))
#    if (tfalse(addst("CMI_SearchIceFilms")) == True) and (os.path.exists(xbmc.translatePath("special://home/addons/") + 'plugin.video.icefilms')):
#       contextMenuItems.append(('Search Icefilms', 'XBMC.Container.Update(%s?mode=555&url=%s&search=%s&nextPage=%s)' % ('plugin://plugin.video.icefilms/', 'http://www.icefilms.info/', labs['title'], '1')))
    try:
        WRFC = 'Ulubione: '
        WRFCr = 'Remove: '
        LB = DoLabs2LB(labs)
        McFA = 'cFavoritesAdd'
        McFR = 'cFavoritesRemove'
        LB['mode'] = McFA
        P1 = 'XBMC.RunPlugin(%s)'
        LB['subfav'] = '1'
        if fav__COMMON__check(LB['site'], LB['section'], LB['title'], LB['year'], LB['subfav']) == True:
            LB['mode'] = McFR
            LabelName = WRFCr + WRFC + addst('fav.tv.' + LB['subfav'] + '.name')
        else:
            LB['mode'] = McFA
            LabelName = WRFC + addst('fav.tv.' + LB['subfav'] + '.name')
        LB['subfav'] = ''
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append((LabelName, Pars))
        for nn in ['2', '3', '4']:
            LB['subfav'] = nn
            if fav__COMMON__check(LB['site'], LB['section'], LB['title'], LB['year'], LB['subfav']) == True:
                LB['mode'] = McFR
                LabelName = WRFCr + WRFC + addst('fav.tv.' + LB['subfav'] + '.name')
            else:
                LB['mode'] = McFA
            LabelName = WRFC + addst('fav.tv.' + LB['subfav'] + '.name')
            Pars = P1 % _addon.build_plugin_url(LB)
            contextMenuItems.append((LabelName, Pars))
        #LB['mode']=McFA; LB['subfav']='2'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.2.name'),Pars))
        #LB['mode']=McFA; LB['subfav']='3'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.3.name'),Pars))
        #LB['mode']=McFA; LB['subfav']='4'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.4.name'),Pars))
        #LB['mode']=McFA; LB['subfav']='5'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.5.name'),Pars))
        #LB['mode']=McFA; LB['subfav']='7'; Pars=P1 % _addon.build_plugin_url(LB); contextMenuItems.append((WRFC+addst('fav.tv.7.name'),Pars))
#        LB['mode'] = 'setView'
#        Pars2 = P1 % _addon.build_plugin_url(LB)
#        contextMenuItems.append(('gggggg',Pars2))

#        if (tfalse(addst("CMI_RefreshMetaData", "true")) == True):
#            LB['mode'] = 'refresh_meta'
#            LabelName = 'Refresh MetaData'
#            LB['imdb_id'] = LB['commonid']
#            LB['alt_id'] = 'imdbnum'
#            LB['video_type'] = 'tvshow'
#            LB['year']
#            Pars = P1 % _addon.build_plugin_url(LB)
#            contextMenuItems.append((LabelName, Pars))
    except:
        pass
    return contextMenuItems


def ContextMenu_Episodes(labs={}):
    contextMenuItems = []
    if tfalse(addst("CMI_ShowInfo")) == True:
        contextMenuItems.append(('Episode Info', 'XBMC.Action(Info)'))
    contextMenuItems.append(('Watched/Unwatched', 'XBMC.Action(ToggleWatched)'))
    if labs == {}:
        return contextMenuItems
    return contextMenuItems


def ContextMenu_Favorites(labs={}):
    contextMenuItems = []
    nameonly = filename_filter_out_year(labs['title'])
    try:
        site = labs['site']
    except:
        site = addpr('site', '')
    try:
        section = labs['section']
    except:
        section = addpr('section', '')
    try:
        _subfav = addpr('subfav', '')
    except:
        _subfav = ''
    if tfalse(addst("CMI_ShowInfo")) == True:
        contextMenuItems.append(('Info', 'XBMC.Action(Info)'))
    if labs == {}:
        return contextMenuItems
    try:
        if _subfav == '':
            _sf = '1'
        else:
            _sf = _subfav
        WRFC = 'Ulubione: '
        LB = DoLabs2LB(labs)
        LB['mode'] = 'cFavoritesAdd'
        P1 = 'XBMC.RunPlugin(%s)'
        if _sf is not '1':
            LB['subfav'] = ''
            Pars = P1 % _addon.build_plugin_url(LB)
            contextMenuItems.append((WRFC + addst('fav.tv.1.name'), Pars))
        if _sf is not '2':
            LB['subfav'] = '2'
            Pars = P1 % _addon.build_plugin_url(LB)
            contextMenuItems.append((WRFC + addst('fav.tv.2.name'), Pars))
        if _sf is not '3':
            LB['subfav'] = '3'
            Pars = P1 % _addon.build_plugin_url(LB)
            contextMenuItems.append((WRFC + addst('fav.tv.3.name'), Pars))
        if _sf is not '4':
            LB['subfav'] = '4'
            Pars = P1 % _addon.build_plugin_url(LB)
            contextMenuItems.append((WRFC + addst('fav.tv.4.name'), Pars))
#        if _sf is not '5':
#            LB['subfav'] = '5'
#            Pars = P1 % _addon.build_plugin_url(LB)
#            contextMenuItems.append((WRFC + addst('fav.tv.5.name'), Pars))
#        if _sf is not '6':
#            LB['subfav'] = '6'
#            Pars = P1 % _addon.build_plugin_url(LB)
#            contextMenuItems.append((WRFC + addst('fav.tv.6.name'), Pars))
#        if _sf is not '7':
#            LB['subfav'] = '7'
#            Pars = P1 % _addon.build_plugin_url(LB)
#            contextMenuItems.append((WRFC + addst('fav.tv.7.name'), Pars))
        LB['mode'] = 'cFavoritesRemove'
        LB['subfav'] = _subfav
        Pars = P1 % _addon.build_plugin_url(LB)
        contextMenuItems.append(('Remove: ' + WRFC + addst('fav.tv.' + _sf + '.name'), Pars))
    except:
        pass
    return contextMenuItems