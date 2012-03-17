#

stops = {}

class Stop:
    def __init__(self, name):
        self.name = name

    def setGoodies(self, goodies):
        self.goodies = goodies

    def getGoodies(self):
        return self.goodies

    def _goodie(self, name):
        return self.goodies[name]

    def getLine(self):
        return self._goodie("Line")

    def getPlatformKey(self):
        return self._goodie("PlatformKey")

    def getPlatformName(self):
        return self._goodie("PlatformName")

    def getStationName(self):
        return self._goodie("StationName")

    def getPlatformOrder(self):
        return self._goodie("PlatformOrder")

    def isStartOfLine(self):
        return self._goodie("StartOfLine") == "TRUE"

    def isEndOfLine(self):
        return self._goodie("EndOfLine") == "TRUE"

    def getBranch(self):
        return self._goodie("Branch")

    def getDirection(self):
        return self._goodie("Direction")

    def getStopID(self):
        return self._goodie("stop_id")

    def getStopCode(self):
        return self._goodie("stop_code")

    def getStopName(self):
        return self._goodie("stop_name")

    def getStopDescription(self):
        return self._goodie("stop_desc")

    def getLat(self):
        return self._goodie("stop_lat")

    def getLon(self):
        return self._goodie("stop_lon")
