#!/usr/bin/env python
# coding: utf-8

# In[233]:


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
#Exporting dataset
import openpyxl as xls


# In[234]:


import matplotlib


# In[235]:


# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))


# In[236]:


#Changing directory
os.chdir('C:/Users/Tyler/Desktop/SNHU')


# In[237]:


#Exporting the data to an excel file
#Frame.to_excel('df.xlsx' ,index = False)


# In[239]:


SNHU_2022 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2022', header = 0)


# In[240]:


#Scrap Code
#'Team Faced':SNHU_2011[6].Opponent,
   #                        'SNHU Runs': Runs[0],
    #                       'Opps Runs': Runs[1],
     #                      'Ks': SNHU_2011[6].K,


# In[89]:


Runs = SNHU_2022[6]['Score'].str.split('-', expand = True)


# In[142]:


Abs = pd.Series(SNHU_2022[3].AVG)
Abs


# In[157]:


#Time Series Batting Averages Dictionaries
SNHU_Schedule_Dictionary = {'Date': SNHU_2022[6].Date,
                           'Overall BA': SNHU_2022[6].H.cumsum()/ SNHU_2022[6].AB.cumsum()
                           }
Cum_Avg ={
    'Date': SNHU_2022[6].Date,
    'Game to Game BA': SNHU_2022[6].AVG    
    }                    


# In[159]:


#Frames for averages 
overall = pd.DataFrame(SNHU_Schedule_Dictionary)
cumulative = pd.DataFrame(Cum_Avg)


# In[219]:


#Batting Average Pivot Table
BA_table = pd.pivot_table(data=cumulative,index='Date',values='Game to Game BA',aggfunc=np.sum)


# In[175]:


Cum_Avg_table = pd.pivot_table(data=overall,index='Date',values='Overall BA',aggfunc=np.sum)


# In[176]:


overall.plot(grid = True)
cumulative.plot(grid = True)
plt.title('Cumulative Batting Average')
plt.xlabel('Number of Games')
plt.ylabel('Batting Average')
plt.legend()


# In[148]:


#Creating a dataframe for the schedule dictionary 
Schedule = pd.DataFrame(SNHU_Schedule_Dictionary)


# In[149]:


Schedule.index = pd.to_datetime(Schedule.index)


# In[150]:


#Line Plot
Schedule['Game to Game BA'].plot(grid = True)
Schedule['Overall BA'].plot(grid = True)
plt.title('Cumulative Batting Average')
plt.xlabel('Number of Games')
plt.ylabel('Batting Average')
plt.legend()


# In[132]:


#SPlitting names
Hitting_2022_Players = SNHU_2022[3].Player.str.split(',', expand = True)


# In[133]:


#Seperating Games played and games started
GP_GS = SNHU_2022[3]['GP-GS'].str.split('-', expand = True)
GP_GS = GP_GS.astype({0:'float'})
GP_GS = GP_GS.astype({1:'float'})


# In[232]:


SNHU_2022[3]['GP-GS']


# In[229]:


#Creating a dictonary for key stats
Dictionary = {'Player' : Hitting_2022_Players[2] + ' ' + Hitting_2022_Players[0],
              'Games Played': GP_GS[0],
              'Games Started' : GP_GS[1],
              'Starting Percentage': GP_GS[1]/GP_GS[0],
                    'BA': SNHU_2022[3].AVG,
                     'OPS':SNHU_2022[3].OPS,
                     'BB': SNHU_2022[3].HBP,
                     'AB': SNHU_2022[3].AB,
                     'Hits':SNHU_2022[3].H,
                     'BB': SNHU_2022[3].BB}


# In[230]:


#Dataframe for hitting Statistics
Frame = pd.DataFrame(Dictionary)


# In[231]:


Frame


# In[137]:


#Seaborn Settings 
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set(color_codes = True)


# In[138]:


#Normal Distribution Model 
sns.distplot(Frame['Starting Percentage'])
plt.title('Playing Time Distribution')
plt.xlabel('Standard Deviations')
sns.set_style('ticks')
plt.show()


# In[243]:


#Dictionary for players batting averages over the games played
SNHU_2022[0]


# In[218]:


Bar = {
    'Player' :  SNHU_2022[0].Player,
    'BA' : SNHU_2022[6].H.cumsum()/ SNHU_2022[6].AB.cumsum()
}


# In[191]:


Bar_Frame = pd.DataFrame(Bar)


# In[246]:


#Names for general averages
Names = SNHU_2022[0].Player.str.split(',', expand = True)


# In[251]:


n = pd.DataFrame(Names)
a = pd.DataFrame(SNHU_2022[0])


# In[270]:


#Dictionary for general averages
General_Avgs = {
    'Player':n[2] + ' ' + n[0],
    'BA': a['AVG']
}


# In[272]:


b = pd.DataFrame(General_Avgs)


# In[273]:


Pivot_table = pd.pivot_table(data=b,index='Player',values='BA',aggfunc=np.sum)


# In[274]:


Pivot_table


# In[275]:


plt.bar(Pivot_table.index,Pivot_table['BA'])

#xticks 
plt.xticks(rotation=70) 

#x-axis labels 
plt.xlabel('Player') 

#y-axis labels 
plt.ylabel('Batting Average') 

#plot title 
plt.title('Averages Across Team') 


# In[ ]:




