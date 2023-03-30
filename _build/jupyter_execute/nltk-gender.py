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

orl = clean(orlando)


# In[6]:


frank = clean(frankenstein)


# In[7]:


print(frank)


# ## NLTK methods for text analysis

# In[8]:


# turn our saved text (list of strings) to an NLTK object for 
# text analysis

frank = nltk.Text(frank)


# In[9]:


# checks the most common words

frank.vocab().most_common(20)


# In[10]:


# load up and clean a text by a man for comparison 

drac = clean(dracula)


# In[11]:


print(drac)


# In[12]:


drac = nltk.Text(drac)

drac.vocab().most_common(20)


# In[13]:


# question: how does each text portray the monster characters?

drac.similar('monster')


# In[14]:


frank.similar('monster')


# In[15]:


drac.count("monster")


# In[16]:


frank.count("monster")


# In[17]:


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

# In[ ]:


orlando.count("woman")


# In[ ]:


orlando.count("man")


# In[ ]:


text = clean(dracula)


# In[ ]:


dracula = nltk.Text(text)


# In[ ]:


dracula.similar('woman')


# ## group challenge: monsters
# 
# Compare and contrast the monsters from Frankenstein and Dracula. One possibility is to compare the main characters from each text.
# 
# After cleaning your text, use NLTK methods like: 
# - `concordance()`
# - `dispersion_plot([])`
# - `collocations()`
# - `common_contexts([])`
# - most common words: `text.vocab().most_common(20)`
# 
# Explore the different ways that monster is being portrayed across Dracula and Frankenstein. What words are associated with each one? Try using words like “Dracula” “Vampire” and “Murderer”, or other words that seem appropriate to your analysis

# In[16]:


drac.concordance("monster")


# In[17]:


frank.concordance("monster")


# In[ ]:


# for frankenstein, words like "miserable", "fear", "solitude" appear in context with "monster"
# for dracula, words like "destroy", "terrible", "threw", "shouted" appear in context with "monster"

# these resulst suggest that Dracula was much less sympathetic than Frankenstein. 
# we sort of pity Frankenstein, while we fear Dracula. 


# In[20]:


# dispersion plot of the words "child", "scream", and "hide"

frank.dispersion_plot(["child", "scream", "hide"])


# In[ ]:


# compared to frankenstein, dracula has more instances of "scream" and "hide". This suggests
# that the monster in dracula is more terrifying than the monster in frankenstein.

# the graph also shows more instances of "child" in the middle and end of the novel. Maybe there's 
# a loss of innocence "child" in frankenstein, but not in dracula. To find out, we would look at 
# the context of the word "child" across the novels.
 
drac.dispersion_plot(["child", "scream", "hide"])


# In[22]:


# checking words similar to "child" in frankenstein and dracula

frank.similar('child')


# In[23]:


drac.similar('child')


# In[24]:


# checking the context of "child" in frankenstein and dracula

drac.concordance('child')


# In[25]:


frank.concordance('child')


# In[ ]:




