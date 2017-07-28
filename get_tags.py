#!/usr/bin/env python
# coding=utf-8

import os
import re

def get_book_tags(fileName):
    with open(fileName,"r") as infile:
        content = infile.read().decode("UTF-8")
        print(type(content))
        #print("content: %s"%content)
        tagList = re.findall(ur'"\>标签:(?P<tag>.*)\<', content)
        print("contentlen:%d, len: %d", len(content), len(tagList))
        print(type(tagList[0]))
        for tag in tagList:
            print(tag)
    print ("begin access fileName[%s]"%(fileName))


if __name__ == "__main__":
    for p, d, files in os.walk('/home/LX/gitcode/SpiderLearn/'):
        if p == r'/home/LX/gitcode/SpiderLearn/':
            for fileName in files:
                if re.match(r'.*html$', fileName):
                    print fileName
                    with open(fileName, "r") as infile:
                        get_book_tags(fileName)
