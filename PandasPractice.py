#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dict1={
    "Name":["Bishal","Bibek","Bsal"],
    "Class":[15,10,20],
    "city":["Pokhara","Pkr","Georgia"]
}


# In[3]:


dictmade=pd.DataFrame(dict1)


# In[4]:


dictmade


# In[5]:


dictmade.to_csv('students.csv')


# In[6]:


dictmade.describe()


# In[7]:


pd.read_csv('students.csv')


# In[8]:


dictmade.index=['first','second','third']


# In[9]:


dictmade


# In[10]:


ser=pd.Series(np.random.rand(10))


# In[11]:


ser


# In[12]:


type(ser)


# In[13]:


newdf=pd.DataFrame(np.random.rand(62,5),index=np.arange(62))


# In[14]:


newdf


# In[15]:


newdf[0][1]=62


# In[16]:


newdf.head()


# In[17]:


newdf.describe()


# In[18]:


newdf.tail()


# In[19]:


newdf.index


# In[20]:


newdf.T


# In[21]:


newdf.sort_index(axis=0,ascending=False)


# In[22]:


newdf.sort_index(axis=1,ascending=False)


# In[23]:


newdf.drop([1],axis=0)


# In[24]:


newdf.drop([1],axis=0)


# In[25]:


newdf.drop([0],axis=1)


# In[32]:


newdf.loc[:,[1]]=21


# In[33]:


newdf


# In[34]:


newdf.drop([1])


# In[ ]:




