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
