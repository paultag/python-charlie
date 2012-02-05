#

import datetime as dt
import charlie

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

    def link_stops(self):
        events = self.getEvents()
        for i in range(1, len(events)):
            events[i - 1][1]['next'] = events[i][1]["PlatformKey"]
            events[i][1]["prev"] = events[i - 1][1]["PlatformKey"]

    def getStop(self, name):
        return self.stopdata[name]

    def getTrip(self):
        return self.name

    def getNextEvent(self, f=None):
        if f == None:
            f = self.getMostCloseEvent()
        if f["InformationType"] != "Predicted":
            try:
                return self.getNextEvent( self.stopdata[f["next"]] )
            except KeyError:
                return None
        return f

    def getMostCloseEvent(self):
        events = self.getEvents()
        lEventT= charlie.epoch
        lEvent = None
        now    = dt.datetime.now(charlie.TIMEZONE)
        for date, key in events:
            if abs( date - now ) < abs( lEventT - now ):
                lEventT, lEvent = date, key
        return lEvent

    def getLastKnownEvent(self):
        lke = { "TargetTime" : charlie.epoch } # XXX: Fixme
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
        time = time.replace( tzinfo=charlie.TIMEZONE )

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
        self.link_stops()
