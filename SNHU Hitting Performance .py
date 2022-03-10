#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from lxml import html
from bs4 import BeautifulSoup
import pandas as pd
import csv 
import matplotlib.pyplot as plt 


# In[2]:


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


# In[3]:


#Hitting Format
Hitting2010 = SNHU_2010[0]
Hitting2010 =Hitting2010.drop(['Bio Link'],axis = 1)
Hitting2010 =Hitting2010.drop(['Player'],axis = 1)
Hitting2010 = Hitting2010.dropna()
#2011
Hitting2011 = SNHU_2011[0]
Hitting2011 =Hitting2011.drop(['Bio Link'],axis = 1)
Hitting2011 =Hitting2011.drop(['Player'],axis = 1)
Hitting2011 = Hitting2011.dropna()
#2012
Hitting2012 = SNHU_2012[0]
Hitting2012 =Hitting2012.drop(['Bio Link'],axis = 1)
Hitting2012 =Hitting2012.drop(['Player'],axis = 1)
Hitting2012 = Hitting2012.dropna()
#2013
Hitting2013 = SNHU_2013[0]
Hitting2013 =Hitting2013.drop(['Bio Link'],axis = 1)
Hitting2013 =Hitting2013.drop(['Player'],axis = 1)
Hitting2013 = Hitting2013.dropna()
#2014
Hitting2014 = SNHU_2014[0]
Hitting2014 =Hitting2014.drop(['Bio Link'],axis = 1)
Hitting2014 =Hitting2014.drop(['Player'],axis = 1)
Hitting2014 = Hitting2014.dropna()
#2015
Hitting2015 = SNHU_2015[0]
Hitting2015 =Hitting2015.drop(['Bio Link'],axis = 1)
Hitting2015 =Hitting2015.drop(['Player'],axis = 1)
Hitting2015= Hitting2015.dropna()
#2016
Hitting2016 = SNHU_2016[0]
Hitting2016 =Hitting2016.drop(['Bio Link'],axis = 1)
Hitting2016 =Hitting2016.drop(['Player'],axis = 1)
Hitting2016 = Hitting2016.dropna()
#2017
Hitting2017 = SNHU_2017[0]
Hitting2017 =Hitting2017.drop(['Bio Link'],axis = 1)
Hitting2017 =Hitting2017.drop(['Player'],axis = 1)
Hitting2017 = Hitting2017.dropna()
#2018
Hitting2018 = SNHU_2018[0]
Hitting2018 =Hitting2018.drop(['Bio Link'],axis = 1)
Hitting2018 =Hitting2018.drop(['Player'],axis = 1)
Hitting2018 = Hitting2018.dropna()
#2019
Hitting2019 = SNHU_2019[0]
Hitting2019 =Hitting2019.drop(['Bio Link'],axis = 1)
Hitting2019 =Hitting2019.drop(['Player'],axis = 1)
Hitting2019 = Hitting2019.dropna()
#2020
Hitting2020= SNHU_2020[0]
Hitting2020=Hitting2020.drop(['Bio Link'],axis = 1)
Hitting2020 =Hitting2020.drop(['Player'],axis = 1)
Hitting2020 = Hitting2020.dropna()
#2021
Hitting2021 = SNHU_2021[0]
Hitting2021 =Hitting2021.drop(['Bio Link'],axis = 1)
Hitting2021 =Hitting2021.drop(['Player'],axis = 1)
Hitting2021 = Hitting2021.dropna()
#2022
Hitting2022 = SNHU_2022[0]
Hitting2022 =Hitting2022.drop(['Bio Link'],axis = 1)
Hitting2022 =Hitting2022.drop(['Player'],axis = 1)
Hitting2022 = Hitting2022.dropna()


# In[4]:


