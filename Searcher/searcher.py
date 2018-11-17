#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:18:56 2018

@author: harinie.r
"""

from requests import get
from bs4 import BeautifulSoup
import webbrowser


def open_url(query, no_of_links):
    
    if(no_of_links == 0):
        no_of_links = 1
        
    res = get('https://google.com/search?q='+query)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    linkElements = soup.select('.r a')
    link2open = min(no_of_links,len(linkElements))
    
    for i in range(link2open):
        webbrowser.open('https://google.com'+linkElements[i].get('href'))
    