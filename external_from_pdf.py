# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 00:43:06 2016

@author: Sonix
"""
import urllib
import re
from urllib import urlopen
from bs4 import BeautifulSoup
import random
import datetime
import random
pages = set()
random.seed(datetime.datetime.now())
#Retrieves a list of all Internal links found on a page
'''def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
#Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks'''
#Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
#Finds all links that start with "http" or "www" that do
#not contain the current URL
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                print "111"
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    print "222"
    return externalLinks[random.randint(0, len(externalLinks)-1)]
'''if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:'''
    
def followExternalOnly():
    externalLink = getRandomExternalLink("https://www.bing.com/search?q=murder+related+news&FORM=AWRE")
    print("Random external link is: "+externalLink)
    followExternalOnly()

followExternalOnly()