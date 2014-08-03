#! /usr/bin/python
# -*- coding: UTF-8 -*-

# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys
import os
import urllib2
import signal

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(2)

class libnet:
    def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(2)
    
    data = None

    txheaders = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'User-Agent: AppleCoreMedia/1.0.0.10B350 (iPhone; U; CPU OS 6_1_4 like Mac OS X; fr_fr)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-EN,fr;q=0.8,en-US;q=0.6,en;q=0.4',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 
    'Content-Type': 'application/x-www-form-urlencoded',
    }
    
    txheadersiphone = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/6.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/21.0.1084.52 Safari/546.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-EN,fr;q=0.8,en-US;q=0.6,en;q=0.4',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'identity', 
    'Accept': '*/* ',
    'Accept-Language': 'fr-fr', 
    'Connection': 'keep-alive',  
    'Content-Type': 'application/x-www-form-urlencoded',
    }
   
    headers = {'Accept' : 'application/xml'}
    
    def __init__(self):
        pass

    def file_exists(self,fichier):
        try:
            file(fichier)
            return True
        except:
            return False
        
    def download_file(self,url,out):
        signal.signal(signal.SIGINT, signal_handler)
        file_name = url.split('/')[-1]
        if not os.path.isfile(out+file_name):
            req = urllib2.Request(url,self.data,self.txheadersiphone)
            u = urllib2.urlopen(req)
            f = open(out+file_name, 'wb')
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
                file_size_dl += len(buffer)
                f.write(buffer)
            f.close()

    def download_image(self,url,out):
	download_file(url,out)
            
    def download_html(self,url):
        req = urllib2.Request(url,self.data,self.txheaders)
        con = urllib2.urlopen(req)
        return con.read()
