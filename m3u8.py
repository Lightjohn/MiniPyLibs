#!/usr/bin/python
# -*- coding: utf8 -*-

class m3u8:
    def __init__(self):
        pass

    def new_file(self,name):
        self.f = open(name,"w")
        self.f.write("#EXTM3U\n\n")
    
    def add_music(self,path, title = "", time=-1):
        if title == "":
            title = path.split("/")[-1]
        self.f.write("#EXTINF:"+str(time)+","+title+"\n")
        self.f.write(path+"\n\n")

    def close(self):
        self.f.close()

