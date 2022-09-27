#!/usr/bin/env python
# coding: utf-8

# In[1]:


import shutil


# In[2]:


shutil.unpack_archive('unzip_me_for_instructions.zip','final_unzip','zip')


# In[4]:


with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)


# In[5]:


import re


# In[6]:


pattern = r'(\d{3})-(\d{3})-(\d{4})'


# In[7]:


def search(file,pattern=r'(\d{3})-(\d{3})-(\d{4})'):
    f=open(file,'r')
    text=f.read()
    
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ''


# In[8]:


import os


# In[9]:


results = []


# In[11]:


for folder,sub_folders,files in os.walk(os.getcwd()+'\\extracted_content'):
    
    for f in files:
        full_path = folder+'\\'+f
        
        results.append(search(full_path))


# In[12]:


for r in results:
    if r!='':
        print(r.group())


# In[ ]:




