#!/usr/bin/env python
# coding: utf-8

# # NLTK: cleaning part two

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


# ## text8: the personals corpus

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
FreqDist(text8).most_common(20)


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

FreqDist(personals_clean).most_common(20)


# In[10]:


# right now, our data is in a list

type(personals_clean)


# In[11]:


# let's try some nltk methods that we know, like dispersion_plot(), 
# similar(), concordance()

# In order to use those methods, we first create an NLTK object
# for our text

personals = nltk.Text(personals_clean)


# In[12]:


# now we have an nltk.text.Text type of object, which is good

type(personals)


# In[13]:


# check similar words for our top word in the FreqDist, 'lady'

personals.similar('lady')


# In[14]:


# create a concordance for 'lady'

personals.concordance('lady')


# In[15]:


# dispersion_plot() checks where certain words appear

personals.dispersion_plot(['lady', 'male', 'fun'])


# In[16]:


# collocations() checks words that frequently go together

personals.collocations()


# In[17]:


# common_contexts([]) checks the immediate words (context) surrounding
# our target word

personals.common_contexts(['lady'])


# ## patterns and research questions

# What patterns do you see emerging from your exploration? Use methods like: similar(), concordance(), collocations(), dispersion_plot(), common_contexts()
# 
# Results:
# - adjectives like 'slim', 'fun' are more common than 'classy'
# - seems like it's more men seeking out women, 'common_contexts'

# ## text5: the chat corpus

# In[18]:


# we are going to check out text5, the chat corpus


# In[19]:


# creating a slice to take a peek at the data

text5[:10]


# In[20]:


# checking the end of the data

text5[-20:]


# In[21]:


# making a Frequency Distribution to see most common words

FreqDist(text5).most_common(20)


# In[22]:


# it seems like there's a lot of stopwords and punctuation here, which we
# want to clean


# In[23]:


# function for cleaning the text

def clean(text):
    stops = stopwords.words('english') # creating a list of stopwords
    clean = [] # creating an empty list, to put new words in

    for word in text: # picking out each word in text5
        if word.isalpha(): # checking if in alphabet
            if word not in stops: # checking if stopword
                clean.append(word.lower()) # adding to list
    return clean


# In[24]:


# calling the function

cleaned = clean(text5)


# In[25]:


# we can see that the stopwords, punctuation, and uppercase letters have been removed

cleaned[:10]


# In[26]:


cleaned[-20:]


# In[27]:


# now our frequency distribution is more informative
# though it's still not a very rich dataset

FreqDist(cleaned).most_common(20)


# In[28]:


text.similar('lmao')


# In[52]:


text.concordance('lmao')


# ## Group challenge
# Choose one text from the nltk.book list. Use `from nltk.book import *` to call up the list.
# Then, using NLTK methods we know, like similar(), concordance(), distribution_plot([]), do some analysis on these lists. 
# 
# What patterns do you see emerging from your exploration? Be ready to share with the class.

# In[59]:


text2


# In[60]:


# one of the words in the title is associated with a character, 'Marianne'

text2.similar('sense')


# In[61]:


text2.similar('sensibility')


# In[ ]:




