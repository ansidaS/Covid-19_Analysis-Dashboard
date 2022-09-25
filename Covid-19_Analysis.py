#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime


# In[3]:


covid = pd.read_csv('C:\\Users\\arunc\\Desktop\\data cleaning\\covid_19_data.csv')


# In[4]:


covid.head()


# In[5]:


covid.tail()


# In[6]:


covid.info()


# In[7]:


covid.drop('SNo',axis=1,inplace=True)


# In[8]:


covid['ObservationDate'] = pd.to_datetime(covid['ObservationDate'])


# In[12]:


covid.info()


# In[10]:


covid.head()


# In[11]:


covid = covid.set_index('ObservationDate')


# In[13]:


datewise_covid = covid.groupby(['ObservationDate']).agg({'Confirmed': 'sum','Deaths':'sum','Recovered':'sum'})


# In[14]:


datewise_covid.head()


# In[15]:


sns.set_style('darkgrid')
plt.figure(figsize=(15,12))
sns.barplot(x = datewise_covid.index.date,y = datewise_covid['Confirmed'],palette='YlOrRd')
plt.xticks(rotation=90)
plt.title('Datewise Confirmed Cases')


# In[16]:


#A mortality rate is a measure of the frequency of occurrence of death in a defined population during a specified interval.
datewise_covid['Mortality Rate'] = (datewise_covid['Deaths']/datewise_covid['Confirmed'])*100


# In[17]:


datewise_covid.head()


# In[18]:


plt.figure(figsize=(12,6))
plt.plot(datewise_covid['Mortality Rate'],label="Mortality Rate")
#plt.xticks(rotation=90)
plt.show()


# In[19]:


India_data = covid[covid['Country/Region']=='India']


# In[20]:


datewise_india = India_data.groupby(['ObservationDate']).agg({'Confirmed': 'sum','Deaths':'sum','Recovered':'sum'})


# In[21]:


datewise_india.head()


# In[22]:


datewise_india['Mortality Rate'] = (datewise_india['Deaths']/datewise_india['Confirmed'])*100


# In[23]:


plt.figure(figsize=(12,6))
plt.plot(datewise_india['Mortality Rate'],label="Mortality Rate")
plt.xticks(fontsize=18)
plt.show()


# In[24]:


datewise_india['Recovery Rate'] = (datewise_india['Recovered']/datewise_india['Confirmed'])*100


# In[25]:


plt.figure(figsize=(12,6))
plt.plot(datewise_india['Mortality Rate'],label="Mortality Rate")
plt.xticks(fontsize=18)
plt.show()


# In[26]:


datewise_india['Recovery Rate'] = (datewise_india['Recovered']/datewise_india['Confirmed'])*100


# In[27]:


plt.figure(figsize=(12,6))
plt.plot(datewise_india['Recovery Rate'],label="Recovery Rate")
plt.xticks(fontsize=18)
plt.show()


# In[28]:


plt.figure(figsize=(12,6))
datewise_india['Confirmed'].diff().plot()


# In[29]:


plt.figure(figsize=(12,6))
datewise_india['Recovered'].diff().plot()


# In[30]:


plt.figure(figsize=(12,6))
datewise_india['Mortality Rate'].diff().plot()


# In[31]:


plt.figure(figsize=(12,6))
datewise_india['Recovery Rate'].diff().plot()


# In[ ]:




