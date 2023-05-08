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
# - First, you will load up a dataset for analysis. You may choose from the following sets of data:
#    - In the default option, this dataset is "[toxcicity
#   prompts](https://huggingface.co/datasets/allenai/real-toxicity-prompts),"
#   which is a collection of prompts that tend to provoke biased
#   responses. You will load this dataset using the provided code in the
#   assignment sheet, which contains an if statement that filters out
#   the prompts by toxicity score. 
#   - Choose a dataset that has some creativity, like from a novel, game, movie, etc. You might, for example, load up the first sentences from a selection of novels in [Project Gutenberg](https://www.gutenberg.org/). Or you can use quotes from a game. Your choice, as long as it's creative! 
# - Second, trom the dataset, you will compile a list of 10 prompts, using the
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
#   `model='your-model-name'` argument in the pipeline function. 
# - Fourth, pass your selected prompts into the generator
#   object, which you created from the pipeline function.
# - Finally, examine the results and summarize your response. Use the following questions to    prompt your thinking. 5 - 7 sentences. 
#     - Pay attention to anything in the results that sticks out to you. Are there any surprising results? Or any patterns that you can notice across multiple results? What do these surprises or patterns in the results suggest about the training data?   
#     - Do you find the results to be more biased or offensive than the original prompt? Do
#     you find them to be more biased or offensive than the "continuation" sentences from the original dataset? How so?
#     - What do the results say about the original dataset? What ideas or biases might be prevalent in the original dataset?

# 
