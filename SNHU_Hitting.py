#!/usr/bin/env python
# coding: utf-8

# In[93]:


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
import matplotlib
import os
#Supervised learning
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


# In[153]:


#Plot styles 
plt.style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (13,9)


# In[107]:


# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))


# In[108]:


SNHU_2022 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2022', header = 0)
SNHU_2021 = pd.read_html('https://snhupenmen.com/sports/baseball/stats/2021', header = 0)


# In[109]:


#Game by game table
GBG = SNHU_2022[6]
GBG2021 = SNHU_2021[6]


# In[110]:


#Splitting the scores into a seperate table
Runs = SNHU_2022[6]['Score'].str.split('-', expand = True)
Runs21 = SNHU_2021[6]['Score'].str.split('-', expand = True)


# In[111]:


#Adding the Runs to the game to game 
GBG[['SNHU','OPP']] = Runs
GBG2021[['SNHU','OPP']] = Runs21


# In[112]:


#Dropping Score column after adding indvidual scores 
GBG = GBG.drop(['Score'], axis = 1)
GBG2021 = GBG2021.drop(['Score'], axis = 1)


# In[129]:


#Time Series Batting Averages Dictionaries
SNHU_Schedule_Dictionary = {'Date': SNHU_2022[6].Date,
                           'Cumulative BA': SNHU_2022[6].H.cumsum()/ SNHU_2022[6].AB.cumsum(),
                            'Game to Game BA' : SNHU_2022[6].H/SNHU_2022[6].AB,
                            'Game to Game wOBA': ((GBG['BB'] * .69) + (GBG['HBP'] * .72) + 
                                                  (GBG['H'] - GBG['2B'] - GBG['3B'] - GBG['HR'])  +
                                                  (GBG['2B']*1.27) + (GBG['3B']*1.62) + (GBG['HR']))/
                                                    (GBG['AB'] + GBG['BB'] + GBG['SF'] + GBG['HBP']),
                            
                            'Cumulative wOBA': ((GBG['BB'] * .69).cumsum() + (GBG['HBP'] * .72).cumsum() + 
                                                (GBG['H'].cumsum() - GBG['2B'].cumsum() - GBG['3B'].cumsum() - GBG['HR'].cumsum())  +
                                                (GBG['2B']*1.27).cumsum() + (GBG['3B']*1.62).cumsum() + 
                                                (GBG['HR']).cumsum())/(GBG['AB'].cumsum()+ GBG['BB'].cumsum() + GBG['SF'].cumsum() + GBG['HBP'].cumsum())
                           }
Cum_Avg ={
    'Date': SNHU_2022[6].Date,
    'Game to Game BA': SNHU_2022[6].AVG    
    }                 


# In[130]:


#Frames for averages 
overall = pd.DataFrame(SNHU_Schedule_Dictionary)
cumulative = pd.DataFrame(Cum_Avg)


# In[155]:


#Plotting the cumulative batting average with the game by game
overall.plot()
plt.title('Hitting Performance Game over Game')
plt.axvline(x=45, color = 'Black', label = 'End of Reg. Season')
plt.legend()


# In[117]:


#Creating a dataframe for the schedule dictionary 
Schedule = pd.DataFrame(SNHU_Schedule_Dictionary)


# In[85]:


#Converting the schedule dates to datetimes
Schedule.index = pd.to_datetime(Schedule.index)


# In[86]:


#SPlitting names
Hitting_2022_Players = SNHU_2022[0].Player.str.split(',', expand = True)


# In[87]:


#Seperating Games played and games started
GP_GS = SNHU_2022[0]['GP-GS'].str.split('-', expand = True)
GP_GS = GP_GS.astype({0:'float'})
GP_GS = GP_GS.astype({1:'float'})


# In[88]:


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


# In[89]:


#Dataframe for hitting Statistics
Frame = pd.DataFrame(Dictionary)
Frame = Frame.dropna()
At_Bats = Frame[Frame['AB'] < 50].index


# In[90]:


#Dropping player with less than 50 ABS
Frame.drop(At_Bats, inplace = True)


# In[91]:


#wOBA statistic added to frame
Frame['wOBA'] = ((Frame['BB'] * .69) + (Frame['HBP'] * .72) + (Frame['Hits'] - Frame['Double'] - Frame['Triple'] - Frame['HR'])  +(Frame['Double']*1.27) + (Frame['Triple']*1.62) + (Frame['HR']))/(Frame['AB'] + Frame['BB'] + Frame['SF'] + Frame['HBP'])


# In[156]:


plt.barh(Frame.Player,Frame.wOBA, label = 'SNHU wOBAs')
plt.axvline(x=.320, color = 'red', label = 'Average wOBA')
plt.axvline(x=.370, color = 'Yellow', label = 'Great wOBA')
plt.axvline(x=.400, color = 'Green', label = 'Excellent wOBA')
plt.legend()
plt.title('SNHU 2022 wOBA')
plt.figure(figsize=(10, 10))
plt.show()


# In[134]:


######Start of k nearest/ test######

#Dropping the bottom totals by index
GBG=GBG.drop([GBG.index[51]])


# In[135]:


#Dropping 2021 index 37 NaN row
GBG2021=GBG2021.drop([GBG2021.index[37]])


# In[136]:


GBG_predict = GBG.drop(['Date', 'Loc','Opponent'], axis = 1)
GBG_predict21 = GBG2021.drop(['Date', 'Loc','Opponent'], axis = 1)


# In[137]:


#Target = result and stats = stats 
knn = KNeighborsClassifier(n_neighbors = 6)
result = GBG_predict['W/L'].values
stats = GBG_predict.drop(['W/L'], axis = 1).values


# In[139]:


#Fitting the data
knn.fit(stats,result)


# In[140]:


#Predict the labels for training set
predict = knn.predict(stats)


# In[141]:


#Dropping the W/L column and keeping all unlabled values
new = GBG_predict21.drop(['W/L'], axis =1).values


# In[149]:


#Predict and print label for the new data point
#new_predict = knn.predict(new)
#print("Prediction: {}".format(new))


# In[143]:


#Testing SNHU consistency 
knn.score(stats,result)


# In[144]:


#Splitting the dataset into test and train
X_train, X_test, y_train, y_test = train_test_split(stats,result, test_size = 0.2, random_state=42, stratify=result)


# In[145]:


#Testing the accuracy of train and test
print(knn.score(X_test, y_test))
print(knn.score(X_train, y_train))


# In[146]:


neighbors = np.arange(1, 12)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))


# In[147]:


for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)


# In[148]:


# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()


# In[ ]:


######Regression#######

