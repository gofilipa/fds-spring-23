#!/usr/bin/env python
# coding: utf-8

# # NLTK and gender

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
    stops = stopwords.words('english')
    open_url = urlopen(url)
    read_text = open_url.read()
    decoded_text = read_text.decode()
    tokens = nltk.word_tokenize(decoded_text)
    
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


text = clean(orlando)


# In[6]:


print(text)


# ## NLTK methods for tex analysis

# In[7]:


text = nltk.Text(text)


# In[8]:


text.vocab().most_common(20)


# In[ ]:




