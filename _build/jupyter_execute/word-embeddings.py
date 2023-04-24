#!/usr/bin/env python
# coding: utf-8

# In[1]:


import gensim
from gensim.test.utils import common_texts
from gensim.models import Word2Vec


# In[2]:


model = Word2Vec(sentences=common_texts, vector_size=100, 
                 window=5, min_count=1, workers=4)


# In[3]:


woman_vector = model.wv['man'] 


# In[6]:


vector


# In[ ]:




