# -*- coding: utf-8 -*-

### Imports ###
import re, os, sys, xbmc, xbmcplugin, xbmcgui, xbmcaddon
from addon.common.addon import Addon  # może trzeba więcej
import weblogingoogle
from addon.common.net import Net  # może trzeba więcej
try:
    import json
except:
    import simplejson as json
##########

__settings__ = xbmcaddon.Addon(id="plugin.video.anime-iptv")
addonPath = __settings__.getAddonInfo('path')
iconFav = xbmcaddon.Addon(id="plugin.video.anime-iptv").getAddonInfo('path') + '/art/favorites.png'
net = Net()
_addon = Addon('plugin.video.anime-iptv', sys.argv)
_artIcon = _addon.get_icon()
_artFanart = _addon.get_fanart()
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
sys.path.append(os.path.join(addonPath, 'resources/libs'))
from favourites import (fav__COMMON__check)


def byteify(input):
    if isinstance(input, dict):
        return dict([(byteify(key), byteify(value)) for key, value in input.iteritems()])
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def addst(r, s=''):
    return _addon.get_setting(r)

loginGoogle = addst('username3', '')
passwordGoogle = addst('password3', '')


def iFL(t):
    return '[I]' + t + '[/I]'  # For Italic Text ###


def bFL(t):
    return '[B]' + t +'[/B]'  # For Bold Text ###


def cFL(t, c='cornflowerblue'):
    return '[COLOR ' + c + ']' + t + '[/COLOR]'  # For Coloring Text ###


def cFL_(t, c='cornflowerblue'):
    return '[COLOR ' + c + ']' + t[0:1] + '[/COLOR]' + t[1:]  # For Coloring Text (First Letter-Only) ###


def set_view(content='none', view_mode=50, do_sort=False):
    h = int(sys.argv[1])
    if (content is not 'none'):
        xbmcplugin.setContent(h, content)
    if (tfalse(addst("auto-view")) == True):
        xbmc.executebuiltin("Container.SetViewMode(%s)" % str(view_mode))


def myNote(header='', msg='', delay=5000, image=iconFav):
    _addon.show_small_popup(title=header, msg=msg, delay=delay, image=image)


def eod():
    _addon.end_of_directory()


def addpr(r, s=''):
    return _addon.queries.get(r, s)


def nURL(url, method='get', form_data={}, headers={}, html='', proxy='', User_Agent='', cookie_file='', load_cookie=False, save_cookie=False):
    if url == '':
        return ''
    dhtml = '' + html
    if len(User_Agent) > 0:
        net.set_user_agent(User_Agent)
    else:
        net.set_user_agent(user_agent)
    if len(proxy) > 9:
        net.set_proxy(proxy)
    if (len(cookie_file) > 0) and (load_cookie == True):
        net.set_cookies(cookie_file)
    if   method.lower() == 'get':
        try:
            html = net.http_GET(url, headers=headers).content
        except:
            html = dhtml
    elif method.lower() == 'post':
        try:
            html = net.http_POST(url, form_data=form_data, headers=headers).content
        except:
            html = dhtml
    elif method.lower() == 'head':
        try:
            html = net.http_HEAD(url, headers=headers).content
        except:
            html = dhtml
    if (len(html) > 0) and (len(cookie_file) > 0) and (save_cookie == True):
        net.save_cookies(cookie_file)
    return html


def filename_filter_out_year(name=''):
    years = re.compile(' \((\d+)\)').findall('__' + name + '__')
    for year in years:
        name = name.replace(' (' + year + ')', '')
    name = name.strip()
    return name


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

# tekstowe


