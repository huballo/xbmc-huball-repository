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


def byteify(input):
    if isinstance(input, dict):
        return dict([(byteify(key), byteify(value)) for key, value in input.iteritems()])
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input


def addpr(r, s=''):
    return _addon.queries.get(r, s)


def addst(r, s=''):
    return _addon.get_setting(r)

loginGoogle = addst('username3', '')
passwordGoogle = addst('password3', '')


def tfalse(r, d=False):
    if   (r.lower() == 'true') or (r.lower() == 't') or (r.lower() == 'y') or (r.lower() == '1') or (r.lower() == 'yes'):
        return True
    elif (r.lower() == 'false') or (r.lower() == 'f') or (r.lower() == 'n') or (r.lower() == '0') or (r.lower() == 'no'):
        return False
    else:
        return d


def iFL(t):
    return '[I]' + t + '[/I]'  # For Italic Text ###


def bFL(t):
    return '[B]' + t + '[/B]'  # For Bold Text ###


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
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def vidfile(url):
    try:
        url = nURL(url)
        HD = re.compile("file: '(.+?)'").findall(url)[0]
        if HD == []:
            return
        url = HD
        return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def mp4upload(url):
    try:
        url = nURL(url)
        print url
        HD = re.compile("'file': '(.+?)'").findall(url)[0]
        if HD == []:
            return
        url = HD
        return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def sibnet(url):
    try:
        url = nURL(url)
        HD = re.compile("file' : '(.+?)'").findall(url)[0]
        if HD == []:
            return
        url = 'http://video.sibnet.ru' + HD
        return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def vk_vk(url):
    try:
        url = nURL(url)
        HD = re.compile('url720=(.+?)&').findall(url)[0]
        if HD == []:
            return
        url = HD
        url = url.replace('https://', 'http://')
        return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def vshare(url):
    try:
        url = nURL(url)
        HD = re.compile("url: '(.+?)'").findall(url)[0]
        if HD == []:
            return
        url = HD
        return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def dailymotion(url):
    try:
        if not url.startswith('http://www.dailymotion.com/embed/video/'):
            url = 'http://www.dailymotion.com/embed/video/' + url.split('/')[-1][0:7]
        data = nURL(url)
        match = re.compile('"stream_h264.+?url":"(http[^"]+?H264-)([^/]+?)(/[^"]+?)"').findall(data)
        for i in range(len(match)):
            url = match[i][0] + match[i][1] + match[i][2]
            url = url.replace('\/', "/")
            return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def animeuploader(url):
    url = nURL(url)
    try:
        HD = re.compile("{file: '(.+?)',").findall(url)[0]
        if HD == []:
            return
        url = HD
        return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


def animeonline(url):
    url = nURL(url)
    try:
        HD = re.compile('<source src="(.+?)"').findall(url)[0]
        if HD == []:
            return
        url = HD
        return url
    except:
        myNote("Failed to Resolve Playable URL.")
        return


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
    elif ('animeuploader' in url):
        url = animeuploader(url)
    elif ('animeonline' in url):
        url = animeonline(url)
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
