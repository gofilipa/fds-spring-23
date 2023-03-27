#!/usr/bin/env python
# coding: utf-8

# # NLTK: nltk.book

# In[1]:


# importing the NLTK library so we can do text analysis

import nltk


# In[2]:


# importing a dataset of "books" to get started with text analysis

from nltk.book import *


# In[3]:


# using the method "concordance" to get a view of the contexts surrounding a given word

text5.concordance("man")


# In[4]:


# checking the concordance for 'woman'

text5.concordance("woman")


# In[5]:


# using the 'similar' method to check for words that have common contexts

text5.similar("man")


# In[6]:


text5.similar("woman")


# In[7]:


# the word 'ugly' has a common context with the word 'woman'

text5.concordance('ugly')


# In[8]:


# using the 'dispersion_plot' method to see where words 
# appear across the text

text3.dispersion_plot(['good', 'evil', 'serpent', 'Adam', 'Eve'])


# In[ ]:




