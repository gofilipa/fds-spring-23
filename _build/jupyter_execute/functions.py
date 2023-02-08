#!/usr/bin/env python
# coding: utf-8

# # Functions
# A function is a way to do something to data in python. It takes some data (as the "input"), does something to that data, and then returns the result (the "output"). 

# ## Defining and calling a function
# You need to first
#  define the function, then you can call it. 

# In[1]:


# define a function that adds two numbers together

def multiply():
    print(2 * 2)



# In[2]:


# call the function

multiply()


# ## Passing data into a function
# We can tell python to run the function on any data that we want. This is called "passing" the data into the function. Data that passes into the function is also known as the "parameter" "argument" or "input."

# In[3]:


def multiply_with_input(a, b):
    print(a * b)


# In[4]:


multiply_with_input(98, 10100)


# In[5]:


# write 2 separate functions for adding and subtracting two numbers. 

def subtraction(a, b):
    print(a - b)

subtraction(8, 4)


# In[6]:


# write a function that prints a personalized greeting,
# according to the name in the function call.
# hint: use what you know about f-strings.








# In[7]:


def greeting(a):
    print(f"Hello, {a}, nice to see you!")


# In[8]:


greeting("Beyonce")


# In[ ]:




