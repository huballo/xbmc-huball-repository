# -*- coding: utf-8 -*-
import os
import sys
import urllib

try:
    import xbmc
    import xbmcvfs
    import xbmcaddon
    import xbmcplugin
    import xbmcgui
except ImportError:
    from tests.stubs import xbmc, xbmcgui, xbmcaddon, xbmcplugin, xbmcvfs

__addon__ = xbmcaddon.Addon()
__scriptid__ = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__version__ = __addon__.getAddonInfo('version')
__language__ = __addon__.getLocalizedString

__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
__profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile')).decode("utf-8")
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib')).decode("utf-8")
__temp__ = xbmc.translatePath(os.path.join(__profile__, 'temp', '')).decode("utf-8")

sys.path.append(__resource__)

from NapisyUtils import NapisyHelper
from NapisyUtils import log
from NapisyUtils import normalizeString
from NapisyUtils import clean_title
from NapisyUtils import parse_rls_title


def search(item):
    helper = NapisyHelper()
    subtitles_list = helper.get_subtitle_list(item)
    file_name = item["file_original_name"]
    if subtitles_list:
        for it in subtitles_list:
            listitem = xbmcgui.ListItem(label="Polish", label2=it["title"], iconImage=str("0"), thumbnailImage="pl")
            numer = it["kod"]
            token = it["token"]
            cookie = it["cookie"]
            url = "plugin://%s/?action=download&id=%s&token=%s&cookie=%s&file_name=%s" % (__scriptid__, numer, token, cookie, file_name)
            xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=listitem, isFolder=False)
    return


def download(sub_id, token, cookie, file_name):  # standard input
    subtitle_list = []
    exts = [".srt", ".sub", ".txt", ".ass"]
    zip_filename = os.path.join(__temp__, "subs.zip")
    helper = NapisyHelper()
    helper.download(sub_id, token, zip_filename, cookie, file_name)
    for file in xbmcvfs.listdir(__temp__)[1]:
        full_path = os.path.join(__temp__, file)
        if os.path.splitext(full_path)[1] in exts:
            subtitle_list.append(full_path)
    return subtitle_list


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = paramstring
        cleanedparams = params.replace('?', '')
        if (params[len(params) - 1] == '/'):
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]
    return param


params = get_params()

if params['action'] in ['search', 'manualsearch']:
    item = {}
    item['temp'] = False
    item['rar'] = False
    item['year'] = xbmc.getInfoLabel("VideoPlayer.Year")  # Year
    item['season'] = str(xbmc.getInfoLabel("VideoPlayer.Season"))  # Season
    item['episode'] = str(xbmc.getInfoLabel("VideoPlayer.Episode"))  # Episode
    item['tvshow'] = normalizeString(xbmc.getInfoLabel("VideoPlayer.TVshowtitle"))  # Show
    item['title'] = normalizeString(xbmc.getInfoLabel("VideoPlayer.OriginalTitle"))  # try to get original title
    item['file_original_path'] = urllib.unquote(
        xbmc.Player().getPlayingFile().decode('utf-8'))  # Full path of a playing file
    item['file_original_name'] = os.path.basename(item['file_original_path'])  # Name of playing file
    item['3let_language'] = []
    item['preferredlanguage'] = unicode(urllib.unquote(params.get('preferredlanguage', '')), 'utf-8')
    item['preferredlanguage'] = xbmc.convertLanguage(item['preferredlanguage'], xbmc.ISO_639_2)

    for lang in urllib.unquote(params['languages']).decode('utf-8').split(","):
        item['3let_language'].append(xbmc.convertLanguage(lang, xbmc.ISO_639_2))

    if item['title'] == "":
        log("VideoPlayer.OriginalTitle not found")
        item['title'] = normalizeString(xbmc.getInfoLabel("VideoPlayer.Title"))  # no original title, get just Title

    if params['action'] == 'manualsearch':
        item['searchstring'] = urllib.unquote(params['searchstring'])

    for lang in unicode(urllib.unquote(params['languages']), 'utf-8').split(","):
        item['3let_language'].append(xbmc.convertLanguage(lang, xbmc.ISO_639_2))

    log("Item before cleaning: \n    %s" % item)

    # clean title + tvshow params
    clean_title(item)
    parse_rls_title(item)

    if item['episode'].lower().find("s") > -1:  # Check if season is "Special"
        item['season'] = "0"
        item['episode'] = item['episode'][-1:]

    if (item['file_original_path'].find("http") > -1):
        item['temp'] = True

    elif (item['file_original_path'].find("rar://") > -1):
        item['rar'] = True
        item['file_original_path'] = os.path.dirname(item['file_original_path'][6:])

    elif (item['file_original_path'].find("stack://") > -1):
        stackPath = item['file_original_path'].split(" , ")
        item['file_original_path'] = stackPath[0][8:]

    item["file_original_size"] = xbmcvfs.File(item["file_original_path"]).size()

    log("item: %s" % (item))

    search(item)

elif params['action'] == 'download':
    ## we pickup all our arguments sent from def search()
    numer = params["id"]
    token = params["token"]
    cookie = params["cookie"]
    file_name = params["file_name"]
    subs = download(numer, token, cookie, file_name)

    ## we can return more than one subtitle for multi CD versions, for now we are still working out how to handle that in XBMC core
    for sub in subs:
        listitem = xbmcgui.ListItem(label=sub)
        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=sub, listitem=listitem, isFolder=False)

xbmcplugin.endOfDirectory(int(sys.argv[1]))  # send end of directory to XBMC
