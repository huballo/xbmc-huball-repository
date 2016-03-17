# -*- coding: utf-8 -*-

### Imports ###
import  os
import sys
import xbmc
import xbmcaddon
import xbmcvfs
from addon.common.addon import Addon  # może trzeba więcej
#######
try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database
##########
iconFav = xbmcaddon.Addon(id="plugin.video.anime-iptv").getAddonInfo('path') + '/art/favorites.png'
_addon = Addon('plugin.video.anime-iptv', sys.argv)
_artIcon = _addon.get_icon()
_artFanart = _addon.get_fanart()
addonInfo = xbmcaddon.Addon().getAddonInfo
dataPath = xbmc.translatePath(addonInfo('profile')).decode('utf-8')
xbmcvfs.mkdir(dataPath)
favouritesFile = os.path.join(dataPath, 'favourites.db')
###########


def bFL(t):
    return '[B]' + t +'[/B]'  # For Bold Text ###


def myNote(header='', msg='', delay=5000, image=iconFav):
    _addon.show_small_popup(title=header, msg=msg, delay=delay, image=image)


def fav__COMMON__list_fetcher(site, section='', subfav=''):
    saved_favs = ('favs_' + site + '__' + section + subfav + '__')
    try:
        db = database.connect(favouritesFile)
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS pluginvideoanimeiptv(name TEXT unique, data TEXT)''')
        db.commit()
        cur.execute("SELECT * FROM pluginvideoanimeiptv WHERE name=?", (saved_favs,))
        items = cur.fetchall()
        for row in items:
            favs = sorted(eval(row[1]), key=lambda fav: (fav[1], fav[0]), reverse=True)
            ItemCount=len(favs)
            if favs:
                return favs
            else:
                return ''
        else:
            return ''
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def fav__COMMON__check(site, section, name, year, subfav=''):
    saved_favs = ('favs_' + site + '__' + section + subfav + '__')
    try:
        db = database.connect(favouritesFile)
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS pluginvideoanimeiptv(name TEXT unique, data TEXT)''')
        db.commit()
        cur.execute("SELECT * FROM pluginvideoanimeiptv WHERE name=?", (saved_favs,))
        items = cur.fetchall()
        for row in items:
            favs = eval(row[1])
            if favs:
                for (_name, _year, _img, _fanart, _country, _url, _plot, _Genres, _site, _subfav, _section, _ToDoParams, _commonID, _commonID2) in favs:
                    if (name == _name):
                        return True
                return False
            else:
                return False
        else:
            return False
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def fav__COMMON__remove(site, section, name, year, subfav=''):
    saved_favs = ('favs_' + site + '__' + section + subfav + '__')
    tf = False
    try:
        db = database.connect(favouritesFile)
        cur = db.cursor()
        cur.execute("SELECT * FROM pluginvideoanimeiptv WHERE name=?", (saved_favs,))
        items = cur.fetchall()
        for row in items:
            favs = eval(row[1])
            if favs:
                for (_name, _year, _img, _fanart, _country, _url, _plot, _Genres, _site, _subfav, _section, _ToDoParams, _commonID, _commonID2) in favs:
                    favs.remove((_name, _year, _img, _fanart, _country, _url, _plot, _Genres, _site, _subfav, _section, _ToDoParams, _commonID, _commonID2))
                    favs = unicode(favs)
                    cur.execute('UPDATE pluginvideoanimeiptv SET data = ? WHERE name = ? ', (favs, saved_favs))
                    db.commit()
                    tf = True
                    myNote(bFL(name.upper() + '  (' + year + ')'), bFL('Usunięto z ulubionych.'))
                    xbmc.executebuiltin("XBMC.Container.Refresh")
                if (tf == False):
                    myNote(bFL(name.upper()), bFL('Nie znaleziono w ulubionych.'))
            else:
                myNote(bFL(name.upper() + '  (' + year + ')'), bFL('Nie znaleziono w ulubionych.'))
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def fav__COMMON__add(site, section, name, year='', img=_artIcon, fanart=_artFanart, subfav='', plot='', commonID='', commonID2='', ToDoParams='', Country='', Genres='', Url=''):
    saved_favs =  ('favs_' + site + '__' + section + subfav + '__')
    favs = []
    favs.append((name, year, img, fanart, Country, Url, plot, Genres, site, subfav, section, ToDoParams, commonID, commonID2))
    favs = unicode(favs)
    try:
        db = database.connect(favouritesFile)
        cur = db.cursor()
        cur.execute("SELECT count(*) FROM pluginvideoanimeiptv WHERE name = ?", (saved_favs,))
        data = cur.fetchone()[0]
        if data == 0:
            print('There is no component named %s'%saved_favs)
            cur.execute('''INSERT INTO pluginvideoanimeiptv(name, data) VALUES(?,?)''', (saved_favs,favs))
            db.commit()
        else:
            print('Component %s found in rows' % (saved_favs))
            cur.execute("SELECT * FROM pluginvideoanimeiptv WHERE name=?", (saved_favs,))
            items = cur.fetchall()
            for row in items:
                favs = eval(row[1])
                if favs:
                    for (_name, _year, _img, _fanart, _country, _url, _plot, _Genres, _site, _subfav, _section, _ToDoParams, _commonID, _commonID2) in favs:
                        if (name == _name) and (year == _year):
                            if len(year) > 0:
                                myNote(bFL(section + ':  ' + name.upper() + '  (' + year + ')'), bFL('Jest już w ulubionych.'))
                            else:
                                myNote(bFL(section + ':  ' + name.upper()), bFL('Jest już w ulubionych.'))
                            return
                favs.append((name, year, img, fanart, Country, Url, plot, Genres, site, subfav, section, ToDoParams, commonID, commonID2))
                favs = unicode(favs)
                cur.execute('UPDATE pluginvideoanimeiptv SET data = ? WHERE name = ? ', (favs, saved_favs))
                db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()
    if len(year) > 0:
        myNote(bFL(name + '  (' + year + ')'), bFL('Dodano do ulubionych.'))
    else:
        myNote(bFL(name), bFL('Dodano do ulubionych.'))


#def fav__COMMON__empty(site, section, subfav=''):
#    favs = []
#    cache.set('favs_' + site + '__' + section + subfav + '__', str(favs))
#    myNote(bFL('Favorites'), bFL('Your Favorites Have Been Wiped Clean.'))