#Hitting2010 wOBA/WRAA Model 
wBB = .69 * Hitting2010['BB']
wHBP = .72 * Hitting2010['HBP']
wSingle = .89 * (Hitting2010['H'] - Hitting2010['2B'] - Hitting2010['3B'] - Hitting2010['HR'])
wDouble = 1.27 * Hitting2010['2B']
wTriple = 1.62 * Hitting2010['3B']
wHR = 2.10 * Hitting2010['HR']
#Divided By
AB = Hitting2010['AB']
BB = Hitting2010['BB']
SF = Hitting2010['SF']
HBP = Hitting2010['HBP']
IBB = 0 
#Final wOBA
Hitting2010['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2010['wRAA'] = (((Hitting2010['wOBA']-.320)/1.209) * AB)
#Hitting2010



#Hitting2011 wOBA/WRAA Model 
wBB11 = .69 * Hitting2011['BB']
wHBP11 = .72 * Hitting2011['HBP']
wSingle11 = .89 * (Hitting2011['H'] - Hitting2011['2B'] - Hitting2011['3B'] - Hitting2011['HR'])
wDouble11 = 1.27 * Hitting2011['2B']
wTriple11 = 1.62 * Hitting2011['3B']
wHR11 = 2.10 * Hitting2011['HR']
#Divided By
AB11 = Hitting2011['AB']
BB11 = Hitting2011['BB']
SF11 = Hitting2011['SF']
HBP11 = Hitting2011['HBP']
IBB11 = 0 
#Final wOBA
Hitting2011['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2011['wRAA'] = (((Hitting2011['wOBA']-.320)/1.209) * AB)
#Hitting2011


#Hitting2012 wOBA/WRAA Model 
wBB12 = .69 * Hitting2012['BB']
wHBP12 = .72 * Hitting2012['HBP']
wSingle12 = .89 * (Hitting2012['H'] - Hitting2012['2B'] - Hitting2012['3B'] - Hitting2012['HR'])
wDouble12 = 1.27 * Hitting2012['2B']
wTriple12 = 1.62 * Hitting2012['3B']
wHR12 = 2.10 * Hitting2012['HR']
#Divided By
AB12 = Hitting2012['AB']
BB12 = Hitting2012['BB']
SF12 = Hitting2012['SF']
HBP12 = Hitting2012['HBP']
IBB12 = 0 
#Final wOBA
Hitting2012['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2012['wRAA'] = (((Hitting2012['wOBA']-.320)/1.209) * AB)
#Hitting2012


#Hitting2013 wOBA/WRAA Model 
wBB13 = .69 * Hitting2013['BB']
wHBP13 = .72 * Hitting2013['HBP']
wSingle13 = .89 * (Hitting2013['H'] - Hitting2013['2B'] - Hitting2013['3B'] - Hitting2013['HR'])
wDouble13 = 1.27 * Hitting2013['2B']
wTriple13 = 1.62 * Hitting2013['3B']
wHR13 = 2.10 * Hitting2013['HR']
#Divided By
AB13 = Hitting2013['AB']
BB13 = Hitting2013['BB']
SF13 = Hitting2013['SF']
HBP13 = Hitting2013['HBP']
IBB13 = 0 
#Final wOBA
Hitting2013['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2013['wRAA'] = (((Hitting2013['wOBA']-.320)/1.209) * AB)
#Hitting2013


#Hitting2014 wOBA/WRAA Model 
wBB14 = .69 * Hitting2014['BB']
wHBP14 = .72 * Hitting2014['HBP']
wSingle14 = .89 * (Hitting2014['H'] - Hitting2014['2B'] - Hitting2014['3B'] - Hitting2014['HR'])
wDouble14 = 1.27 * Hitting2014['2B']
wTriple14 = 1.62 * Hitting2014['3B']
wHR14 = 2.10 * Hitting2014['HR']
#Divided By
AB14 = Hitting2014['AB']
BB14 = Hitting2014['BB']
SF14 = Hitting2014['SF']
HBP14 = Hitting2014['HBP']
IBB14 = 0 
#Final wOBA
Hitting2014['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2014['wRAA'] = (((Hitting2014['wOBA']-.320)/1.209) * AB)
#Hitting2014


#Hitting2015 wOBA/WRAA Model 
wBB15 = .69 * Hitting2015['BB']
wHBP15 = .72 * Hitting2015['HBP']
wSingle15 = .89 * (Hitting2015['H'] - Hitting2015['2B'] - Hitting2015['3B'] - Hitting2015['HR'])
wDouble15 = 1.27 * Hitting2015['2B']
wTriple15 = 1.62 * Hitting2015['3B']
wHR15 = 2.10 * Hitting2015['HR']
#Divided By
AB15 = Hitting2015['AB']
BB15 = Hitting2015['BB']
SF15 = Hitting2015['SF']
HBP15 = Hitting2015['HBP']
IBB15 = 0 
#Final wOBA
Hitting2015['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2015['wRAA'] = (((Hitting2015['wOBA']-.320)/1.209) * AB)
#Hitting2015


#Hitting2016 wOBA/WRAA Model 
wBB16 = .69 * Hitting2016['BB']
wHBP16 = .72 * Hitting2016['HBP']
wSingle16 = .89 * (Hitting2016['H'] - Hitting2016['2B'] - Hitting2016['3B'] - Hitting2016['HR'])
wDouble16 = 1.27 * Hitting2016['2B']
wTriple16 = 1.62 * Hitting2016['3B']
wHR16 = 2.10 * Hitting2016['HR']
#Divided By
AB19 = Hitting2019['AB']
BB19 = Hitting2019['BB']
SF19 = Hitting2019['SF']
HBP19 = Hitting2019['HBP']
IBB19 = 0 
#Final wOBA
Hitting2016['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2016['wRAA'] = (((Hitting2016['wOBA']-.320)/1.209) * AB)
#Hitting2019


#Hitting2017 wOBA/WRAA Model 
wBB17 = .69 * Hitting2017['BB']
wHBP17 = .72 * Hitting2017['HBP']
wSingle17 = .89 * (Hitting2017['H'] - Hitting2017['2B'] - Hitting2017['3B'] - Hitting2017['HR'])
wDouble17 = 1.27 * Hitting2017['2B']
wTriple17 = 1.62 * Hitting2017['3B']
wHR17 = 2.10 * Hitting2017['HR']
#Divided By
AB17 = Hitting2017['AB']
BB17 = Hitting2017['BB']
SF17 = Hitting2017['SF']
HBP17 = Hitting2017['HBP']
IBB17 = 0 
#Final wOBA
Hitting2017['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2017['wRAA'] = (((Hitting2017['wOBA']-.320)/1.209) * AB)
#Hitting2017


#Hitting2018  wOBA/WRAA Model 
wBB18 = .69 * Hitting2018['BB']
wHBP18 = .72 * Hitting2018['HBP']
wSingle18 = .89 * (Hitting2018['H'] - Hitting2018['2B'] - Hitting2018['3B'] - Hitting2018['HR'])
wDouble18 = 1.27 * Hitting2018['2B']
wTriple18 = 1.62 * Hitting2018['3B']
wHR18 = 2.10 * Hitting2018['HR']
#Divided By
AB18 = Hitting2018['AB']
BB18 = Hitting2018['BB']
SF18 = Hitting2018['SF']
HBP18 = Hitting2018['HBP']
IBB11 = 0 
#Final wOBA
Hitting2018['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2018['wRAA'] = (((Hitting2018['wOBA']-.320)/1.209) * AB)
#Hitting2018


#Hitting2019 wOBA/WRAA Model 
wBB19 = .69 * Hitting2019['BB']
wHBP19 = .72 * Hitting2019['HBP']
wSingle19 = .89 * (Hitting2019['H'] - Hitting2019['2B'] - Hitting2019['3B'] - Hitting2019['HR'])
wDouble19 = 1.27 * Hitting2019['2B']
wTriple19 = 1.62 * Hitting2019['3B']
wHR19 = 2.10 * Hitting2019['HR']
#Divided By
AB19 = Hitting2019['AB']
BB19 = Hitting2019['BB']
SF19 = Hitting2019['SF']
HBP19 = Hitting2019['HBP']
IBB19 = 0 
#Final wOBA
Hitting2019['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2019['wRAA'] = (((Hitting2019['wOBA']-.320)/1.209) * AB)
#Hitting2011


#Hitting2020 wOBA/WRAA Model 
wBB20 = .69 * Hitting2011['BB']
wHBP20 = .72 * Hitting2011['HBP']
wSingle20 = .89 * (Hitting2020['H'] - Hitting2020['2B'] - Hitting2020['3B'] - Hitting2020['HR'])
wDouble20 = 1.27 * Hitting2020['2B']
wTriple20 = 1.62 * Hitting2020['3B']
wHR20 = 2.10 * Hitting2020['HR']
#Divided By
AB20 = Hitting2020['AB']
BB20 = Hitting2020['BB']
SF20 = Hitting2020['SF']
HBP20 = Hitting2020['HBP']
IBB20 = 0 
#Final wOBA
Hitting2020['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2020['wRAA'] = (((Hitting2011['wOBA']-.320)/1.209) * AB)
#Hitting2020


#Hitting2021 wOBA/WRAA Model 
wBB21 = .69 * Hitting2021['BB']
wHBP21 = .72 * Hitting2021['HBP']
wSingle21 = .89 * (Hitting2021['H'] - Hitting2021['2B'] - Hitting2021['3B'] - Hitting2021['HR'])
wDouble21 = 1.27 * Hitting2021['2B']
wTriple21 = 1.62 * Hitting2021['3B']
wHR21 = 2.10 * Hitting2021['HR']
#Divided By
AB21 = Hitting2021['AB']
BB21 = Hitting2021['BB']
SF21 = Hitting2021['SF']
HBP21 = Hitting2021['HBP']
IBB21 = 0 
#Final wOBA
Hitting2021['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2021['wRAA'] = (((Hitting2021['wOBA']-.320)/1.209) * AB)
#Hitting2021


#Hitting2022 wOBA/WRAA Model 
wBB22 = .69 * Hitting2022['BB']
wHBP22 = .72 * Hitting2022['HBP']
wSingle22 = .89 * (Hitting2022['H'] - Hitting2022['2B'] - Hitting2022['3B'] - Hitting2022['HR'])
wDouble22 = 1.27 * Hitting2022['2B']
wTriple22 = 1.62 * Hitting2022['3B']
wHR22 = 2.10 * Hitting2011['HR']
#Divided By
AB22 = Hitting2022['AB']
BB22 = Hitting2022['BB']
SF22 = Hitting2022['SF']
HBP22 = Hitting2022['HBP']
IBB22 = 0 
#Final wOBA
Hitting2022['wOBA'] = (wBB + wHBP + wSingle + wDouble + wTriple + wHR)/(AB + BB - IBB + SF + HBP)
#wRAA
Hitting2022['wRAA'] = (((Hitting2022['wOBA']-.320)/1.209) * AB)
#Hitting2022


# In[5]:


#Descriptive Statistics
print(Hitting2010.head())
print(Hitting2010.info())
print(Hitting2010.shape)
print(Hitting2010.describe())
#Parts of the Dataframe
print(Hitting2010.columns)
print(Hitting2010.index)


# In[6]:


#Data set with keys containing 2010-2022
All_years = pd.concat([Hitting2010,Hitting2011,Hitting2012,Hitting2013,Hitting2014,Hitting2015,Hitting2016,
                    Hitting2017, Hitting2018, Hitting2019,Hitting2020, Hitting2021, Hitting2022],
                       keys = ['Hitting2010','Hitting2011','Hitting2012','Hitting2013','Hitting2014','Hitting2015','Hitting2016',
                    'Hitting2017', 'Hitting2018', 'Hitting2019','Hitting2020', 'Hitting2021', 'Hitting2022'],
                      axis = 0)

All_No_Keys = pd.concat([Hitting2010,Hitting2011,Hitting2012,Hitting2013,Hitting2014,Hitting2015,Hitting2016,
                    Hitting2017, Hitting2018, Hitting2019,Hitting2020, Hitting2021, Hitting2022],
                                    axis = 0 )


# In[7]:


#BoxPlot Plus 20 at-bats
Plus20AB_10 = Hitting2010[Hitting2010['AB'] > 20]
Plus20AB_11 = Hitting2011[Hitting2011['AB'] > 20]
Plus20AB_12 = Hitting2012[Hitting2012['AB'] > 20]
Plus20AB_13 = Hitting2013[Hitting2013['AB'] > 20]
Plus20AB_14 = Hitting2014[Hitting2014['AB'] > 20]
Plus20AB_15 = Hitting2015[Hitting2015['AB'] > 20]
Plus20AB_16 = Hitting2016[Hitting2016['AB'] > 20]
Plus20AB_17 = Hitting2017[Hitting2017['AB'] > 20]
Plus20AB_18 = Hitting2018[Hitting2018['AB'] > 20]
Plus20AB_19 = Hitting2019[Hitting2019['AB'] > 20]
Plus20AB_20 = Hitting2020[Hitting2020['AB'] > 20]
Plus20AB_21 = Hitting2021[Hitting2021['AB'] > 20]
Plus20AB_22 = Hitting2022[Hitting2022['AB'] > 20]
Plus20AB_All = All_No_Keys[All_No_Keys['AB'] > 20]


# In[8]:


#Open dataframe for boxplot values of wOBA
BoxPlot = pd.DataFrame()


# In[9]:


#2010-2022 averages for wOBA box plot
BoxPlot['2010-2022'] = Plus20AB_All['wOBA']


# In[10]:


#Adding columns to Box plot for year to year wOBA comparisons
BoxPlot['2010'] = Plus20AB_10['wOBA']
BoxPlot['2011'] = Plus20AB_11['wOBA']
BoxPlot['2012'] = Plus20AB_12['wOBA']
BoxPlot['2013'] = Plus20AB_13['wOBA']
BoxPlot['2014'] = Plus20AB_14['wOBA']
BoxPlot['2015'] = Plus20AB_15['wOBA']
BoxPlot['2016'] = Plus20AB_16['wOBA']
BoxPlot['2017'] = Plus20AB_17['wOBA']
BoxPlot['2018'] = Plus20AB_18['wOBA']
BoxPlot['2019'] = Plus20AB_19['wOBA']
BoxPlot['2020'] = Plus20AB_20['wOBA']
BoxPlot['2021'] = Plus20AB_21['wOBA']
BoxPlot['2022'] = Plus20AB_22['wOBA']


# In[11]:


#SNHU Boxplot wOBA 2010- 2022
BoxPlot.plot(kind = "box", figsize = (16,6))
plt.title("2010 - 2022 wOBA")
plt.style.use("fivethirtyeight")


# In[12]:





# In[ ]:




