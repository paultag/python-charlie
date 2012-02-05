# 

import charlie
import urllib2
import json

def fetch_line( line ):
    uas = "%s/%s (http://charlie.pault.ag)" % (
        charlie.__appname__, charlie.__version__
    )
    url = "%s/%s.json" % (
        charlie._apiurl,
        line
    )
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', uas)]
    f = opener.open( url )
    return json.loads(f.read())
