#!/usr/bin/env python

import charlie

for line in charlie.Lines:
    print line
    for station in charlie.Lines[line].getStations():
        print "  " + station
        for platform in charlie.Stations[station].getPlatforms():
            print "    " + platform
