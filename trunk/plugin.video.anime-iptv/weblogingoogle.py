# -*- coding: UTF-8 -*-

"""
 weblogin
 by Anarchintosh @ xbmcforums
 Copyleft (GNU GPL v3) 2011 onwards

 this example is configured for Fantasti.cc login
 See for the full guide please visit:
 http://forum.xbmc.org/showthread.php?p=772597#post772597


 USAGE:
 in your default.py put:

 import weblogin
 logged_in = weblogin.doLogin('a-path-to-save-the-cookie-to','the-username','the-password')

 logged_in will then be either True or False depending on whether the login was successful.
"""

import os
import re
import urllib,urllib2
import cookielib

### TESTING SETTINGS (will only be used when running this file independent of your addon)
# Remember to clear these after you are finished testing,
# so that your sensitive details are not in your source code.
# These are only used in the:  if __name__ == "__main__"   thing at the bottom of this script.
#myusername = 'huball@ymail.com'
#mypassword = 'daytek1980'
#note, the cookie will be saved to the same directory as weblogin.py when testing


def check_login(source,username):

    #the string you will use to check if the login is successful.
    #you may want to set it to:    username     (no quotes)
    logged_in_string = 'huball'

    #search for the string in the html, without caring about upper or lower case
    if re.search(logged_in_string,source,re.IGNORECASE):
        return True
    else:
        return False


def doLogin(cookiepath, username, password):

    #check if user has supplied only a folder path, or a full path
    if not os.path.isfile(cookiepath):
        #if the user supplied only a folder path, append on to the end of the path a filename.
        cookiepath = os.path.join(cookiepath,'cookies.lwp')

    #delete any old version of the cookie file
    try:
        os.remove(cookiepath)
    except:
        pass

    if username and password:

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(opener)



        #the url you will request to.
        login_url = 'https://accounts.google.com/ServiceLogin?service=grandcentral'
        authenticate_url = 'https://accounts.google.com/ServiceLoginAuth?service=grandcentral'
        login_page_contents = opener.open(login_url).read()
        galx_match_obj = re.search(r'name="GALX"\s*type="hidden"\n\s*value="([^"]+)"', login_page_contents, re.IGNORECASE)
        galx_value = galx_match_obj.group(1) if galx_match_obj.group(1) is not None else ''

        #build the form data necessary for the login
#        login_data = urllib.urlencode({'user':username, 'pass':password, 'memento':1, 'x':0, 'y':0, 'do':'login'})
        login_params = urllib.urlencode({
            'Email': username,
            'Passwd': password,
            'continue': 'https://www.google.com/voice/account/signin',
            'GALX': galx_value
        })

        opener.open(authenticate_url, login_params)
#        gv_home_page_contents = opener.open(gv_home_page_url).read()

        #build the request we will make
        req = urllib2.Request(authenticate_url, login_params)
#        req.add_header('User-Agent',header_string)

        #initiate the cookielib class
        cj = cookielib.LWPCookieJar()

        #install cookielib into the url opener, so that cookies are handled
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        #do the login and get the response
        response = opener.open(req)
        response.close()

        #check the received html for a string that will tell us if the user is logged in
        #pass the username, which can be used to do this.
#        login = check_login(gv_home_page_contents,username)

        #if login suceeded, save the cookiejar to disk
#        if login == True:
        cj.save(cookiepath)

        #return whether we are logged in or not
#        return login

#    else:
#        return False

#code to enable running the .py independent of addon for testing
if __name__ == "__main__":
    if myusername is '' or mypassword is '':
        print 'YOU HAVE NOT SET THE USERNAME OR PASSWORD!'
    else:
        logged_in = doLogin(os.getcwd(),myusername,mypassword)
        print 'LOGGED IN:',logged_in
