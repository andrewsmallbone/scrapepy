#! /usr/bin/python

# https://github.com/andrewsmallbone/scrapepy/yahoo-weather.py
# by Andrew Smallbone <andrew@rocketnumbernine.com>
# Use freely, please send corrections/extensions/improvements


# Uses Yahoo weather API to get some weather info for given Location
# See full API at http://developer.yahoo.com/weather/
# example output:
# 4C Fair
# low: -1C, high: 2C
# PM Rain/Snow Showers
# sun: 7:22-5:43


# uses lxml: installed with 'pip install lxml' or 'easy_install lxml'
from lxml import etree


def get_yahoo_weather(location, units='c'):
    url = "http://weather.yahooapis.com/forecastrss?u={0}&w={1}".format(units, location)
    return etree.parse(url)

# helper to return to string value of the xpath within the yahoo rss/channel div
def get(doc, path):
    return doc.xpath('string(/rss/channel/{})'.format(path), namespaces = {'yweather': 'http://xml.weather.yahoo.com/ns/rss/1.0'})


if __name__ == "__main__":

    # get weather for Helsinki in centigrade
    # search for location ID at http://weather.yahoo.com/  use 'f' for fahrenheit
    doc = get_yahoo_weather(26194557, 'c')

    # current temperature and condition
    (temp, condition) = (get(doc, 'item/yweather:condition[1]/@temp'), get(doc, 'item/yweather:condition[1]/@text'))

    # forecast - only first (usually 'later today') 'yweather:forecast[2]' usually gives tomorrow forecast
    (day, low, high, text) = (get(doc, 'item/yweather:forecast[1]/@day'), get(doc, 'item/yweather:forecast[1]/@low'),
                    get(doc, 'item/yweather:forecast[1]/@high'), get(doc, 'item/yweather:forecast[1]/@text'))

    # sunrise and sunset - ignore the am/pm
    (sunrise, sunset) = (get(doc, 'yweather:astronomy[1]/@sunrise').split()[0],  get(doc, 'yweather:astronomy[1]/@sunset').split()[0])

    width = 20 # only display 20 characters per line
    print "{0}C {1}".format(temp, condition)[:width]
    print "low: {0}C, high: {1}C".format(low, high)[:width]
    print text[:width]
    print "sun: {0}-{1}".format(sunrise, sunset)[:width]

