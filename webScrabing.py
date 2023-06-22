#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy  as np
import requests
from bs4 import BeautifulSoup


# In[2]:


from bs4 import BeautifulSoup
import requests 
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"


# In[3]:


web = requests.get(url)
sup = BeautifulSoup(web.text, "html.parser")


# In[24]:


netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close","Volume"])

netflix_data


# In[ ]:





# In[25]:


for row in sup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
       # netflix_data = netflix_data.append({, ignore_index=True)
    newData = pd.DataFrame({"Date":[date], "Open":[Open], "High":[high], "Low":[low], "Close":[close], "Adj Close":[adj_close], "Volume":[volume]})
    netflix_data = pd.concat([netflix_data,newData])
    
netflix_data


# In[26]:


read_html_pandas_data = pd.read_html(url)


# In[27]:


read_html_pandas_data[0]


# Our output is correct
