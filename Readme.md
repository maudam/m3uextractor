## m3uextractor

Actual release 0.6

A simple program to convert .m3u file in something useful to pass to external software.

This script convert standard .m3u file to a list of urls with the filename from the tvg-name field appended to the url and with file suffix from original link.  
The output file can be processed by software like the wonderful **jdownloader** (https://jdownloader.org)

Future improvements:
- additional output formats


---
Input file format  (2 lines per link):


        #EXTINF:-1 tvg-id="id field" tvg-name="name field" tvg-logo="Url of logo" group-title="title field",name field
        http://path/to/some/url/rAnDoMnAmE.mp4
---

Output file format:

        http://path/to/some/url/rAnDoMnAmE.mp4#name=tvg-name field.mp4

License: GPLV2
