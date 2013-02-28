scrapepy
========

Some python scripts for scraping websites - html/xml/rss/json

Written for producing content for display on 4x20 LCD controlled by phatIO, for example:

	yahoo-weather.py > /Volumes/PHATIO/dev/lcd

See http://www.phatio.com/ and http:www.phatio.com/ideas/HD44780/, but with a little editing can be used for other purposes.

**yahoo-weather.py**

Displays some weather info for given location using xpath with lxml, example output:

	4C Fair
	low: -1C, high: 2C
	PM Rain/Snow Showers
	sun: 7:22-5:43


**helsinki-bustimes.py**

Given a list of Helsinki bus stop codes, routes, and the time it takes you to walk to each, it will display the departure times so you can decide which to walk to.

	now: 11:15
	S 11:23 11:38 11:54
	R 11:37 11:57 12:17

Uses xpath and the lxml API.  This should work for buses/trains but has only been tested with bus stops - there's a huge amount of functionality at [http://developer.reittiopas.fi/pages/en/home.php].