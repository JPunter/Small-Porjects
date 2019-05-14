'''
To do:
Build date range
Build query options as user inputs (location,job title, range from location)
    Build database parser to check that jobId doesnt already exist in database. (I don't want dubplicates)
Build data return from reed class
Build data thinner with Reed class
Build data submission to database

'''
import sys
import pandas as pd 

from datetime import date
from datetime import timedelta
from time import sleep

from reed import Reed
from postgres import PostGresTools as pgtools 

#These must be passed with the application initialisation
clientkey = sys.argv[1]
# 3dbd30fd-117e-42a5-ac4f-2f1908c082ed
dbkey = sys.argv[2]
# ACV0Cw5CDcWQWyNfXqaA

#Establish connection to both the API host and the locally hosted PostGreSQL database
Reed = Reed(key = clientkey)
pg = pgtools(dbname = "jobSeeker", user = "postgres",
                host = "localhost", password = dbkey)

# Provides a date range to the program that will just search for jobs posted in the last 7 days
# This keeps the data returned to a more reasonable scale in London
date_range = pd.date_range(
    date.today() - timedelta(days=7), 
    date.today())

# if you want to send more locations to the API for results, add them to this list
locations = ["Truro"]
#keywords to be fed into the search function
keywords = ["Software","Software engineer","Graduate software"]


for location in locations:
    for keyword in keywords:
        tmp = Reed.search(keywords=keyword,
                          locationName=location, 
                          distanceFromLocation="1") #Default distance set at 10 miles
data = Reed.json_to_pd(tmp)


for date in date_range:
    for post_date in tmp["results"]["date"]:
        if date == post_date:
            print("Found")
