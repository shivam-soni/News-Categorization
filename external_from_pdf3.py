# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 20:51:20 2016

@author: Sonix
"""

import urllib
import re
from urllib import urlopen
from bs4 import BeautifulSoup
import datetime
import unicodedata


def getData(insideSite,fp):
    html=urlopen(insideSite)
    bsObj1 = BeautifulSoup(html,"lxml")
    dataList=bsObj1.find_all("p")
    global s
    global s1
    s=''
    s1=''
    for data in dataList: 
        s=s+data.get_text()
    s1=s.encode('utf-8')
    print( s1)    
    fp.write(s1)
    fp.write("\n\n\t\t\t*******************NEW SITE*************************\n\n")
    fp.write(insideSite)
    
    

def getExternalLinks(bsObj, excludeUrl):
    global externalLinks
    externalLinks=[]
    #Finds all links that start with "http" or "www" that do
    #not contain the current URL
    for link in bsObj.findAll("a",href=re.compile("^(http|www|https)((?!"+excludeUrl+").)*$"),limit=8):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("https://","").split("/")
    return addressParts





seeds="https://www.bing.com/search?q=theft+related+news&go=Search&qs=n&pq=theft+related+&sc=0-14&sp=-1&sk=&cvid=D4953FA1A49344ABB30461EEC2F90C40&first=91&FORM=PORE"
j=0
externalLinks = []
s=''
s1=''
fp=open("Theft_Data.txt","a")
while(j<100):
    print (seeds)
    html = urlopen(seeds)    
    bsObj = BeautifulSoup(html,"lxml")
    externalLinks = getExternalLinks(bsObj, splitAddress(seeds)[0])
    for i in range(0,len(externalLinks)):
        print (externalLinks[i])
        if(externalLinks[i]=="http://go.microsoft.com/fwlink/?LinkId=521839&CLCID=4009"):
            break
        else:
            getData(externalLinks[i],fp)
    #getData(externalLinks[1])
    #print externalLinks[1]
    
    nextSeed=''
    l=bsObj.findAll("a",{"class":"sb_pagN"})
    if (len(l)!=0):
        for l1 in l:
            nextSeed=l1.attrs['href']    
            seeds="https://www.bing.com"+nextSeed
            j=j+1
            print (j)
    else:
        print ("Work completed")
        break

fp.close() 
    

#print("Random external link is: "+externalLink)

