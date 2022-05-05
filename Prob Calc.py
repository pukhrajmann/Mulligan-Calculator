#!/usr/bin/env python
# coding: utf-8

# In[134]:


import numpy as np
from random import shuffle


# In[135]:


#Runterra Mulligan Calculator
def deck(lowcost,midcost,highcost):
    #lowcost 0-3
    #midcost 4-7
    #highcost 8-12
    low_mid_deck = lowcost + midcost
    lowdeck = np.linspace(0, lowcost, lowcost+1)
    middeck = np.linspace(lowcost+1, low_mid_deck, midcost)
    highdeck = np.linspace(low_mid_deck+1, highcost + low_mid_deck, highcost)

    deck = np.hstack(( lowdeck,middeck,highdeck )).ravel()
    
    shuffle(deck)
    return deck


# In[136]:


def hand(deck):
    mulligan = []
    for x in range(4):
        mulligan.append(deck[x])
    
    return mulligan


# In[137]:



hand(deck(10,13,10))

