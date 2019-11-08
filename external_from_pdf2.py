# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 10:55:26 2016

@author: Sonix
"""
import urllib
import re
from urllib import urlopen
from bs4 import BeautifulSoup
import random
import datetime
import random
seeds="https://www.bing.com/search?q=murder+related+news&first=561&FORM=PERE5"
j=0
externalLinks = []
s=''
s1=''
fp=open("DatacomingFrom_57th_seed.txt","w")
while(j<1000):
    print seeds
    html = urlopen(seeds)    
    bsObj = BeautifulSoup(html,"lxml")
    address=seeds
    try:
        addressParts = address.replace("https://", "").split("/")
        externalLinks=[]
        excludeUrl=addressParts[0]
        for link in bsObj.findAll("a",href=re.compile("^(http|www|https)((?!"+excludeUrl+").)*$"),limit=8):
            if link.attrs['href'] is not None:
                if link.attrs['href'] not in externalLinks:
                    externalLinks.append(link.attrs['href'])
                    
        for i in range(0,len(externalLinks)):
            print externalLinks[i]
            html1=urlopen(externalLinks[i])
            bsObj1 = BeautifulSoup(html1,"lxml")
            dataList=bsObj1.find_all("p")
            s=''
            s1=''
            for data in dataList: 
                s=s+data.get_text()
            s1=s.encode('utf-8')
            print s1    
            fp.write(s1)
            fp.write("\n\n\t\t\t*******************NEW SITE*************************\n\n")
    except:
        for l in bsObj.findAll("a",{"class":"sb_pagN"}):
            nextSeed=l.attrs['href']    
        seeds="https://www.bing.com"+nextSeed
        continue
    
    for l in bsObj.findAll("a",{"class":"sb_pagN"}):
        nextSeed=l.attrs['href']    
    seeds="https://www.bing.com"+nextSeed
    j=j+1
    print j
    
fp.close()
    