#!/usr/bin/env python
# coding: utf-8

# # Final Project

# ## Objective: 
# To explore & analyze how a language model from the
# *Transformers* libary generates text based on specific prompts. You
# will have the choice of analyzing discrimination and bias, or
# analyzing a topic of your choosing. If you choose to do the latter,
# you must also submit your prompts that you use for inputing to the
# language model.
# 

# ## Instructions:
# 
# Steps: 
# - First, you will load up a dataset for analysis. In the default
#   option, this dataset is "[toxcicity
#   prompts](https://huggingface.co/datasets/allenai/real-toxicity-prompts),"
#   which is a collection of prompts that tend to provoke biased
#   responses. You will load this dataset using the provided code in the
#   assignment sheet, which contains an if statement that filters out
#   the prompts by toxicity score. 
# - Second, trom the dataset, you will compile a list of 20 prompts, using the
#   provided code in the assignment sheet. Later on, you will draw from
#   this list to feed prompts into the text generator. You may use the
#   code provided.
# - Third, you will create a generator object tied into which you will
#   pass your prompts. Here, you may use the default language model
#   (which is 'distil-gpt2', or use one of your choosing from the
#   [models
#   hub](https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads)),
#   with the "text generation" option from the "Natural Language
#   Processing" selected on the lefthand menu. If selecting your own
#   model, modify the code provided by adding a
#   ~model='your-model-name'~ argument in the pipeline function. 
# - Fourth, pick out five prompts from your list of twenty to pass into
#   the generator object. You can create a slice (using list slicing) or
#   specify the index for each prompt, one at a time. Use the
#   code provided, but modify it to select the 5 prompts of your
#   choosing. 
# - Fifth, when you've selected your prompts, pass them into the generator
#   object, which you created from the pipeline function.
# - Finally, examine the results and summarize your response. Pay
#   attention to anything that sticks out to you. Do you find the
#   results to be more biased or offensive than the original prompt? Do
#   you find them to be more biased or offensive than the "continuation"
#   sentences from the original dataset. Write up a summary of your
#   examination.
