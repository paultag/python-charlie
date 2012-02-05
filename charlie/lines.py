# Lines.

lines = {}

class Line:
    def __init__(self, name):
        self.name     = name
        self.stations = {}

    def addStation(self, station_name, station):
        self.stations[station_name] = station

    def getStations(self):
        return self.stations

    def getStation(self, station):
        return self.stations[station]
