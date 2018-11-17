#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:19:55 2018

@author: harinie.r
"""

from tkinter import messagebox


def makeWindowCenter(window):
    '''
    To make the screen fit in the center of the user's screen
    '''
    width = 500
    height = 180
    scr_width = window.winfo_screenwidth()
    scr_height = window.winfo_screenheight()
    x = (scr_width-width)/2
    y = (scr_height-height)/2
    window.geometry("%dx%d+%d+%d" %(width,height,x,y))
    
    
    
def setWindowProperties(window):
    '''
    --- Disable full screen button from the window,
    --- as the application is designed only for fixed width
    '''
    
    window.resizable(0,0)
         
    '''
    --- Handling ESCAPE button and Window close Button
    '''
    
    window.protocol("WM_DELETE_WINDOW",lambda : close_searcher(window))
    window.bind("<Escape>",lambda e: close_searcher(window))
        


def close_searcher(window):
    "CLose the window and quit the application if user confirms"
    if(messagebox.askokcancel("QUIT", "    Do you want to quit the search ?",parent=window)):
        window.quit()