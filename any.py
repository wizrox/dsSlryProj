#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Author: Ken
git : https://github.com/PlayingNumbers/ds_salary_proj
Tutorial(youtube) : https://www.youtube.com/watch?v=GmW4F6MHqqs&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

Inspired by (Tutorial) : https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Disclaimer: I don't own the copyrights of the code , It was written and coded as
            followed on the youtube channel as mentioned above.please take a note that I have changed the names of the column and files according to my need
                   , if you are copy pasting this code you have to look for syntax errors in names of files and
                   data-columns that are used in tutorial.
"""


import glassdoor_scrapper as gs
import pandas as pd


# path = "FirefoxDriver/geckodriver"
path = "ChromeDriver/chromedriver" # ChromeDriver is Folder, inside the fodler is file "chromedriver"

df = gs.get_jobs('data scientist',100,False, path,10)

df.to_csv('glsDr_jobs.csv', index=False)
