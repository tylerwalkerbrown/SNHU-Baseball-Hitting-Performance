#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


import matplotlib


# In[4]:


# Import the os module
import os

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))


# In[5]:


#Changing directory
os.chdir('C:/Users/Tyler/Desktop/SNHU')


# In[7]:


#Exporting the data to an excel file
#export.to_excel('SNHU_Pitching.xlsx' ,index = False)


# In[9]:


SNHU_2022 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2022', header = 0)


# In[10]:


export = pd.DataFrame(SNHU_2022[1])


# In[11]:


#Scrap Code
#'Team Faced':SNHU_2011[6].Opponent,
   #                        'SNHU Runs': Runs[0],
    #                       'Opps Runs': Runs[1],
     #                      'Ks': SNHU_2011[6].K,


# In[12]:


Runs = SNHU_2022[6]['Score'].str.split('-', expand = True)


# In[13]:


Abs = pd.Series(SNHU_2022[3].AVG)


# In[14]:


#Time Series Batting Averages Dictionaries
SNHU_Schedule_Dictionary = {'Date': SNHU_2022[6].Date,
                           'Overall BA': SNHU_2022[6].H.cumsum()/ SNHU_2022[6].AB.cumsum()
                           }
Cum_Avg ={
    'Date': SNHU_2022[6].Date,
    'Game to Game BA': SNHU_2022[6].AVG    
    }                    


# In[15]:


#Frames for averages 
overall = pd.DataFrame(SNHU_Schedule_Dictionary)
cumulative = pd.DataFrame(Cum_Avg)


# In[16]:


#Batting Average Pivot Table
BA_table = pd.pivot_table(data=cumulative,index='Date',values='Game to Game BA',aggfunc=np.sum)


# In[17]:


Cum_Avg_table = pd.pivot_table(data=overall,index='Date',values='Overall BA',aggfunc=np.sum)


# In[18]:


overall.plot(grid = True)
cumulative.plot(grid = True)
plt.xlabel('Number of Games')
plt.ylabel('Batting Average')
plt.legend()


# In[19]:


#Creating a dataframe for the schedule dictionary 
Schedule = pd.DataFrame(SNHU_Schedule_Dictionary)


# In[42]:


Schedule


# In[39]:


Schedule.index = pd.to_datetime(Schedule.index)


# In[45]:


#Line Plot
Schedule['Overall BA'].plot(grid = True)
cumulative.plot(grid = True)
plt.title('GBG BA')
plt.xlabel('Number of Games')
plt.ylabel('Batting Average')
plt.legend()


# In[121]:


#SPlitting names
Hitting_2022_Players = SNHU_2022[0].Player.str.split(',', expand = True)


# In[122]:


#Seperating Games played and games started
GP_GS = SNHU_2022[0]['GP-GS'].str.split('-', expand = True)
GP_GS = GP_GS.astype({0:'float'})
GP_GS = GP_GS.astype({1:'float'})


# In[166]:


#Creating a dictonary for key stats
Dictionary = {'Player' : Hitting_2022_Players[2] + ' ' + Hitting_2022_Players[0],
              'Games Played': GP_GS[0],
                    'BA': SNHU_2022[0].AVG,
                     'OPS':SNHU_2022[0].OPS,
                     'HBP': SNHU_2022[0].HBP,
                     'AB': SNHU_2022[0].AB,
                     'Hits':SNHU_2022[0].H,
                     'BB': SNHU_2022[0].BB,
                     'Double':SNHU_2022[0]['2B'] ,
                     'Triple':SNHU_2022[0]['3B'] ,
                     'HR':SNHU_2022[0].HR,
                     'SF': SNHU_2022[0].SF}


# In[167]:


#Dataframe for hitting Statistics
Frame = pd.DataFrame(Dictionary)
Frame = Frame.dropna()


# In[168]:


#wOBA statistic added to frame
Frame['wOBA'] = ((Frame['BB'] * .69) + (Frame['HBP'] * .72) + (Frame['Hits'] - Frame['Double'] - Frame['Triple'] - Frame['HR'])  +(Frame['Double']*1.27) + (Frame['Triple']*1.62) + (Frame['HR']))/(Frame['AB'] + Frame['BB'] + Frame['SF'] + Frame['HBP'])


# In[171]:


#Plus 30 ABs 
Plus_30_AB = Frame.loc[Frame['AB'] > 30]


# In[161]:


#Dataframe for hitting Statistics
Frame = pd.DataFrame(Dictionary)


# In[162]:


#Seaborn Settings 
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set(color_codes = True)


# In[177]:


#Normal Distribution Model 
sns.distplot(Frame['wOBA'])
sns.distplot(Plus_30_AB['wOBA'])
plt.legend(labels=["Total","30 Plus ABs"])
plt.show()


# In[54]:


Bar = {
    'Player' :  SNHU_2022[0].Player,
    'BA' : SNHU_2022[6].H.cumsum()/ SNHU_2022[6].AB.cumsum()
}


# In[55]:


Bar_Frame = pd.DataFrame(Bar)


# In[56]:


#Names for general averages
Names = SNHU_2022[0].Player.str.split(',', expand = True)


# In[57]:


n = pd.DataFrame(Names)
a = pd.DataFrame(SNHU_2022[0])


# In[58]:


#Dictionary for general averages
General_Avgs = {
    'Player':n[2] + ' ' + n[0],
    'BA': a['AVG']
}


# In[59]:


b = pd.DataFrame(General_Avgs)


# In[69]:


Pivot_table = pd.pivot_table(data=b,index='Player',values='BA',aggfunc=np.sum)
Pivot = Pivot_table[Pivot_table['BA']<.500]


# In[71]:


#Bar Chart Showing Averages
plt.bar(Pivot.index,Pivot['BA'])

#xticks 
plt.xticks(rotation=70) 

#x-axis labels 
plt.xlabel('Player') 

#y-axis labels 
plt.ylabel('Batting Average') 

#plot title 
plt.title('Averages Across Team') 


# In[ ]:




