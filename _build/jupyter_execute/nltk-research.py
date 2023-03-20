#!/usr/bin/env python
# coding: utf-8

# # NLTK research questions

# In[1]:


# On Jupyter - run this cell
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# In[2]:


# on Colab -- run this cell
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')


# ## nltk personals corpus

# In[3]:


# import our list of books from the NLTK library

from nltk.book import *


# In[4]:


# check out text8, the personals ads, first 20 words

text8[:20]


# In[5]:


# how to find the length of the dataset, use len()

len(text8)


# In[6]:


# check the most frequent words, using nltk method "Frequency 
# Distribution", that measures word frequencies

# first import the FreqDist class
from nltk import FreqDist

# then check the most common 15 words
FreqDist(text8).most_common(15)


# In[7]:


# notice that the text is not cleaned, since it's counting
# punctuation and stopwords. 
# We need to write a loop that remove stopwords and punctuation 

stops = stopwords.words('english')

personals_clean = [] # creating an empty list, to put new words in

for word in text8: # picking out each word in text8
    if word.isalpha(): # checking if that word is in the alphabet
        if word not in stops: # checking if that word is in stops
             personals_clean.append(word.lower()) # adding to our list


# In[8]:


# check the first 20 words -- we have a cleaner dataset now

personals_clean[:20]


# In[9]:


# create a frequency distribution, the results are much better 
# than before

FreqDist(personals_clean).most_common(15)


# In[10]:


# let's try some nltk methods that we know, like dispersion_plot(), 
# similar(), concordance()

# In order to use those methods, we first create an NLTK object
# for our text

personals = nltk.Text(personals_clean)


# In[11]:


# check similar words for our top word in the FreqDist, 'lady'

personals.similar('lady')


# In[12]:


# create a concordance for 'lady'

personals.concordance('lady')


# In[13]:


# dispersion_plot() checks where certain words appear

personals.dispersion_plot(['lady', 'male', 'fun'])


# In[14]:


# collocations() checks words that frequently go together

personals.collocations()


# In[15]:


# common_contexts([]) checks the immediate words (context) surrounding
# our target word

personals.common_contexts(['lady'])


# ## patterns and research questions

# What patterns do you see emerging from your exploration? Use methods like: similar(), concordance(), collocations(), dispersion_plot(), common_contexts()
# 
# Results:
# - adjectives like 'slim', 'fun' are more common than 'classy'
# - seems like it's more men seeking out women, 'common_contexts'
