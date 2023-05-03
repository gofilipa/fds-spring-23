#!/usr/bin/env python
# coding: utf-8

# 
# # transformers: generating language

# 

# ## importing necessary libraries

# In[1]:


# import the transformers library, along with the pipeline and set_seed functions
# import the datasets library, along with the load_dataset function

get_ipython().system('pip install transformers')
get_ipython().system('pip install datasets')
from datasets import load_dataset
import transformers
from transformers import pipeline, set_seed


# ## loading and saving the dataset

# In[2]:


# loads the dataset from here: https://huggingface.co/datasets/allenai/real-toxicity-prompts'
# & checking the dataset object

dataset = load_dataset("allenai/real-toxicity-prompts") 


# In[3]:


# taking a peek at our dataset object - a dict (dictionary) type

dataset


# In[4]:


# how to access items within a dict (dictionary) type of object

dataset['train']['prompt'][0]


# In[5]:


# let's count how many rows there are in the 'prompt' column

len(dataset['train']['prompt'])


# In[6]:


# creates a list of prompts containing input and output pairs

prompts = []

for item in dataset['train']:
  if item['prompt']['toxicity'] == None:
    pass
  elif item['prompt']['toxicity'] > .7:
    input = item['prompt']['text']
    output = item['continuation']['text']
    input_output = input, output
    prompts.append(input_output)
  else: 
    pass


# In[7]:


len(prompts)


# In[8]:


# check out the first ten items from our new list

prompts[:10]


# In[9]:


# prints just the first item from the list, both input and output

prompts[0]


# In[10]:


# prints first item (the input) from the first input_output pair

prompts[0][0]


# In[11]:


# prints second item (the output) from the first input_output pair

prompts[0][1]


# In[12]:


# show us a list of the input prompts with their corresponding index number
# this number will be useful later when we want to pick specific prompts
# to feed into the generator

print('list of prompts: ')
print('\n')

for (index, item) in enumerate(prompts[:10]):
  print(f'number', index, 'in the list:')
  print(item[0])
  print('\n')


# ## using the text generation model

# In[13]:


# creating a text generator from the pipeline function
# first one is gpt-2, the default. Read more here: 

gpt2 = pipeline('text-generation')


# In[14]:


gpt2(prompts[0][0],
     max_length = 50)


# In[15]:


# let's compare the generated result with the actual continuation

prompts[0][1]


# In[16]:


# the second one is bloom, read more here: https://huggingface.co/bigscience/bloom-560m 
bloom = pipeline('text-generation', model='bigscience/bloom-560m')


# In[ ]:


# feed the same prompt from above into the bloom model

bloom(prompts[0][0],
     max_length = 50)


# ## generating multiple prompts at once

# In[ ]:


# testing out the generator function on the first three items in our prompts list
# here we use an advanced syntax called "list indexing"

gpt2([item[0] for item in prompts[:3]],
     max_length=50)


# In[ ]:


# testing out the generator function on one chosed item in our prompts list
# use the correct index number (scroll up to see the numbered list) to identify
# your chosen prompt

gpt2(prompts[4][0], max_length=50)


# In[ ]:


bloom(prompts[4][0], max_length=50)


# In[ ]:




