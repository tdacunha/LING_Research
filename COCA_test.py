#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import os
import time

t1 = time.time()
PoS_remove = ['y','x', '"@_ge','...','ge_"@', 'zz_nn', 'fo']
Join = ["'s", "'ll","'m", "'ve","'re","n't", "'d", "'"]

def phone_number(word):
    if len(word) >= 8 and word[3] == '-' and word[0].isdigit()==True and word[4].isdigit()==True and word[5].isdigit()==True and word[1].isdigit()==True and word[6].isdigit()==True:
        return True
    else:
        return False
    
def line_inclusion(x):
    if len(x)==3 and x[2] not in PoS_remove and x[0].lower() not in Join and 'www' not in x[0].lower() and '*' not in x[0].lower() and phone_number(x[0].lower())==False:
        return True

                                                                                                                                            

dict = {}
directory = '/Users/TaraD/Ling_Research/COCA/COCA/Word_lemma_PoS/'

for file in os.listdir(directory):
    print(file)
    
    #Full directory:
    text = open(directory + file, 'r', encoding='utf-8', errors='ignore')
    
    #Test file:
    #text = open('/Users/TaraD/Ling_Research/COCA/COCA/Word_lemma_PoS/wlp_news_2007.txt', 'r', encoding='utf-8', errors='ignore')
    
    lines = (text.readlines())

    length = len(lines)
    
    for index in range(length):
        line = lines[index]
        #line_after = lines[index+1]
        
        line_list = line.split()
        #line_list_after = line_after.split()
        
        #MAKING SURE LINE/WORD SHOULD BE INCLUDED
        if line_inclusion(line_list)==True:
            word = (line_list[0]).lower()
            
            #MAKING SURE NOT END WORD AND CONCATENATING CONTRACTIONS
            if (index+1) < length:
                word_after = ((lines[index+1]).split())[0].lower()   #(line_list_after[0]).lower()

                if word_after in Join:
                    word = word + word_after
            
            #ADDING WORD TO DICTIONARY
            if word in dict:
                dict[word] = dict[word] + 1
                
            else:
                dict[word] = 1
            #print(word)
            
    text.close()        
    
print(time.time()-t1)
print(len(dict))
#print(dict)

