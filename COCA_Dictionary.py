#!/usr/bin/env python
# coding: utf-8

# # Testing With 1 File

# In[85]:


"""
import numpy as np
dict = {}

text = open('/Users/TaraD/Ling_Research/COCA/COCA/Word_lemma_PoS/wlp_spok_2005.txt', 'r', encoding='utf-8', errors='ignore')
lines = (text.readlines())

count = -1
for line in lines:
    count += 1
    #if count <50:
        #if count >= 0:
    line_list = line.split()
    if len(line_list)==3 and line_list[2] != 'y':
        word = line_list[1]
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
        #print(word)
        
    #else:
        #break
print(count)
print(len(dict))
#print(dict)
#print(dict.values())
#print(max(dict, key=dict.get))

text.close()
"""


# In[2]:


"""
import os
directory = '/Users/TaraD/Ling_Research/COCA/COCA/Word_lemma_PoS/'

count = 0
for file in os.listdir(directory):
    count+=1
print(count)
"""


# In[86]:


"""
sorted_dict = sorted(dict, key=dict.get, reverse=True)
print(sorted_dict)
"""


# # Running all Files --> Full Dictionary

# In[58]:


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

                                                                                                                                            


# In[63]:


import numpy as np
import os
import time

t1 = time.time()


dict = {}
directory = '/home/tdacunha/pnc_project/COCA/Word_lemma_PoS/'

count = 0
for file in [1]: #in os.listdir(directory):
    #if count > 0:
        #break
    #count+=1
    #print(file)
    
    #Full directory:
    #text = open(directory + file, 'r', encoding='utf-8', errors='ignore')
    
    #Test file:
    text = open('/home/tdacunha/pnc_project/COCA/Word_lemma_PoS/wlp_news_2007.txt', 'r', encoding='utf-8', errors='ignore')
    
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


# In[60]:


"""
print(dict)
"""


# In[68]:


#import pickle
dict_COCA_txt = open("TESTdict_COCA_txt.txt", "w")
for k, v in dict.items():
    dict_COCA_txt.write(str(k) + ' : '+str(v)+'\n\n')
#dict_COCA_txt.write((dict))

#with open("dict_COCA_txt3.txt", "w") as file:
    #file.write(pickle.dumps(dict))
dict_COCA_txt.close()

#import pickle
#dict_COCA_pkl = open("dict_COCA_pkl3.pkl", "wb")
#pickle.dump(dict,dict_COCA_pkl)
#dict_COCA_pkl.close()


# In[76]:


#import numpy as np
#sorted_dict_full = sorted(dict, key=dict.get, reverse=True)
#print(type(sorted_dict_full))
#print(np.shape(sorted_dict_full))
#print(type(dict))
#dict_COCA_txt_sorted = open("dict_COCA_txt3_sorted.txt", "w")
#for k, v in sorted_dict_full:
#    dict_COCA_txt_sorted.write(str(k) + ' : '+str(v)+'\n\n')
#dict_COCA_txt_sorted.close()
#print(sorted_dict_full)


# In[ ]:





# In[62]:


#TESTING ETC
#word = '215-382-5349'
#word[8].isdigit()


# In[ ]:




