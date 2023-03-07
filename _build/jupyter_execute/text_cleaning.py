#!/usr/bin/env python
# coding: utf-8

# # NLTK part two: loading and cleaning texts

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


type(raw)


# In[6]:


# our data is currently in byte type, and we want to convert 
# it to a string

decoded = raw.decode()


# In[7]:


# now we have a string type data -- which is necessary for analysis
type(decoded)


# In[8]:


# let's check out what we have in 'decoded'

decoded


# ## tokenizing the text

# In[9]:


# we use the NLTK "word_tokenize" method to create a list of "tokens,"
# or smaller strings, from our long string above

tokens = nltk.word_tokenize(decoded)


# In[10]:


# check the first ten words from our list of tokens

tokens[:10]


# ## removing frontmatter and backmatter

# In[11]:


# find where the first word of the text begins
# use the index() method

tokens.index("TRAGEDY")


# In[12]:


# the text begins at the 164th word

tokens[164]


# In[13]:


# create a slice that excludes the frontmatter

tokens_no_frontmatter = tokens[164:]


# In[14]:


tokens_no_frontmatter[:10]


# In[15]:


# very complicated process of finding and removing backmatter

tokens_no_backmatter = tokens_no_frontmatter[:-3246]


# In[16]:


# changing the name to "shakes" for convenience

shakes = tokens_no_backmatter


# In[17]:


shakes[:10]


# In[18]:


# use the count() method to find the number of times a word appears in the text

shakes.count("Love")


# In[19]:


# the word counts are different depending on captialization

shakes.count("love")


# In[20]:


# we also see this with "ROMEO" vs "Romeo"

shakes.count('ROMEO')


# In[21]:


shakes.count('Romeo')


# In[22]:


# To make the word counts more accurate, we will convert all words to lowercase
# we will also remove punctuation

shakes_no_punct_lower = []

for word in shakes:
    if word.isalpha():
        shakes_no_punct_lower.append(word.lower())


# In[23]:


shakes_no_punct_lower[:10]


# In[24]:


# now we have regularized the text, so the word counts are more trustworthy

shakes_no_punct_lower.count('romeo')


# ## 1) what is data?
# Information gathered and collected, used for counting and other math
# Facts and statistics to back up truth
# Qualitative -- not just numbers
# Collection of information
# 
# ## 2) who controls data? 
# Humans, AI, Organizations.
# Government.
# 
# ##  3) what do the people who control data do with it?
