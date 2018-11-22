# -*- coding: utf-8 -*-

import os
import re
import shutil
import unicodedata
import requests
import xbmc
import xbmcvfs
import xbmcaddon
from AnimesubUtil import AnimesubUtil

__addon__ = xbmcaddon.Addon()
__version__ = __addon__.getAddonInfo('version')  # Module version
__scriptname__ = __addon__.getAddonInfo('name')
__language__ = __addon__.getLocalizedString
__profile__ = unicode(xbmc.translatePath(__addon__.getAddonInfo('profile')), 'utf-8')
__temp__ = unicode(xbmc.translatePath(os.path.join(__profile__, 'temp', '')), 'utf-8')

regexHelper = re.compile('\W+', re.UNICODE)


def normalizeString(str):
    return unicodedata.normalize(
        'NFKD', unicode(unicode(str, 'utf-8'))
    ).encode('utf-8', 'ignore')


def log(msg):
    xbmc.log((u"### [%s] - %s" % (__scriptname__, msg)).encode('utf-8'), level=xbmc.LOGDEBUG)


def notify(msg_id):
    xbmc.executebuiltin((u'Notification(%s,%s)' % (__scriptname__, __language__(msg_id))).encode('utf-8'))


def clean_title(item):
    title = os.path.splitext(os.path.basename(item["title"]))
    tvshow = os.path.splitext(os.path.basename(item["tvshow"]))
    if len(title) > 1:
        if re.match(r'^\.[a-z]{2,4}$', title[1], re.IGNORECASE):
            item["title"] = title[0]
        else:
            item["title"] = ''.join(title)
    else:
        item["title"] = title[0]
    if len(tvshow) > 1:
        if re.match(r'^\.[a-z]{2,4}$', tvshow[1], re.IGNORECASE):
            item["tvshow"] = tvshow[0]
        else:
            item["tvshow"] = ''.join(tvshow)
    else:
        item["tvshow"] = tvshow[0]
    item["title"] = unicode(item["title"], "utf-8")
    item["tvshow"] = unicode(item["tvshow"], "utf-8")
    # Removes country identifier at the end
    item["title"] = re.sub(r'\([^\)]+\)\W*$', '', item["title"]).strip()
    item["tvshow"] = re.sub(r'\([^\)]+\)\W*$', '', item["tvshow"]).strip()


def parse_rls_title(item):
    title = regexHelper.sub(' ', item["title"])
    tvshow = regexHelper.sub(' ', item["tvshow"])
    groups = re.findall(r"(.*?) (\d{4})? ?(?:s|season|)(\d{1,2})(?:e|episode|x|\n)(\d{1,2})", title, re.I)
    if len(groups) == 0:
        groups = re.findall(r"(.*?) (\d{4})? ?(?:s|season|)(\d{1,2})(?:e|episode|x|\n)(\d{1,2})", tvshow, re.I)
    if len(groups) > 0 and len(groups[0]) >= 3:
        title, year, season, episode = groups[0]
        item["year"] = str(int(year)) if len(year) == 4 else year
        item["tvshow"] = regexHelper.sub(' ', title).strip()
        item["season"] = str(int(season))
        item["episode"] = str(int(episode))
        log("TV Parsed Item: %s" % (item,))
    else:
        groups = re.findall(r"(.*?)(\d{4})", item["title"], re.I)
        if len(groups) > 0 and len(groups[0]) >= 1:
            title = groups[0][0]
            item["title"] = regexHelper.sub(' ', title).strip()
            item["year"] = groups[0][1] if len(groups[0]) == 2 else item["year"]
            log("MOVIE Parsed Item: %s" % (item,))


class NapisyHelper:
    def get_subtitle_list(self, item):
        search_results = self._search_tvshow(item)
        log("Search results: %s" % search_results)
        return search_results

    def get_results(self, name, language):
        results = []
        url = "http://animesub.info/szukaj.php?szukane={0}&pTitle={1}".format(name, language)
        s = requests.Session()
        r = s.get(url)
        read_data = r.text
        list_items = re.compile('<tr class="KNap"><td align="left">(.+?)<\/td>([\S\s]+?)value="(.+?)">([\S\s]+?)value="(.+?)">').findall(read_data)
        count = len(list_items)
        if count > 0:
            for item in list_items:
                title = item[0]
                kod = item[2]
                token = item[4]
                cookie = (s.cookies.items())
                cookie = (cookie[0][1])
                results.append({"title": title, "kod": kod, "token": token, "cookie": cookie})

            AnimesubUtil.sort_by_similarity(name, "title", results)
        return results

    def _search_tvshow(self, item):
        if item.get('searchstring', None):
            name = item['searchstring']
        else:
            name = AnimesubUtil(item["file_original_name"]).searchable()
        log("Szukana nazwa: %s" % name)
        results = self.get_results(name, "org")
        if len(results) == 0:
            results = self.get_results(name, "en")
        if len(results) == 0:
            results = self.get_results(name, "pl")
        return results

    def download(self, kod, token, zip_filename, cookie, file_name):
        ## Cleanup temp dir, we recomend you download/unzip your subs in temp folder and
        ## pass that to XBMC to copy and activate
        if xbmcvfs.exists(__temp__):
            shutil.rmtree(__temp__)
        xbmcvfs.mkdirs(__temp__)
        cookies = {'ansi_sciagnij': cookie}
        data = [('id', kod), ('sh', token), ('single_file', 'Pobierz napisy')]
        r = requests.post('http://animesub.info/sciagnij.php', cookies=cookies, data=data)
        with open(zip_filename, "wb") as subFile:
            subFile.write(r.content)
        subFile.close()
        AnimesubUtil(file_name).prepare_zip(zip_filename)
        xbmc.Monitor().waitForAbort(0.5)
        xbmc.executebuiltin(('XBMC.Extract("%s","%s")' % (zip_filename, __temp__,)).encode('utf-8'), True)
