# -*- coding: utf-8 -*-
import xbmcplugin
import xbmcgui
import xbmcaddon
import sys
mainSite = 'http://tvgry.pl/'
my_addon = xbmcaddon.Addon('plugin.video.Pac-12')
addonPath = my_addon.getAddonInfo('path')
icon = addonPath + '/icon.png'
fanart = addonPath + '/fanart.jpg'


addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

# Pac National
url = 'http://goo.gl/0CofPI'
li = xbmcgui.ListItem('Pac National 720p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://xrxs.net/video/live-p12netw-4728.m3u8'
li = xbmcgui.ListItem('Pac National 1080p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

# Arizona
url = 'http://goo.gl/yy2Y0F'
li = xbmcgui.ListItem('Arizona 720p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://xrxs.net/video/live-p12ariz-4728.m3u8'
li = xbmcgui.ListItem('Arizona 1080p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

# Bay Area
url = 'http://goo.gl/gHG3ty'
li = xbmcgui.ListItem('Bay Area 720p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://xrxs.net/video/live-p12baya-4728.m3u8'
li = xbmcgui.ListItem('Bay Area 1080p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

# Los Angeles
url = 'http://goo.gl/m4Xaul'
li = xbmcgui.ListItem('Los Angeles 720p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://xrxs.net/video/live-p12losa-4728.m3u8'
li = xbmcgui.ListItem('Los Angeles 1080p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

# Mountain
url = 'http://goo.gl/6QnKIG'
li = xbmcgui.ListItem('Mountain 720p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://xrxs.net/video/live-p12moun-4728.m3u8'
li = xbmcgui.ListItem('Mountain 1080p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

# Oregon
url = 'http://goo.gl/FLfuDu'
li = xbmcgui.ListItem('Oregon 720p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://xrxs.net/video/live-p12oreg-4728.m3u8'
li = xbmcgui.ListItem('Oregon1080p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

# Washington
url = 'http://goo.gl/ZOww80'
li = xbmcgui.ListItem('Washington 720p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://xrxs.net/video/live-p12wash-4728.m3u8'
li = xbmcgui.ListItem('Washington 1080p', iconImage=icon)
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
