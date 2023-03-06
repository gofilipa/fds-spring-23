#!/usr/bin/env python
# coding: utf-8

# # homework 3: text cleaning

# Please download this page by pressing the download button on upper right corner. You should save the page as an `.ipynb` file. 
# 
# Afer downloading the document, open it on your own computer, either on Google Colab or Jupyter-Notebooks. If using Google Colab, you may need to first upload the document to your Google Drive before you can work on it.
# 
# When you are finished, download the document as an `.ipynb` file and submit it through Blackboard. 

# For this assignment, you will choose a text that you've read/seen before, maybe from the Project Gutenburg library. Then, in the cells below, you will load up your text into a Jupyter notebook or Google Colab notebook. 

# In[1]:


# First, import the libraries we need to analyze text (nltk) and get 
# data over URLs (urllib)


# In[2]:


# Then, grab the URL of your text from Gutenberg (or elsewhere) and 
# save it to a variable called "my_url" 


# In[3]:


# open the URL address with urlopen(my_url) and save it to "opened_url"


# In[4]:


# read the data in the URL using read() and save it to "raw" 


# In[5]:


# our data is currently in byte type, so we need to convert it to a 
# string type using decode(). Save the result to "decoded"


# Next we will tokenize the text, then remove the front & back matter

# In[6]:


# Use NLTK "word_tokenize" method to create a list of "tokens,"
# or smaller strings, from our long string above


# In[7]:


# check the first ten words from our list of tokens


# In[8]:


# find where the first word of the text begins, this is the index


# In[9]:


# using the index, create a slice that excludes the frontmatter


# Complete the loop below to remove punctuation and capital leters. Make sure you save the cleaned text to a new variable.

# In[10]:


# fill in the missing code at the comment, then run the cell. 

no_punct = []
# write the first line of the for loop here
  if word.isalpha():
    no_punct.append(word.lower())


# In[ ]:


# fill in the missing code at the comment, then run the cell.

stops = stopwords.words('english')

o_unstopped = []
for t in o_text:
    if # complete the if statment here
        o_unstopped.append(t)


# Bonus: 
# Combine all of the cleaning steps (removing stopwords, punctuation, capital letters) within a single function called "clean" which you can then call on the text. 

# In[ ]:




