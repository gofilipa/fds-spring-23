#!/usr/bin/env python
# coding: utf-8

# # NLTK part two: loading texts

# In[1]:


# import the libraries we need to analyze text (nltk) and get data
# over URLs (urllib)

import nltk
from urllib.request import urlopen 


# ## loading up the text

# In[2]:


# grabs URL and saves it to a variable

my_url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'


# In[3]:


# opens the URL address

opened_url = urlopen(my_url)


# In[4]:


# read the data in the URL

raw = opened_url.read()


# In[5]:


# our data is currently in byte type, and we want to convert 
# it to a string

decoded = raw.decode()


# In[6]:


# now we have a string type data -- which is necessary for analysis
type(decoded)


# In[7]:


# let's check out what we have in 'decoded'

decoded


# ## tokenizing the text

# In[8]:


# we use the NLTK "word_tokenize" method to create a list of "tokens,"
# or smaller strings, from our long string above

tokens = nltk.word_tokenize(decoded)


# In[9]:


# check the first ten words from our list of tokens

tokens[:10]


# ## removing frontmatter and backmatter

# In[10]:


# find where the first word of the text begins

tokens.index("TRAGEDY")


# In[11]:


# the text begins at the 164th word

tokens[164]


# In[12]:


# create a slice that excludes the frontmatter

tokens_no_frontmatter = tokens[164:]


# In[13]:


tokens_no_frontmatter[:10]


# In[ ]:




