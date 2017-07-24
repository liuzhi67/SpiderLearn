#!/usr/bin/env python
# coding=utf-8

import os
import re

def get_book_tags(url):
    print ("begin access url[%s]"%(url))

for p, d, files in os.walk('/home/LX/gitcode/SpiderLearn/'):
    if p == r'/home/LX/gitcode/SpiderLearn/':
        for fileName in files:
            if re.match(r'.*html$', fileName):
                print fileName
                with open(fileName, "r") as infile:
                    get_book_tags(fileName)
