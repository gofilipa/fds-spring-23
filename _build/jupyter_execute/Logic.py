#!/usr/bin/env python
# coding: utf-8

# # Logic

# In[1]:


# remember booleans?

type(True)


# In[2]:


type(False)


# In[3]:


# double equals sign checks for equavalence

1 == 1


# In[4]:


1 == 0 


# In[5]:


10 > 5


# In[6]:


# single equals sign makes an assignment

variable = 'my variable'


# In[7]:


# double equals sign checks for an equivalence

variable == 'hello'


# In[8]:


age = 17
if age > 24:
    print("You can rent a car")
elif age > 20: 
    print("You can have a beer")
    print("You can also play poker")
elif age > 17:
    print("You can vote")
elif age > 16:
    print("You can build your credit")
else:
    print("You're too young")


# In[9]:


show = 'the last of us'
if show == 'spongebob':
    print('you have the wrong show')
elif show == 'survivor':
    print('you have the correct show')
else:
    print("I don't know what show you're talking about... I'm just a little program")


# In[ ]:




