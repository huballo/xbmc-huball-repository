### #########################################################################

### # Author:             #        The Highway
### # Description:     #        Downloader File For:  The Binary Highway

### #########################################################################
### #########################################################################
### Imports ###
from common import *


def download(url, destfile, destpath, useResolver=True):
    import urllib
    dp = ''
    link = url
    if isPath(destpath)==False:
        os.mkdir(destPath)
    myNote('Starting Download', destfile, 100)
    urllib.urlretrieve(link, xbmc.translatePath(os.path.join(destpath, destfile)), lambda nb, bs, fs, url=url: _pbhook(nb, bs, fs, url, dp))
    myNote('Download Complete', destfile, 15000)


def _pbhook(numblocks, blocksize, filesize, url, dp):
    try:
        percent = min((numblocks * blocksize * 100) / filesize, 100)
    except:
        percent = 100
