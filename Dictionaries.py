#!/usr/bin/env python
# coding: utf-8

# In[111]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
import csv 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Decision Tree 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
#Time Series packages
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY
import datetime


# In[23]:


SNHU_2010 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2010', header = 0)
SNHU_2011 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2011', header = 0)
SNHU_2012 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2012', header = 0)
SNHU_2013 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2013', header = 0)
SNHU_2014 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2014', header = 0)
SNHU_2015 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2015', header = 0)
SNHU_2016 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2016', header = 0)
SNHU_2017 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2017', header = 0)
SNHU_2018 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2018', header = 0)
SNHU_2019 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2019', header = 0)
SNHU_2020 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2020', header = 0)
SNHU_2021 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2021', header = 0)
SNHU_2022 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2022', header = 0)


# In[ ]:


#Scrap Code
#'Team Faced':SNHU_2011[6].Opponent,
   #                        'SNHU Runs': Runs[0],
    #                       'Opps Runs': Runs[1],
     #                      'Ks': SNHU_2011[6].K,


# In[105]:


Runs = SNHU_2011[6]['Score'].str.split('-', expand = True)


# In[143]:


Abs = pd.Series(SNHU_2011[6].AVG)


# In[144]:


Abs


# In[136]:


#Schedule Dictonary
SNHU_Schedule_Dictionary = {'Date': SNHU_2011[6].Date,
                           'Game to Game BA': SNHU_2011[6].AVG,
                           'Overall BA': SNHU_2011[6].H/ SNHU_2011[6].AB}


# In[137]:


#Creating a dataframe for the schedule dictionary 
Schedule = pd.DataFrame(SNHU_Schedule_Dictionary)


# In[140]:


Schedule


# In[138]:


Schedule.index = pd.to_datetime(Schedule.index)


# In[139]:


Schedule.plot(grid = True)


# In[119]:


type(Schedule['Date'])


# In[ ]:


#Here 
#On
#is
#Hitters data analysis


# In[44]:


#Pulling the names of the players
Hitting_2011_Players = SNHU_2011[3].Player.str.split(',', expand = True)


# In[63]:


#Seperating Games played and games started
GP_GS = SNHU_2011[3]['GP-GS'].str.split('-', expand = True)
GP_GS = GP_GS.astype({0:'float'})
GP_GS = GP_GS.astype({1:'float'})


# In[73]:


#Creating a dictonary for key stats
Dictionary = {'Player' : Hitting_2011_Players[2] + ' ' + Hitting_2011_Players[0],
              'Games Played': GP_GS[0],
              'Games Started' : GP_GS[1],
              'Starting Percentage': GP_GS[1]/GP_GS[0],
                    'BA': SNHU_2011[3].AVG,
                     'OPS':SNHU_2011[3].OPS,
                     'BB': SNHU_2011[3].HBP,
                     'AB': SNHU_2011[3].AB,
                     'Hits':SNHU_2011[3].H,
                     'BB': SNHU_2011[3].BB}


# In[74]:


#Dataframe for hitting Statistics
Frame = pd.DataFrame(Dictionary)


# In[91]:


#Seaborn Settings 
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set(color_codes = True)


# In[94]:


#Normal Distribution Model 
sns.distplot(Frame['Starting Percentage'])
plt.title('Playing Time Distribution')
plt.xlabel('Standard Deviations')
sns.set_style('ticks')
plt.show()

