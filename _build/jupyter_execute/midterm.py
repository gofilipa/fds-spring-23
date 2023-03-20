#!/usr/bin/env python
# coding: utf-8

# # Midterm

# ## Section 1: Python Basics

# In[1]:


quote = ["Imma", "let", "you", "finish", "but", "Beyonce", "had", 
         "the", "best", "video", "of", "all", "time"]


# In[2]:


## Question 1:

# Take the above list called "quote", and write a loop below to print out each word from 
# the from the list, one by one. 


# In[3]:


## Question 2:

# In your own words below, explain how a loop works. What is each line of code 
# doing? 1 - 2 sentences. 


# In[4]:


## Question 3: 

# From the above quote, print out the first word using list indexing. 


# In[ ]:





# In[5]:


## Question 4:

# From the above quote, print out the first 4 words using list slicing. 


# In[ ]:





# In[6]:


## Question 5:

# From the above quote, print out the last word using list indexing. 


# In[ ]:





# ## text cleaning

# In[7]:


# for all computers: run this cell to import our libraries we will need for text cleaning

import nltk
from urllib.request import urlopen 
from nltk.corpus import stopwords


# In[8]:


# for Jupyter-Notebooks ONLY: run this cell

from nltk.stem import WordNetLemmatizer


# In[9]:


# for Google Colab ONLY: run this cell

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nlkt.download('punkt')


# In[ ]:


# then, run this cell to load up and format the text, which is "Frankenstein"

my_url = 'https://www.gutenberg.org/cache/epub/84/pg84.txt'
opened_url = urlopen(my_url)
raw = opened_url.read()
decoded = raw.decode()
tokens = nltk.word_tokenize(decoded)


# In[ ]:


# then, run this cell to check the first ten words "tokens"

tokens[:10]


# In[ ]:


## Question 6:

# Explain what the above code is doing in your own words, 1-2 sentences. 


# In[ ]:


frank_no_punct_lower = [] # creating an empty list, to put new words in

for word in tokens: # picking out each word in list of tokens
    if word.isalpha(): # checking if that word is in the alphabet
        frank_no_punct_lower.append(word.lower())


# In[ ]:


## Question 7:

# Explain in your own words what the loop is doing in the last
# line. 1 - 2 sentences.


# In[ ]:


# run this cell to load our list of stopwords

stops = stopwords.words('english')


# In[ ]:


# run this cell to remove stopwords

frank_no_stops = []

for item in frank_no_punct_lower:
    if item not in stops:
        frank_no_stops.append(item)


# In[ ]:


## Question 8: 

# Explain in your own words why we would want to remove stopwords from our text. How
# might they affect our analysis of word frequencies in the text? 1 - 2 sentences.


# In[ ]:


# FOR JUPYTER ONLY:
# run this cell to create the lemmatizer variable for our next loop

wordnet_lemmatizer = WordNetLemmatizer()


# In[ ]:


# FOR COLAB ONLY:
# run this cell to create the lemmatizer variable for our next loop


wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()


# In[ ]:


frank_lemmatized = []

for word in frank_no_stops: # picking out each word in our list of words without stopwords
    lemma = wordnet_lemmatizer.lemmatize(word) 
    frank_lemmatized.append(lemma)


# In[ ]:


## Question 8:

# Explain in your own words what the loop is doing on each line. I did the first line for you.
# 1 sentence per line.


# ## Bonus questions

# In[ ]:


# first, run this cell to create an NLTK type object from our current text, so we can analyze it.

text = nltk.Text(frank_no_stops)


# In[ ]:


# then, run this cell to see the 20 most common words from the cleaned text

text.vocab().most_common(20)


# In[ ]:


# BONUS QUESTION # 1:
# use the NLTK method .similar() on one of the words from the above list


# In[ ]:


# BONUS QUESTION # 2:
# use the NLTK method .condordance() on the word "monster"


# In[ ]:


# BONUS QUESTION # 3:
# use the NLTK method .dispersion_plot() on two or more words of your choosing from
# the results so far.


# In[ ]:


# BONUS QUESTION # 4:
# Based on the results of the above analysis, what do you find interesting about this 
# text? What do you think the most common words in the text are telling us about the 
# text? Feel free to take a guess here, and follow your curiosity. 2 - 3 sentences.


# 
