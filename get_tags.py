#!/usr/bin/env python
# coding=utf-8

import os
import re

class User_Tag_Analysis:

    def __init__(self):
        self.tagDic = dict()

    def get_book_tags(self, fileName):
        with open(fileName,"r") as infile:
            content = infile.read().decode("UTF-8")
            print(type(content))
            #print("content: %s"%content)
            tagList = re.findall(ur'"\>标签:(?P<tag>.*)\<', content)
            print("contentlen:%d, len: %d", len(content), len(tagList))
            print(type(tagList[0]))
            for tagStr in tagList:
                #print(tag)
                tags = tagStr.split(" ")
                for tag in tags:
                    if self.tagDic.has_key(tag):
                        self.tagDic[tag] += 1
                    elif tag.strip():
                        self.tagDic[tag] = 1;
        print ("begin access fileName[%s]"%(fileName))

    def print_tag_dict(self):
        print(type(self.tagDic))
        for k, v in self.tagDic.items():
            print("key: %s, value:%d"%(k, v))
        print("sorted tag, freq:")
        sortedTagFreq = sorted(self.tagDic.items(), key=lambda item:item[1], reverse=True)
        print(type(sortedTagFreq))
        for kv in sortedTagFreq:
            print("key: %s, value:%d"%(kv[0], kv[1]))
        #print(sortedTagFreq)



if __name__ == "__main__":
    userTagAna = User_Tag_Analysis()
    for p, d, files in os.walk('/home/LX/gitcode/SpiderLearn/'):
        if p == r'/home/LX/gitcode/SpiderLearn/':
            for fileName in files:
                if re.match(r'.*html$', fileName):
                    print fileName
                    with open(fileName, "r") as infile:
                        userTagAna.get_book_tags(fileName)
    userTagAna.print_tag_dict();
