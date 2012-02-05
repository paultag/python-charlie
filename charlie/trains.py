#

import datetime as dt

trains = {}

class Train:
    def __init__(self, name):
        self.name = name

    def setGoodies(self, goodies):
        if goodies["Trip"] != self.name:
            raise Exception("That's not me!") # XXX: Fixme
        self._goodies = goodies
        time = dt.datetime.strptime(goodies["Time"], "%m/%d/%Y %H:%M:%S %p")
        self._goodies["Time"] = time
        delt = self._goodies["TimeRemaining"]
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
        self._goodies["TargetTime"] = t
        self._goodies["TimeRemaining"] = delt

    def _goodie(self, goodie):
        return self._goodies[goodie]

    # foo

    def getLine(self):
        return self._goodie("Line")
    def getTrip(self):
        return self._goodie("Trip")
    def getTargetTime(self):
        return self._goodie("TargetTime")
    def getLastKnownPlatform(self):
        return self._goodie("PlatformKey")
    def getLastKnownCheckinType(self):
        return self._goodie("InformationType")
    def getTime(self):
        return self._goodie("Time")
    def getTimeRemaining(self):
        return self._goodie("TimeRemaining")
    def getRevenue(self):
        return self._goodie("Revenue")
    def getRoute(self):
        return self._goodie("Route")
