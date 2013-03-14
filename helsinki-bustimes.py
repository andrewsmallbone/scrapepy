#! /usr/bin/python

# helsinki-bustimes.py
# by Andrew Smallbone <andrew@rocketnumbernine.com>.
# Use freely.

# Prints the next bus times for the specified bus stops and route that leave after
# the given number of minutes (shortname, busstop code, route, minutes)
# So if you live near two bus stops (named S and R) one takes 5 minutes to walk to, 
# the other 10 minutes the following would show the next busses to depart from each
# after the walking time so you can decide which to walk to.
stops = [('S', 'V5139', '2', 5), ('R', 'V5128', '2', 10)]

# example output:

# now: 10:40
# S 10:46 10:53 11:08
# R 11:57 12:17


# Uses the Helsinki HSL/HRT Reittiopas API which requires a 
# (free) username/password: from: http://developer.reittiopas.fi/pages/en/home.php
# check the examples and geolocation API to get busstop codes.
username = 'xx'
password = 'xx'


# uses lxml: installed with 'pip install lxml' or 'easy_install lxml'
from lxml import etree
import re

import datetime
from datetime import timedelta
now = datetime.datetime.now()

url = 'http://api.reittiopas.fi/hsl/prod/?format=xml&user={0}&pass={1}&request=stop&code={2}&time={3.hour:02}{3.minute:02}&time_limit=120'

# returns a list of times ("hh:mm") of the next buses leaving the specified 
# bus stop, on the given line, after the specified minutes from now
# http://developer.reittiopas.fi/pages/en/http-get-interface-version-2.php#stop
def get_departures(stop, line, after):
    departure_time = now+timedelta(minutes=after)
    doc = etree.parse(url.format(username, password, stop, departure_time))
    return [re.sub('(..)$', ':\\1', departure.findtext('time')) # return  "hh:mm" instead of "hhmm"
        for departure in doc.xpath('/response/node/departures/node')
        if (departure.findtext('code').rsplit()[1] == line)]

print "now: {0.hour}:{0.minute:02}".format(now)
for stop in stops:
    print stop[0] + " " + " ".join(get_departures(stop[1], stop[2], stop[3])[:3])

