#!/usr/bin/env python
# coding: utf-8

# # Data Types and Variables

# ## Python as a calculator
# You can use Python to make calculations like addition, subtraction, multiplication, and division.

# In[1]:


1 + 1


# In[2]:


3 * 4


# In[3]:


21 / 7


# In[4]:


10 - 9


# ## Data Types
# Python interprets all data as a type of data. For example, a number is interpreted as an "integer," and any characters contained within quotes are interpreted as a "string." 

# In[5]:


type(1)


# In[6]:


type('hello world!')


# In[7]:


type("1")


# In[8]:


type(1)


# In[9]:


type(1.)


# In[10]:


type(True)


# In[11]:


type(False)


# In[12]:


type(['sausage', 'egg', 'cheese'])


# In[13]:


type([1, 4, 2])


# ## Variables
# Python saves data as "variables," which are a kind of label that we can assign to values like integers, strings, or lists.

# In[14]:


x = 5


# In[15]:


x


# In[16]:


y = 10


# In[17]:


y


# In[18]:


x + 5


# In[19]:


x


# In[20]:


x = "Hello"


# In[21]:


x


# In[22]:


y = " Goodbye"


# In[23]:


y


# In[24]:


x + y 


# In[25]:


breakfast = ['kiwis', 'yogurt', 'peanut butter sandwish', 'water']


# In[26]:


breakfast


# In[27]:


type(breakfast)


# In[28]:


number = 1000


# In[29]:


number


# ## Rules for creating variables

# In[30]:


# variables can start with an underscore or an alphabetic character.  
_5 = "five"


# In[31]:


# variables are case sensitive
my_variable = "test"
My_variable = "test again"


# In[32]:


My_variable


# In[33]:


my_variable


# In[34]:


# generally variables cannot start with punctuation
$varialbe = "dollar"


# ## Objects
# Every time you save some data to a variable, you are creating an "object" in python. 

# In[6]:


# this creates a string type object
greeting = "Hello World!"


# In[7]:


greeting


# ## Methods for Objects
# Objects have built-in functionality based on their data type, like strings and lists. In other words, you can do certain things to string-type objects that you cannot with list-type objects.

# In[8]:


# certain methods, like upper(), can be used to do things to strings
greeting.upper()


# In[ ]:


# lower() is another string method
greeting.lower()


# In[ ]:


greeting


# In[ ]:


breakfast


# In[ ]:


# there are also methods for lists, like sort()
breakfast.sort()


# In[ ]:


breakfast


# In[9]:


greeting.sort()


# In[ ]:


# string concatenation is when you add two strings together
"Hello" + "goodbye"


# In[ ]:


# f-string formatting is when you use an "f" and curly brackets {} 
# to tell python that you are going to put code in the string

f"Today for breafast, I ate {breakfast}"


# ## Homework help

# In[ ]:


name = "Filipa"


# In[ ]:


age = 33


# In[ ]:


f"my name is {name}, and my age is {age}"

