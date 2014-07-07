#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: lvtongda

import urllib
import urllib2
import re

videourl = raw_input('You must input the url of the video: ')
title = raw_input('You can input the custom name of the video or not: ')
quality = raw_input('You can input the definition of the video or not: ')
url = 'http://www.flvcd.com/parse.php?kw=' + urllib.quote(videourl) + '&format=' + quality
req = urllib2.Request(url)
req.add_header('host', 'www.flvcd.com')
res = urllib2.urlopen(req)
html = res.read()

pattern = re.compile('<input\s+type="hidden"\s+name="inf"\s+value="([^"]+)')
match = pattern.search(html)
urls = match.group(1).split('|')
urls.pop()

for k, v in enumerate(urls):
    print 'Downloading block %.2d ...' % (k+1)
    urllib.urlretrieve(v, str(k+1) + '-' + title + '.flv')
    print 'Downloading block %.2d completely' % (k+1)
