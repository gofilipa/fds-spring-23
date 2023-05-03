#!/usr/bin/env python
# coding: utf-8

# # transformers: introduction

# In[1]:


# first, install the library Transformers
# you only need to install this library once. 

get_ipython().system('pip install transformers')


# In[2]:


# import the transformers library, along with the pipeline and set_seed functions

import transformers
from transformers import pipeline, set_seed


# ## text generation
# generates new text based on an input prompt, like a chatbot. 

# In[3]:


# pulling in the text generation "pipeline", and setting it to the variable
# called "generator"

generator = pipeline('text-generation')


# In[4]:


# taking the generator function and passing a sentence and maximum length and 
# number of responses to the function

generator('This summer, I was rock climbing in Yosemite when',
          max_length=50,
          num_return_sequences=2)


# ## fill mask
# Fills the word in the blank with a guess

# In[5]:


# create the "unmasker" variable set to the "fill-mask" task

unmasker = pipeline('fill-mask')


# In[ ]:


# give it a sentence, with the <mask> as a fill in the blank
# the "top_k" argument means we will get 4 responses

unmasker('To be or not to be; that is the <mask>', top_k=4)


# In[ ]:


unmasker('My name is Professor Calado and I teach at <mask>', top_k=4)


# ## summarization
# Takes a longer text and condenses it.

# In[ ]:


# taking the "summarization" task and saving it to "summarizer"
# then passing some text into the "summarizer"

# we use three quotes at the beginning and end of the string 
# if we want to put in a text that spans multiple lines

summarizer = pipeline('summarization')
summarizer('''The past 3 years of work in NLP have been characterized 
by the development and deployment of ever larger language models, 
especially for English. BERT, its variants, GPT-2/3, and others, 
most recently Switch-C, have pushed the boundaries of the possible 
both through architectural innovations and through sheer size. Using 
these pretrained models and the methodology of fine-tuning them for 
specific tasks, researchers have extended the state of the art on a 
wide array of tasks as measured by leaderboards on specific benchmarks 
for English. In this paper, we take a step back and ask: How big is too 
big? What are the possible risks associated with this technology and 
what paths are available for mitigating those risks? We provide 
recommendations including weighing the environmental and financial costs 
first, investing resources into curating and carefully documenting 
datasets rather than ingesting everything on the web, carrying out 
pre-development exercises evaluating how the planned approach fits into 
research and development goals and supports stakeholder values, and 
encouraging research directions beyond ever larger language models.''')


# ## question-answering
# Takes an input question and context and provides an answer

# In[ ]:


# calling the question-answer pipeline
# passing a question and context into the pipeline
# the function will look into the context to get the answer

question_answer = pipeline('question-answering')
question_answer(question='Was the writer of Frankenstien a man or a woman?', 
                context='''Frankenstien is a book written by Mary Shelley who is 
                a woman''')


# ## ner (named entity recognition)
# Named entity recognition (NER) is a task where the model has to find which parts of the input text correspond to entities such as persons, locations, or organizations.

# In[ ]:


ner = pipeline("ner", grouped_entities=True)
ner("My name is Filipa Calado and I work at City College in Manhattan.")


# In[ ]:




