import os
import charlie.data

import charlie.stops
import charlie.stations
import charlie.lines

Stops    = charlie.stops.stops
Stations = charlie.stations.stations
Lines    = charlie.lines.lines

__appname__ = "python-charlie"
__version__ = "0.1~pre1"

_cache_file_raw = "~/.python-charlie.cache"
_cache_file      = os.path.expanduser(_cache_file_raw)

# _apiurl     = "http://developer.mbta.com/Data/"
_apiurl     = "http://tag.pault.ag/charlie-fake/"
_datadir    = "/home/tag/dev/local/python-charlie/data"
_csvfile    = _datadir + "/station.data.csv"

charlie.data.load_data( _csvfile )
