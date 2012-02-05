import json

import charlie.lines      as cL
import charlie.stops      as cSp
import charlie.stations   as cS
import charlie.trains     as cT

import charlie.transport  as transport

def load_trains( line ):
    trains = transport.fetch_line(line)
    for train in trains:
        tripid = train['Trip']
        t = cT.Train( tripid )
        t.setGoodies( train )
        cT.trains[tripid] = t

def load_lines( data ):
    for platform in data:
        line = platform["Line"]
        if line not in cL.lines:
            cL.lines[line] = cL.Line(line)

def load_stations( data ):
    for platform in data:
        line    = platform["Line"]
        station = platform["StationName"]
        lat     = platform["stop_lat"]
        lon     = platform["stop_lon"]

        if station not in cS.stations:
            s = cS.Station(station)
            s.setLat( lat )
            s.setLon( lon )
            s.setLine( line )
            cS.stations[station] = s
            cL.lines[line].addStation( station, s )

def load_platforms( data ):
    for platform in data:
        sid = platform["PlatformKey"]
        host = platform["StationName"]

        if sid not in cSp.stops:
            stop = cSp.Stop(sid)
            stop.setGoodies(platform)
            cSp.stops[sid] = stop
            cS.stations[host].addPlatform(sid, stop)

def load_data( csv ):
    data = open(csv, 'r').readlines()
    data = [ s.strip().split(",") for s in data ]
    headers = data[0]
    hkey    = {}
    data = data[1:]
    zData = []
    for d in data:
        platform = {}
        for x in range(0,len(headers)):
            platform[headers[x]] = d[x]
        zData.append(platform)
    # first, we need all the lines in place.
    load_lines( zData )
    load_stations( zData )
    load_platforms( zData )

    #for line in cL.lines:
    load_trains("Red")#line)
