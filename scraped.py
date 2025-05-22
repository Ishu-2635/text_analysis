#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os, sys
from bs4 import BeautifulSoup
import requests
import time


# In[10]:


data = pd.read_excel('C://Users//Abhi//Desktop//stats and ml//data set-20230603T103433Z-001//Input.xlsx', names=[0,1])
data


# In[11]:


data.describe()


# In[4]:


url_id = data.iloc[:, 0].tolist()
url = data.iloc[:, 1].tolist()
print(url_id)
print(url)


# In[12]:


for i in url:
    response=requests.get(url[i]).text
    #print(i)
    


# In[13]:


for i in range(len(url)):
    response=requests.get(url[i]).text
    #print(response)
    


# In[23]:


print(response)


# In[14]:


import nltk 
import re


# In[15]:


if len(url_id) == len(url):
    for (url_var, url_content) in zip(url_id, url):
        webp = requests.get(url_content).text
        soup = BeautifulSoup(webp, 'lxml')

        try:
            title = soup.find_all('h1')[0].text
        except IndexError:
            title = ''

        try:
            content = soup.findAll('div', {'class': 'td-post-content tagdiv-type'})[0].text
        except IndexError:
            content = ''

        review = title.strip() + "\n" 
        review += "\n" + content.strip()
        review = review.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        review = re.sub(r'[^a-zA-Z.]', ' ', review)
        review = review.lower()
        review = review.split()
        review = "  ".join(review)

        with open(f'{url_var}.txt', 'w') as file:
            file.write(review)
            file.write("\n\n")  # You can add newlines between titles and content for better readability
        time.sleep(1)
else:
    print("url_id and url lists must have the same length.")


# In[ ]:




