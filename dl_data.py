
#download and plot covid19 counrtries death number data

#@author: Kaneka

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

covid=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
#print(covid)

# =========Convert data from github into a dataframe with dates as index and countries/province as column names

df=covid.T # transpose covid dataframe into df dataframe
countries=list(covid['Country/Region']) # create a list 'countries' of countries from the column 'Country/Region' in covid

province=list(covid['Province/State']) # create a list of 'province' from the column 'Province/State' in covid

colnames= [i if str(j)=='nan' else i+'/'+j  for i, j in zip(countries, province)] # create a list by concatenating countries names and "/" and province names

df.columns= colnames # Set new column names to df dataframe
df=df.drop(df.index[[0,1,2,3]]) # remove the first 4 lines of df with country, province, lat,long
df.index=pd.to_datetime(df.index, format='%m/%d/%y') # set new index with date as datetime64[ns] format
#==================== Plot ======================
dfp=df[['France','Italy','Spain','Tanzania','Sweden','Portugal','Poland','Brazil']] # select column with specific names of countries and store it into dfp dataframe to plot
dfp.plot()
