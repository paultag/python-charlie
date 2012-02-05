# foo

stations = {}

class Station:
    def __init__(self, name):
        self.name = name
        self.platforms = {}

    def setLat(self, lat):
        self.lat = lat
    def setLon(self, lon):
        self.lon = lon
    def setLine(self, line):
        self.line = line

    def addStop(self, platform_name, platform):
        self.platforms[platform_name] = platform
    def getStop(self, platform_name):
        return platforms[platform_name]
    def getStops(self):
        return platforms
