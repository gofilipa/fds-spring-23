#!/usr/bin/env python
# coding: utf-8

# ## transformers: bias & discrimination

# ### Freewrite: 
# 
# ### Why is bias and discrimination a problem in large language models? Where do models learn to be biased? 
# - the data from the models do not represent everyone. 
# - the people programming the models: computer programmers. They are not trained to be sensitive to alternative perspectives, or minority experiences or views. 
# - some of the data sources include reddit and are not well moderated
# - reflects current society, so if society is biased, then the model will be biased. 
# 

# ### Why is it difficult to train a model that isn't biased? Refer to the "[Stochastic Parrots](https://dl.acm.org/doi/pdf/10.1145/3442188.3445922)" paper, section 4, to get ideas
#   - "Size Doesn’t Guarantee Diversity" - the idea that representation is enough to represent diverse points of view overlooks the ways that the data and training practices overlooks minority perspectives. 
#   - "Hegemonic viewpoints" - the dominant view. The model only represents the most common viewpoints. Ideas, identites, perspectives that are different or less common get weeded out. This is because it's a statistical model, looking for the biggest pattern. 
#   - Privilege - those who do not have access to the internet cannot represent themselves. People who are not in 1st world countries; people who cannot afford technologies. 
#   - Most of the data comes from one demographic (male, young) whose view will dominate the others. 
#   - "Mob mentality" on social media means that unpopular views are suppressed. 
#   - There's no way to "automate" taking out bias. The attempt to weed out "bad words" takes out all examples of the words, even the ones that explain why the words are bad. This means the model has no information about why certain words are offensive. For example the the list of "[Dirty, Naughty, Obscene or Otherwise Bad Words](https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/blob/master/en)."

# In[ ]:




