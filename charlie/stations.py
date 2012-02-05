# foo

stations = {}

class Station:
    def __init__(self, name):
        self.name   = name
        self.lookup = {}

    def setLat(self, lat):
        self.lat = lat
    def setLon(self, lon):
        self.lon = lon
    def setLine(self, line):
        self.line = line

    def addPlatform(self, platkey, stop):
        self.lookup[platkey] = stop
    def getPlatforms(self):
        return self.lookup
    def getPlatform(self, name):
        return self.lookup[name]
