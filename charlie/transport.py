#

import charlie
import urllib2
import json
import time

def fetch_line( line ):
    cfd = charlie._cache_folder + "/%s" % line
    try:
        fd = open( cfd, 'r' )
        cache = json.load(fd)
        if time.time() < cache["timestamp"] + charlie.MAX_PING:
            return cache["payload"]
    except IOError:
        pass

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
    payload = json.loads(f.read())

    fd = open( cfd, 'w' )
    fd.write(json.dumps({
        "timestamp" : time.time(),
        "payload"   : payload
    }))

    return payload
