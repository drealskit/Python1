#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


car = pd.read_csv(r"C:\Users\CAREW\Downloads\2. Cars Data1.csv")


# In[3]:


car.head()


# In[4]:


car.shape


# In[7]:


#car.isnull()
car.isnull().sum() #finding null values


# In[8]:


new_car = car.dropna()


# In[9]:


new_car.shape #null roles dropped 


# In[10]:


#check what are the different types of make are there in our dataset. and count of them 
new_car['Make'].value_counts()


# In[15]:


#show all the recprs where origin is asia or europe 
new_car[new_car['Origin'].isin(['Asia', 'Europe'])]


# In[17]:


#Remove all the records (rows) where weight is above 4000
new_car.head(2)


# In[19]:


new_car[~(new_car['Weight'] > 4000)]


# In[20]:


426-103


# In[21]:


#Increase all the values of MPG_City column by 3
new_car.head(2)


# In[23]:


new_car['MPG_City'] = new_car['MPG_City'].apply(lambda x:x+3)
new_car


# In[ ]:




