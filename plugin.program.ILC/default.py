# -*- coding: utf-8 -*-
import xbmcgui
import xbmcaddon
import xbmc
import re
import os

my_addon = xbmcaddon.Addon('plugin.program.ILC')
addonPath = my_addon.getAddonInfo('path')

try:
    iptvsimple_addon = xbmcaddon.Addon('pvr.iptvsimple')
    iptvsimpledir = xbmc.translatePath(iptvsimple_addon.getAddonInfo('profile'))
    settingsiptv = iptvsimpledir + 'settings.xml'
except:
    xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % ('ILM', "IPTVsimple wyłączony", 1, ''))
    exit()


m3uUrl_1 = my_addon.getSetting("m3uUrl_1")
m3uUrl_2 = my_addon.getSetting("m3uUrl_2")
m3uUrl_3 = my_addon.getSetting("m3uUrl_3")

m3uPath_1 = my_addon.getSetting("m3uPath_1")
m3uPath_2 = my_addon.getSetting("m3uPath_2")
m3uPath_3 = my_addon.getSetting("m3uPath_3")

m3uPathType_1 = my_addon.getSetting("m3uPathType_1")
m3uPathType_2 = my_addon.getSetting("m3uPathType_2")
m3uPathType_3 = my_addon.getSetting("m3uPathType_3")

txtpath = my_addon.getSetting("txtPath")


def CATEGORIES():
    if my_addon.getSetting("sourceCount") == '0':
        if m3uPathType_1 == '0':
            lista = [[m3uPath_1, m3uPath_1], ['Plik z adresami list', 'txtpath']]
        elif m3uPathType_1 == '1':
            lista = [[m3uUrl_1, m3uUrl_1], ['Plik z adresami list', 'txtpath']]
        menu(lista)
    elif my_addon.getSetting("sourceCount") == '1':
        if m3uPathType_1 == '0' and m3uPathType_2 == '0':
            lista = [[m3uPath_1, m3uPath_1], [m3uPath_2, m3uPath_2], ['plik txt', 'txtpath']]
        elif m3uPathType_1 == '1' and m3uPathType_2 == '0':
            lista = [[m3uUrl_1, m3uUrl_1], [m3uPath_2, m3uPath_2], ['plik txt', 'txtpath']]
        elif m3uPathType_1 == '0' and m3uPathType_2 == '1':
            lista = [[m3uPath_1, m3uPath_1], [m3uUrl_2, m3uUrl_2], ['plik txt', 'txtpath']]
        elif m3uPathType_1 == '1' and m3uPathType_2 == '1':
            lista = [[m3uUrl_1, m3uUrl_1], [m3uUrl_2, m3uUrl_2], ['plik txt', 'txtpath']]
        menu(lista)


def read_data(lista):
    if 'txtpath' in lista:
        txtfile()
    else:
        with open(settingsiptv, 'r') as f:
            read_data = f.read()
            if 'http:' in lista:
                read_data = re.sub('<setting id="m3uPathType" value="\d" />', '<setting id="m3uPathType" value="1" />', read_data)
                read_data = re.sub('<setting id="m3uUrl" value(.+?)/>', '<setting id="m3uUrl" ''value' + '="' + lista + '" />', read_data)
            else:
                read_data = re.sub('<setting id="m3uPathType" value="\d" />', '<setting id="m3uPathType" value="0" />', read_data)
                lista = lista.replace(os.path.sep, '/')
                read_data = re.sub('<setting id="m3uPath" value(.+?)/>', '<setting id="m3uPath" ''value' + '="' + lista + '" />', read_data)
            f.close()
        with open(settingsiptv, 'wb') as f:
            f.write(read_data)
            f.close()
        dis_or_enable_addon('pvr.iptvsimple', enable="false")
        dis_or_enable_addon('pvr.iptvsimple')


def txtfile():
    with open(txtpath, 'r') as f:
        lists = []
        for line in f:
            lists.append(line.rstrip().split(","))
        f.close()
        menufile(lists)


def menufile(lista):
    d = xbmcgui.Dialog()
    item = d.select("Wybierz listę", getItemTitles(lista))
    if item != -1:
        lista = str(lista[item][0])
        lista2 = lista.lower()
        read_data(lista2)


def menu(lista):
    d = xbmcgui.Dialog()
    item = d.select("Wybierz listę", getItemTitles(lista))
    if item != -1:
        lista = str(lista[item][1])
        lista2 = lista.lower()
        read_data(lista2)


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def dis_or_enable_addon(addon_id, enable="true"):
    import json
    addon = '"%s"' % addon_id
    if xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "true":
        return xbmc.log("### Skipped %s, reason = allready enabled" % addon_id)
    elif not xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "false":
        return xbmc.log("### Skipped %s, reason = not installed" % addon_id)
    else:
        do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon, enable)
        query = xbmc.executeJSONRPC(do_json)
        response = json.loads(query)
        if enable == "true":
            xbmc.log("### Enabled %s, response = %s" % (addon_id, response))
        else:
            xbmc.log("### Disabled %s, response = %s" % (addon_id, response))

CATEGORIES()

