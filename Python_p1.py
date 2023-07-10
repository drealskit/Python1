#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd 


# In[19]:


data = pd.read_csv(r"C:\Users\CAREW\Downloads\Weather_Data.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.shape


# In[6]:


data.index


# In[7]:


data.columns


# In[8]:


data.dtypes


# In[9]:


data['Weather'].unique()


# In[10]:


data.nunique()


# In[11]:


data.count()


# In[12]:


data['Weather'].value_counts()


# In[13]:


data.info()


# In[4]:


#Q1 Find all the unique wind speed values in the data
data.head(2)


# In[5]:


data['Wind Speed_km/h'].nunique()


# In[6]:


data['Wind Speed_km/h'].unique() #answer to question 1


# In[7]:


#q2 find the number of times when the weather is exactly clear
#using value_counts
data.Weather.value_counts()


# In[8]:


#answer using filtering 
#data.head(2)
#data.Weather == 'Clear' #will show in boolean, we have to put into another df to show number
data[data.Weather == 'Clear']


# In[9]:


#using group by
data.groupby("Weather").get_group('Clear')


# In[10]:


#Q3 Find the number of times when the wind speed was exactly 4km/h
data[data['Wind Speed_km/h'] == 4]


# In[12]:


data.isnull().sum()
#showing sum of all null rows to be zero


# In[13]:


#or
data.notnull().sum()


# In[16]:


#q5 rename the column name Weather of the datafrane to "Weather Conditions"
#data.rename(columns = {'Weather' : 'Weather Conditions'}) #temp rename, we have to use inplace to permanently change it 
data.rename(columns = {'Weather' : 'Weather Conditions'} , inplace = True) 


# In[17]:


data.head()


# In[20]:


#Whats the mean visibility
data.Visibility_km.mean()


# In[21]:


#Whats the standard deviation of pressure in this dat
data.Press_kPa.std()


# In[22]:


#Whats the variance of relative humidity in this data
data['Rel Hum_%'].var() #because there is space betweeen the name of the column


# In[24]:


#Find all the instances when Snow was recorded
#value_counts
#data.head(2)
data['Weather'].value_counts()  answer is #390


# In[25]:


#answer via filtering 
data[data['Weather'] == 'Snow']


# In[28]:


#str.constains to find any item with snow
data[data['Weather'].str.contains('Snow')].tail(50)


# In[30]:


#Find all instance when wind speed is above 24 and visibility is 25
data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# In[32]:


#What is the mean value of each column against each weather 
data.groupby('Weather').mean()


# In[33]:


#Whats the minimum and maximum value of each column against each weather 
data.groupby('Weather').min()


# In[34]:


data.groupby('Weather').max()


# In[35]:


#Show all the records where the weather is fog 
data[data['Weather'] == 'Fog']


# In[38]:


#Find all instances when weather is clear or visbility is above 40
data[(data['Weather'] == 'Clear') | (data['Visibility_km'] > 40)].head(50)


# In[42]:


#Find all instance when weather is clear and relative humidity is > 50 | Visibility is above 40
data[(data['Weather'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]


# In[ ]:




