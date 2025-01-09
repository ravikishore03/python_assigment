#!/usr/bin/env python
# coding: utf-8

# In[12]:


def mean_value(*n):
    sum = 0
    count = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum /counter 
    return mean


# In[22]:


def product(*n):
    result = 1
    for number in n:
        result *= number
    return result


# In[24]:


print(product(2, 3, 4))


# In[ ]:




