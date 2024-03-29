#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
'''
Author: Ken
git : https://github.com/PlayingNumbers/ds_salary_proj
Tutorial(youtube) : https://www.youtube.com/watch?v=QWgg4w1SpJ8&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=6

Inspired by (Tutorial) : https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Disclaimer: I don't own the copyrights of the code , It was written and coded as
            followed on the youtube channel as mentioned above, I have add extra comments for 
            my reference to make code understandable.please take a note that I have changed the names of the column and files according to my need
                   , if you are copy pasting this code you have to look for syntax errors in names of files and
                   data-columns that are used in tutorial.
'''
"""

import requests
from data_input import data_in

URL = 'http://0.0.0.0:8080/predict'
headers = {"Content-Type":"application/json"}
data = {"input": data_in}

r = requests.get(URL, headers = headers, json = data)

r.json()
