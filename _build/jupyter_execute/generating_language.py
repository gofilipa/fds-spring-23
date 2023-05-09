#!/usr/bin/env python
# coding: utf-8

# 
# # transformers: generating language

# ## importing necessary libraries

# In[1]:


# import the transformers library, along with the pipeline and set_seed functions
# import the datasets library, along with the load_dataset function

get_ipython().system('pip install transformers')
get_ipython().system('pip install datasets')
from datasets import load_dataset
import transformers
from transformers import pipeline, set_seed


# ## loading and slicing the dataset

# In[2]:


# loads the dataset from here: https://huggingface.co/datasets/allenai/real-toxicity-prompts'
# & checking the dataset object

dataset_toxicity = load_dataset("allenai/real-toxicity-prompts") 


# In[3]:


# OPTIONAL:

# code that splits a long string into individual items in a list, 
# separated by periods (into sentences)

dataset_creative = 'The studio was filled with the rich odour of roses, and when the light summer wind stirred amidst the trees of the garden, there came through the open door the heavy scent of the lilac, or the more delicate perfume of the pink-flowering thorn. From the corner of the divan of Persian saddle-bags on which he was lying, smoking, as was his custom, innumerable cigarettes, Lord Henry Wotton could just catch the gleam of the honey-sweet and honey-coloured blossoms of a laburnum, whose tremulous branches seemed hardly able to bear the burden of a beauty so flamelike as theirs; and now and then the fantastic shadows of birds in flight flitted across the long tussore-silk curtains that were stretched in front of the huge window, producing a kind of momentary Japanese effect, and making him think of those pallid, jade-faced painters of Tokyo who, through the medium of an art that is necessarily immobile, seek to convey the sense of swiftness and motion. The sullen murmur of the bees shouldering their way through the long unmown grass, or circling with monotonous insistence round the dusty gilt horns of the straggling woodbine, seemed to make the stillness more oppressive. The dim roar of London was like the bourdon note of a distant organ.'

sentences = dataset_creative.split('.')

sentences[0]


# In[4]:


len(sentences)


# In[5]:


# taking a peek at our dataset object - a dict (dictionary) type

dataset_toxicity


# In[6]:


# how to access items within a dict (dictionary) type of object

dataset_toxicity['train']['prompt'][0]


# In[7]:


# let's count how many rows there are in the 'prompt' column

len(dataset_toxicity['train']['prompt'])


# In[8]:


# creates a list of prompts containing input and output pairs

prompts = []

for item in dataset_toxicity['train']:
  if item['prompt']['toxicity'] == None:
    pass
  elif item['prompt']['toxicity'] > .5:
    input = item['prompt']['text']
    output = item['continuation']['text']
    input_output = input, output
    prompts.append(input_output)
  else: 
    pass


# In[9]:


# checking the first item in our new list

prompts[0]


# In[10]:


# creates a list of prompts containing input and output pairs

flirty = []

for item in dataset_toxicity['train']:
  # alter the label to your chosen label, like "flirtation"
  if item['prompt']['flirtation'] == None:
    pass
  # can change the options here to filter different labels
  # for example, change 'toxicity' to 'flirtation'
  # or change the .5 to .7 for more 'toxic' results
  elif item['prompt']['flirtation'] > .7:
    input = item['prompt']['text']
    output = item['continuation']['text']
    input_output = input, output
    # make sure you change the list name to the right variable
    flirty.append(input_output)
  else: 
    pass


# In[11]:


flirty[0]


# In[12]:


len(flirty)


# In[13]:


len(prompts)


# In[14]:


# check out the first ten items from our new list

prompts[:10]


# In[15]:


# prints just the first item from the list, both input and output

prompts[0]


# In[16]:


# prints first item (the input) from the first input_output pair

prompts[0][0]


# In[17]:


# prints second item (the output) from the first input_output pair

prompts[0][1]


# In[18]:


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

# In[19]:


# creating a text generator from the pipeline function
# first one is gpt-2, the default. Read more here: 

gpt2 = pipeline('text-generation')


# In[20]:


# feed the first half of the first prompt

gpt2(prompts[0][0], max_length = 50)


# In[21]:


# you can add the 'num_return_sequences' to increase the number of results

gpt2(sentences[0], max_length=100, num_return_sequences=3)


# ## Comparing prompts to original 'continuation'

# In[22]:


# let's compare the generated result with the actual continuation
# to access the second half of the prompt, use [1] index

# first prompt, second half
prompts[0][1]


# In[23]:


# second prompt, second half
prompts[1][1]


# ## generating multiple prompts at once

# In[24]:


# testing out the generator function on the first three items in our prompts list
# here we use an advanced syntax called "list indexing"

gpt2([item[0] for item in prompts[:10]],
     max_length=50)


# In[ ]:


# testing out the generator function on one chosed item in our prompts list
# use the correct index number (scroll up to see the numbered list) to identify
# your chosen prompt

gpt2(prompts[4][0], max_length=50)

