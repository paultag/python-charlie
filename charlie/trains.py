#

import datetime as dt

trains = {}

class Train:
    def __init__(self, name):
        self.name     = name
        self.stopdata = {}

    def getEvents(self):
        ret = []
        for key in self.stopdata:
            ret.append((
                self.stopdata[key]["TargetTime"],
                self.stopdata[key]
            ))
        return sorted( ret )

    def getMostCloseEvent(self):
        events = self.getEvents()
        lEventT= dt.datetime(1970, 1, 1) 
        lEvent = None
        now    = dt.datetime.now()
        for date, key in events:
            if ( date - now ) > ( lEventT - now ):
                lEventT, lEvent = date, key
        return lEvent

    def getLastKnownEvent(self):
        lke = { "TargetTime" : dt.datetime(1970, 1, 1) }
        # print self.stopdata
        for item in self.stopdata:
            d = self.stopdata[item]["TargetTime"]
            if d > lke["TargetTime"]:
                lke = self.stopdata[item]
        return lke

    def addInfo(self, goodies):
        if goodies["Trip"] != self.name:
            raise Exception("That's not me!") # XXX: Fixme

        time = dt.datetime.strptime(goodies["Time"], "%m/%d/%Y %I:%M:%S %p")
        goodies["Time"] = time
        delt = goodies["TimeRemaining"]
        neg = False
        if delt[:1] == "-":
            neg = True
            delt = delt[1:]
        hms = [ int(d) for d in delt.split(":") ]
        delt = dt.timedelta(hours=hms[0], minutes=hms[1], seconds=hms[2])
        if neg:
            t = time - delt
        else:
            t = time + delt
        goodies["TargetTime"] = t
        goodies["TimeRemaining"] = delt
        self.stopdata[goodies["PlatformKey"]] = goodies
