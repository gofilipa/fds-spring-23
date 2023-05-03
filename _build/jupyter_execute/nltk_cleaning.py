#!/usr/bin/env python
# coding: utf-8

# # NLTK: cleaning part one

# In[1]:


# import the libraries we need to analyze text (nltk) and get data
# over URLs (urllib)

import nltk
from nltk.corpus import stopwords
# for google colab: nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
# for google colab: nltk.download('wordnet')
# for google colab: nltk.download('omw-1.4')
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
# it first to a string, then to a list of strings

decoded = raw.decode()


# In[7]:


# now we have a string type data
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


# In[11]:


# we have finished converting the data into a list format
# which means we are ready to start cleaning the data

type(tokens)


# ## removing frontmatter and backmatter
# note: this section will not be included in the midterm

# In[12]:


# find where the first word of the text begins
# use the index() method

tokens.index("TRAGEDY")


# In[13]:


# the text begins at the 164th word

tokens[164]


# In[14]:


# create a slice that excludes the frontmatter

tokens_no_frontmatter = tokens[164:]


# In[15]:


tokens_no_frontmatter[:10]


# In[16]:


# to remove the backmatter, we want to create a list slice
# that slices off the last 3246 words

tokens_no_backmatter = tokens_no_frontmatter[:-3246]


# In[17]:


# changing the name to "shakes" for convenience

shakes = tokens_no_backmatter


# In[18]:


# checking the first 10 words

shakes[:10]


# In[19]:


# checking the last 10 words

shakes[-10:]


# ## cleaning capital letters and punctuation

# In[20]:


# the capital forms of words ("love" vs "Love") will make our 
# word counts inaccurate

# to check this, use the count() method to find the number of 
# times a word appears in the text

shakes.count("Love")


# In[21]:


# the word counts are different depending on lower vs upper case

shakes.count("love")


# In[22]:


# we also see this with "ROMEO" vs "Romeo"

shakes.count('ROMEO')


# In[23]:


shakes.count('Romeo')


# In[24]:


# To make the word counts more accurate, we will convert all words to 
# lowercase, we will also remove punctuation

# here, we write a loop that contains a conditional statement
# the conditional statement will filter out words that don't have 
# letters (punctuation)

# in the final line of the loop, we add our filtered word to 
# the new list, and make it lowercase

shakes_no_punct_lower = []

for word in shakes:
    if word.isalpha():
        shakes_no_punct_lower.append(word.lower())


# In[25]:


# check the first ten lines of our new list

shakes_no_punct_lower[:10]


# In[26]:


# now we have regularized the text, so the word counts are more 
# reflective of the actual words rather than their format

shakes_no_punct_lower.count('romeo')


# # removing 'stopwords'
# Next, we want to remove words that occur too often in our text,
# like "a" "the" "so" "is", etc. 
# These words are too frequent and they will mess up our word counts.

# In[27]:


# what are the most common words in the text?
# we can use NLTK's FreqDist to find out.

from nltk import FreqDist
FreqDist(shakes_no_punct_lower).most_common(10)


# In[28]:


# to remove stopwords, first create a list of stopwords, 
# which we will later want to remove from our text

stops = stopwords.words('english')


# In[31]:


# check out the first 20 words in the list

stops[:20]


# In[34]:


# Now, we create a loop that checks if the words in our no punctuation 
# and lowecased list is a stopword.
# if the word is a stopword, we do not add it to the new list.

shakes_no_stops = []

for item in shakes_no_punct_lower:
    # this line checks if the current word is not in our stopwords list
    if item not in stops:
        # if it is not in the stopwords list, we add it the new one
        shakes_no_stops.append(item)


# In[35]:


# see that there are no stopwords in the new list

shakes_no_stops[:10]


# In[37]:


# so what are the most common words now?
# the results are much better!

FreqDist(shakes_no_stops).most_common(10)


# # lemmatizing
# Lemmatizing is the process of getting a root from the word. This is another thing we want to make sure that our data is as regularized and simplified as possible.

# In[39]:


# first, create the lemmatizer variable which links to the function

wordnet_lemmatizer = WordNetLemmatizer()
# for google colab: wordnet_lemmatizer = nltk.stem.WordNetLemmatizer() 


# In[40]:


# the lemmatizer simplies words to their root form

wordnet_lemmatizer.lemmatize("children")


# In[41]:


# geese becomes goose

wordnet_lemmatizer.lemmatize("geese")


# In[42]:


# families becomes family

wordnet_lemmatizer.lemmatize("families")


# In[43]:


# now, we can write a loop that lemmatizes all of the words
# in our text

shakes_lemmatized = []

for word in shakes_no_stops:
    # we create the "lemma" variable to store the lemmatized word
    lemma = wordnet_lemmatizer.lemmatize(word)
    # we add that word to our new list
    shakes_lemmatized.append(lemma)


# In[47]:


# let's check the new list

shakes_lemmatized[:10]


# # ready for analysis!

# In[48]:


# Congratulations!
# we have removed punctuation and stopwords
# and we have transformed word forms to lowercase
# and to singular forms.


# In[50]:


# Now, turn the text into a nltk.Text type object. 

shakes = nltk.Text(shakes_lemmatized)


# In[51]:


# now we can run methods like "similar()" and "concordance()"
shakes.similar("love")


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
