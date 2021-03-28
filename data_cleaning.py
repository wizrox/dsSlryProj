#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Ken
git : https://github.com/PlayingNumbers/ds_salary_proj
Tutorial(youtube) : https://www.youtube.com/watch?v=fhi4dOhmW-g&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=3

Inspired by (Tutorial) : https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Disclaimer: I don't own the copyrights of the code , It was written and coded as
            followed on the youtube channel as mentioned above, I have add extra comments for 
            my reference to make code understandable.please take a note that I have changed the names of the column and files according to my need
                   , if you are copy pasting this code you have to look for syntax errors in names of files and
                   data-columns that are used in tutorial.
"""

import pandas as pd
df = pd.read_csv('glsDr_jobs.csv')

#A)salary parsing: all code frome line 21 - 37
#Company name text onloy
#state field
#age of company
# parsing of Job description(python, etc.)


#-----------3making column from existing columns values to classify the data category like"per-hour" to "yearly-salary"

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided_salary'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

#removing the values of -1 in column "Salary Estimate" ----------1
df = df[df['Salary Estimate'] != '-1']

# making value of "salary Estimate" column numerical ---------------------2
salary = df["Salary Estimate"].apply(lambda x: x.split('(')[0]) # where x="[Salry Estimate ]" value

minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))


df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary) / 2
#A)salary parsing : finishes

#B)Company name text only
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1) #<------learn about "axis = 1"
#`^^^^^ this line of code will detect company-name with column rating value greater than 0 and omit the last 3 characters
 #` from the 'company name' column (the value with rating if any) and store them in new column of name 'company txt'
 
#C)state field
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1]) # whenever it's says 'KeyError:' it refers to the column_name /dictionary name which is case sensitive like in this case is 'Location' != 'location'
df.job_state.value_counts()

# df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis = 1)
# ^^^^^^ this line of code will not comply with this datasest as there were no columen name"Headquarters" exist in dataset

#D)age of company
df['age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)

#E) parsing of job description (python, etc.)

#ptyhon
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
# 

# R
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
# df.R_yn.value_counts()

# spark
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# df.spark.value_counts()

#aws
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
# df.aws.value_counts()

#excel
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
# df.excel.value_counts()

# df.columns #<------to get the list of column names in 'str{}'
# df_out = df.drop(['Unnamed: 0'], axis=1) # <----to remove the column


df.to_csv('salary_data_cleansed.csv', index = False) # <--- to avoud index col i.e.'[Unnamed: 0]' set 'index = False'
# ^^^ to save the .csv file

# pd.read_csv('salary_data_cleansed.csv')
# ^^^^ to read the file using 'panda'