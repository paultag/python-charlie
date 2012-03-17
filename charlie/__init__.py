import os
import charlie.data

import charlie.stops
import charlie.stations
import charlie.lines
import charlie.trains

import dateutil.tz as tz
import datetime as dt

TIMEZONE     = tz.gettz('America/New_York')
#                                ^^^^^^^^
#                              Yankees Suck!
epoch    = dt.datetime(1970, 1, 1, tzinfo=TIMEZONE)
MAX_PING = 30 # in seconds

stop_list    = charlie.stops.stops
station_list = charlie.stations.stations
line_list    = charlie.lines.lines
train_list   = charlie.trains.trains

def get_station_by_stop( platform ):
    stop = stop_list[platform]
    return station_list[stop.getStationName()]

__appname__ = "charlie"
__version__ = "0.5"

_cache_folder_raw = "~/.python-charlie"
_cache_folder     = os.path.expanduser(_cache_folder_raw)

_apiurl     = "http://developer.mbta.com/Data/"
# _apiurl     = "http://tag.pault.ag/charlie-fake/"
# _apiurl      = "http://localhost/"
_datadir    = "/usr/share/charlie/data"
_csvfile    = _datadir + "/station.data.csv"

def refresh():
    return charlie.data.load_data( _csvfile )
refresh()