def ParseDescription(plot):
    if ("&amp;" in plot):
        plot = plot.replace('&amp;', '&')
    if ("&nbsp;" in plot):
        plot = plot.replace('&nbsp;', '')
    if ('&#' in plot) and (';' in plot):
        if ("&#8211;" in plot):
            plot = plot.replace("&#8211;", "-")
        if ("&#8216;" in plot):
            plot = plot.replace("&#8216;", "'")
        if ("&#8217;" in plot):
            plot = plot.replace("&#8217;", "'")
        if ("&#8220;" in plot):
            plot = plot.replace('&#8220;', '"')
        if ("&#8221;" in plot):
            plot = plot.replace('&#8221;', '"')
        if ("&#215;" in plot):
            plot = plot.replace('&#215;', 'x')
        if ("&#x27;" in plot):
            plot = plot.replace('&#x27;', "'")
        if ("&#xF4;" in plot):
            plot = plot.replace('&#xF4;', "o")
        if ("&#xb7;" in plot):
            plot = plot.replace('&#xb7;', "-")
        if ("&#xFB;" in plot):
            plot = plot.replace('&#xFB;', "u")
        if ("&#xE0;" in plot):
            plot = plot.replace('&#xE0;', "a")
        if ("&#0421;" in plot):
            plot = plot.replace('&#0421;', "")
        if ("&#xE9;" in plot):
            plot = plot.replace('&#xE9;', "e")
        if ("&#xE2;" in plot):
            plot = plot.replace('&#xE2;', "a")
        if ("&#038;" in plot):
            plot = plot.replace('&#038;', "&")
        if ('&#' in plot) and (';' in plot):
            try:
                matches = re.compile('&#(.+?);').findall(plot)
            except:
                matches = ''
            if (matches is not ''):
                for match in matches:
                    if (match is not '') and (match is not ' ') and ("&#" + match + ";" in plot):
                        try:
                            plot = plot.replace("&#" + match + ";", "")
                        except:
                            pass
    for i in xrange(127, 256):
        try:
            plot = plot.replace(chr(i), "")
        except:
            pass
    return plot


def messupText(t, _html=False, _ende=False, _a=False, Slashes=False):
    if (_html == True):
        try:
            t = HTMLParser.HTMLParser().unescape(t)
        except:
            t = t
        try:
            t = ParseDescription(t)
        except:
            t = t
    if (_ende == True):
        try:
            t = t.encode('ascii', 'ignore')
            t = t.decode('iso-8859-1')
        except:
            t = t
    if (_a == True):
        try:
            t = _addon.decode(t)
            t = _addon.unescape(t)
        except:
            t = t
    if (Slashes == True):
        try:
            t = t.replace('_', ' ')
        except:
            t = t
    return t


def html_entity_decode_char(m):
        ent = m.group(1)
        if ent.startswith('x'):
            return unichr(int(ent[1:], 16))
        try:
            return unichr(int(ent))
        except:
            if ent in htmlentitydefs.name2codepoint:
                return unichr(htmlentitydefs.name2codepoint[ent])
            else:
                return ent


def html_entity_decode(string):
    string = string.decode('UTF-8')
    s = re.compile("&#?(\w+?);").sub(html_entity_decode_char, string)
    return s.encode('UTF-8')


def clean_html(html):
    """Clean an HTML snippet into a readable string"""
    if type(html) == type(u''):
        strType = 'unicode'
    elif type(html) == type(''):
        strType = 'utf-8'
        html = html.decode("utf-8")
    # Newline vs <br />
    html = html.replace('\n', ' ')
    html = re.sub(r'\s*<\s*br\s*/?\s*>\s*', '\n', html)
    html = re.sub(r'<\s*/\s*p\s*>\s*<\s*p[^>]*>', '\n', html)
    # Strip html tags
    html = re.sub('<.*?>', '', html)
    if strType == 'utf-8':
        html = html.encode("utf-8")
    return html.strip()


def video_google(url):
    try:
        import json
    except:
        import simplejson as json
    if (tfalse(addst("googlelog")) == True):
        logged_in = weblogingoogle.doLogin(addonPath, loginGoogle, passwordGoogle)
    url = nURL(url)
    url = re.compile('"fmt_stream_map",(".+?")').findall(url)[0]
    url = json.loads(url)
    url = [i.split('|')[-1] for i in url.split(',')]
    if url == []:
        return
    try:
        url = [i for i in url if not any(x in i for x in ['&itag=43&', '&itag=35&', '&itag=34&', '&itag=5&'])][0]
    except:
        url = url[0]
    return url


def vidfile(url):
    url = nURL(url)
    HD = re.compile("file: '(.+?)'").findall(url)[0]
    if HD == []:
        return
    url = HD
    return url


