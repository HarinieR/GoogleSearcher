#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:54:56 2018

@author: harinie.r
"""

from tkinter import Tk
from Searcher.windowDesigner import makeWindowCenter, setWindowProperties
from Searcher.GoogleSearcher import GoogleSearcher


if __name__ == "__main__":
    window = Tk()
    window.title("GOOGLE SEARCHER")
    makeWindowCenter(window)
    setWindowProperties(window)
    app = GoogleSearcher(window)
    window.mainloop()