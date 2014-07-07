#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: lvtongda

import urllib
import urllib2
import re

videourl = raw_input('Please input the video url of cntv: ')
title = raw_input('Please input the title of the video: ')
url = 'http://www.flvcd.com/parse.php?kw=' + urllib.quote(videourl) + '&format=high'
req = urllib2.Request(url)
req.add_header('host', 'www.flvcd.com')
res = urllib2.urlopen(req)
html = res.read()

pattern = re.compile('<input\s+type="hidden"\s+name="inf"\s+value="([^"]+)')
match = pattern.search(html)
urls = match.group(1).split('|')
urls.pop()

for k, v in enumerate(urls):
    print '>downloading Block %.2d ...' % (k+1,)
    urllib.urlretrieve(v, str(k) + title + '.flv')
    print 'downloading Block.%.2d completely<' % (k+1,)