def mp4upload(url):
    url = nURL(url)
    HD = re.compile("'file': '(.+?)'").findall(url)[0]
    if HD == []:
        return
    url = HD
    return url


def sibnet(url):
    url = nURL(url)
    HD = re.compile("file' : '(.+?)'").findall(url)[0]
    if HD == []:
        return
    url = 'http://video.sibnet.ru' + HD
    return url


def vk_vk(url):
    url = nURL(url)
    HD = re.compile('url720=(.+?)&').findall(url)[0]
    if HD == []:
        return
    url = HD
    url = url.replace('https://', 'http://')
    return url


def vshare(url):
    url = nURL(url)
    HD = re.compile("url: '(.+?)'").findall(url)[0]
    if HD == []:
        return
    url = HD
    return url


def dailymotion(url):
    if not url.startswith('http://www.dailymotion.com/embed/video/'):
        url = 'http://www.dailymotion.com/embed/video/' + url.split('/')[-1][0:7]
    data = nURL(url)
    match = re.compile('"stream_h264.+?url":"(http[^"]+?H264-)([^/]+?)(/[^"]+?)"').findall(data)
    for i in range(len(match)):
        url = match[i][0] + match[i][1] + match[i][2]
        url = url.replace('\/', "/")
        return url


def PlayFromHost(url):
    PlayerMethod = addst("core-player")
    if   (PlayerMethod == 'DVDPLAYER'):
        PlayerMeth = xbmc.PLAYER_CORE_DVDPLAYER
    elif (PlayerMethod == 'MPLAYER'):
        PlayerMeth = xbmc.PLAYER_CORE_MPLAYER
    elif (PlayerMethod == 'PAPLAYER'):
        PlayerMeth = xbmc.PLAYER_CORE_PAPLAYER
    else:
        PlayerMeth = xbmc.PLAYER_CORE_AUTO
    play = xbmc.Player(PlayerMeth)
    import urlresolver
    infoLabels = {"Studio": addpr('studio', ''), "ShowTitle": addpr('showtitle', ''), "Title": addpr('title', '')}
    li = xbmcgui.ListItem(addpr('title', ''), iconImage=addpr('img', ''), thumbnailImage=addpr('img', ''))
    li.setInfo(type="Video", infoLabels=infoLabels)
    li.setProperty('IsPlayable', 'true')
    if ('google' in url):
        url = video_google(url)
    elif ('vk' in url):
        url = vk_vk(url)
    elif ('sibnet' in url):
        url = sibnet(url)
    elif ('dailymotion' in url):
        url = dailymotion(url)
    elif ('youtube.com' in url):
        stream_url = url
    elif ('vidfile' in url):
        url = vidfile(url)
    elif ('mp4upload.com' in url):
        url = mp4upload(url)
    elif ('vshare' in url):
        url = vshare(url)
    else:
        try:
            stream_url = urlresolver.HostedMediaFile(url).resolve()
        except:
            myNote("urlresolver.HostedMediaFile(url).resolve()", "Failed to Resolve Playable URL.")
            return
    try:
        _addon.resolve_url(url)
    except:
        t = ''
    try:
        play.play(stream_url, li)
    except:
        t = ''


def GetDataBeetwenMarkers(data, marker1, marker2, withMarkers=True, caseSensitive=True):
    if caseSensitive:
        idx1 = data.find(marker1)
    else:
        idx1 = data.lower().find(marker1.lower())
    if -1 == idx1:
        return False, ''
    if caseSensitive:
        idx2 = data.find(marker2, idx1 + len(marker1))
    else:
        idx2 = data.lower().find(marker2.lower(), idx1 + len(marker1))
    if -1 == idx2:
        return False, ''
    if withMarkers:
        idx2 = idx2 + len(marker2)
    else:
        idx1 = idx1 + len(marker1)
    return True, data[idx1:idx2]


# This function raises a keyboard for user input
def getUserInput(title=u"Input", default=u"", hidden=False):
    result = None
    # Fix for when this functions is called with default=None
    if not default:
        default = u""
    keyboard = xbmc.Keyboard(default, title)
    keyboard.setHiddenInput(hidden)
    keyboard.doModal()
    if keyboard.isConfirmed():
        result = keyboard.getText()
    return result
