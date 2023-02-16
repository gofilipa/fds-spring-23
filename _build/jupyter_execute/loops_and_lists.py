#!/usr/bin/env python
# coding: utf-8

# # Loops and Lists

# In[1]:


# remember lists? Let's make a list of breakfast items

breakfast = ["bread", "butter", "bec", "banana"]


# In[2]:


# syntax for a loop includes two lines
# the first line identifies the variable name (for each item)
# and the name of the list (or string) that we want to loop over
# the second line instructs the loop what to do to each item

for item in breakfast:
    print(item)


# In[3]:


# we can also loop through strings

for letter in "Hello world!":
    print(letter)


# In[4]:


# it doesn't matter what we name the variable, as long as we
# are consistent in calling the same variable in the body 
# of the loop

sentence = ["this", "is", "a", "sentence"]

for letter in sentence:
    print(letter)


# In[5]:


# print out the phrase: [item] is my favorite breakfast!

for item in breakfast:
    print(f"{item} is my favorite breakfast!") 
    


# ## Group challenge: 

# In[6]:


# Write some code to print out the square of each of
# these numbers:

# you want the output to print as a string, like so:
# "The square of 2 is 4."
# "The square of 3 is 9."

prime_numbers = [2, 3, 5, 7, 11]

for item in prime_numbers:
    print(f"The sqaure of {item} is {item*item}")

# Hint: Remember that the square of a number is that number 
# times itself. Remember how to use "f-strings".


# ## Lists

# In[7]:


movies = ["Avatar", "Nope", "Up", "The Cat in the Hat", "The Incredibles"]


# In[8]:


len(movies)


# In[9]:


len(breakfast)


# In[10]:


# for reference, these are functions we already have been using:

print()
len()
type()
# this is a method, not a function: breakfast.upper()


# In[17]:


movies = ["Avatar", "Nope", "Up", "The Cat in the Hat", "The Incredibles"]
movies_length = len(movies)
print(movies_length)


# In[22]:


# this does the same thing as the code above, but less readable (imo)
print(len(movies))


# In[2]:


# list indexing
movies = ["Avatar", "Nope", "Up", "The Cat in the Hat", "The Incredibles"]

movies[0]


# In[3]:


movies[1]


# In[23]:


movies[3]


# In[24]:


movies[-1]


# In[25]:


movies[-3]


# In[26]:


movies[-5]


# In[27]:


# common error with list indexing is going too far, out of the range of the list.

movies[-6]


# In[4]:


movies = ["Avatar", "Nope", "Up", "The Cat in the Hat", "The Incredibles"]

movies[1:3]


# In[9]:


# in a list slice, the first term is inclusive
# and the second term is exclusive

movies[2:5]


# In[12]:


# this also works with strings

"hello-world"[2:6]


# In[18]:


# the colon takes everything to the left or the right, depending on where the colon is placed
movies[:3]


# In[19]:


movies[3:]


# ## Group challenge 
# Create a new list of books, with at least 5 books in your
# list. Make sure the total number of books in the list is an odd
# number.
# How do you print out the book in the middle of the list?
# 
# What about the three books in the middle? Remember that the
# first value in a slice is inclusive, and the final value is
# exclusive.
# 

# In[20]:


# first create a list
books = ["harry potter", "jane eyre", "percy jackson", "social credit", "hands-on python"]


# In[22]:


# grabs the third item (which is set to #2 on the list)
books[2]


# In[23]:


# takes a slice of the middle three items, from 1 to 3 (doesn't include 4). 
books[1:4]


# In[ ]:




