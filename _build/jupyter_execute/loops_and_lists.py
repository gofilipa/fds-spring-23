#!/usr/bin/env python
# coding: utf-8

# # Loops and Lists

# In[1]:


# remember lists? Let's make a list of breakfast items

breakfast = ["nuts", "sausage", "hash browns", "fruit snacks"]


# In[2]:


# syntax for a loop includes two lines
# the first line identifies the variable name (for each item)
# and the name of the list (or string) that we want to loop over
# the second line instructs the loop what to do to each item

for item in breakfast:
    print(item)


# In[3]:


# we can also loop through strings

for letter in "Hello":
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


# In[ ]:




