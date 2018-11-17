#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:20:26 2018

@author: harinie.r
"""

from Searcher.searcher import open_url
from tkinter import Frame, Label, Entry, Button, StringVar, IntVar, W, E, TclError


class GoogleSearcher():
    def __init__(self,master):
        self.window = master
        
        '''
        --- Create the labels and entries to get the search query
        --- Create the button to open up the search result(s) pages
        '''
        
        self.query_frame = Frame(self.window)
        
        self.query_lbl = Label(self.query_frame, text="search for", width=20, height=2, padx=20, anchor=W, font=(None,15))
        self.query_lbl.grid(row=0, column=0)
        
        self.no_of_links_lbl = Label(self.query_frame, text="No of links to open", width=20, height=2, padx=20, anchor=W, font=(None,15))
        self.no_of_links_lbl.grid(row=1, column=0)
        
        # Create Entry widgets for User to enter the query to search and the no of links User want to open
        self.query = StringVar()
        self.query_entry = Entry(self.query_frame, textvariable=self.query, width=25)
        self.query_entry.grid(row=0, column=1, columnspan=5, padx=2, pady=2, sticky=W+E)
        self.query_entry.focus_set()
        
        self.no_of_links = IntVar()
        self.no_of_links.set(1)
        self.no_of_links_entry = Entry(self.query_frame, textvariable=self.no_of_links, width=25)
        self.no_of_links_entry.grid(row=1, column=1, columnspan=5, padx=2, pady=2, sticky=W+E)
        
        self.info_lbl = Label(self.query_frame, text="[optional - opens a tab by default - even if entered 0!]", width=35, height=1, font=(None,8))
        self.info_lbl.grid(row=2, column=1, columnspan=5, padx=2, pady=2, sticky=W)
        
        self.query_frame.grid(row=0, column=0, pady=10)
        
        # Create search button to search the entered query
        self.search_button = Button(self.window, text="SEARCH", width=8, command=lambda : open_url(str(self.query.get()),self.get_no_of_links()))
        self.search_button.grid(row=1, column=0)
        
    
    def get_no_of_links(self):
        '''
        Handling exception if User skips with the no_of_links_entry box !
        '''
        
        try:
            return self.no_of_links.get()
        except TclError:
            return 1