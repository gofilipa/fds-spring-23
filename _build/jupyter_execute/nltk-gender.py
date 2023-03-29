#!/usr/bin/env python
# coding: utf-8

# # NLTK: gender analysis

# In[1]:


# On Jupyter - run this cell
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from urllib.request import urlopen 


# In[2]:


# on Colab -- run this cell
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
from urllib.request import urlopen 


# ## selecting and cleaning our text

# In[3]:


def clean(url):
    # loads and tokenizes the text
    open_url = urlopen(url)
    read_text = open_url.read()
    decoded_text = read_text.decode()
    tokens = nltk.word_tokenize(decoded_text)
    
    # cleans the text
    stops = stopwords.words('english')
    text = [] 
    for word in tokens:
        if word.isalpha(): 
            if word not in stops:
                text.append(word.lower())     
    
    return text


# In[4]:


# books by women
frankenstein = 'https://www.gutenberg.org/cache/epub/84/pg84.txt'
little_women = 'https://www.gutenberg.org/cache/epub/37106/pg37106.txt'
pride_prejudice = 'https://www.gutenberg.org/cache/epub/1342/pg1342.txt'
orlando = 'http://gutenberg.net.au/ebooks02/0200331.txt'

# books by men
dracula = 'https://www.gutenberg.org/cache/epub/345/pg345.txt'
dorian_gray = 'https://www.gutenberg.org/cache/epub/174/pg174.txt'
crime_punishment = 'https://www.gutenberg.org/files/2554/2554-0.txt'
heart_darkness = 'https://www.gutenberg.org/files/219/219-0.txt'


# In[5]:


# running the "clean" function on the text "orlando"

text = clean(orlando)


# In[6]:


print(text)


# ## NLTK methods for text analysis

# In[7]:


# turn our saved text (list of strings) to an NLTK object for 
# text analysis

orlando = nltk.Text(text)


# In[8]:


# most common words

orlando.vocab().most_common(20)


# In[9]:


# load up and clean a text by a man for comparison 

dorian = clean(dorian_gray)


# In[10]:


print(dorian)


# In[11]:


dorian = nltk.Text(dorian)

dorian.vocab().most_common(20)


# In[12]:


# question: how does each text treat male and female characters?

orlando.similar('man')


# In[13]:


orlando.similar('woman')


# In[14]:


orlando.common_contexts(["woman"])


# ## group challenge

# Compare and contrast one text by a woman and one text by a man. One possibility is to compare the main characters from each text. Another possibility is to compare the genders of the main characters. Or you can explore themes, or settings from the text.
# 
# After cleaning your text, use NLTK methods like: 
# - `concordance()`
# - `dispersion_plot([])`
# - `collocations()`
# - `common_contexts([])`
# - most common words: `text.vocab().most_common(20)`
# 
# Try to answer the following questions:
# - What words are associated with "man" and "woman" from each text?
# - What are the differences between the genders?
# - What are the differences in gender portrayal between the male and female authors?

# Frankenstein: "man" vs "woman" 
# - with `similar()`, "man" has 14 words, and "woman" has 1. 
# - Means that men has more references than women text. Makes sense because it's about a male scientist creating a man. 

# In[15]:


orlando.count("woman")


# In[16]:


orlando.count("man")


# In[17]:


text = clean(dracula)


# In[18]:


dracula = nltk.Text(text)


# In[19]:


dracula.similar('woman')


# In[ ]:




