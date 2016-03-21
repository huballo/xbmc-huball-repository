import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonname = addon.getAddonInfo('name')
line1 = "Animejoy addon is now a part of Anime-IPTV addon."
line2 = "You can find it in my repository."
line3 = "Greetings, huball"
xbmcgui.Dialog().ok(addonname, line1, line2, line3)