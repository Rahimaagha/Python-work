#!/usr/bin/env python
# coding: utf-8

# # A.
# 

# In[1]:


def match_ends(put):
    x=0
    
    for val in put:
     if len(val) > 1 and val[0]==val[-1]:
        x= x+1
    return x


# In[2]:


match_ends(['wow','dad','pop'])


# In[3]:


match_ends(['fef','pop','kel'])


# # B

# In[5]:


def front_x(words):
    l1 = []
    l2 = []

    for word in words:
        if word.startswith('x'):
            l1.append(word)
    else:
        l2.append(word)

    return sorted(l1) + sorted(l2)


# In[6]:


front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] )


# In[7]:


front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])


# In[8]:


front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])


# In[ ]:




