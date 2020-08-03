#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import csv
import numpy as np
import ast

t0 = time.time()
#LOADING PNC DATA
pnc_file = open('/home/tdacunha/pnc_project/refaved_PNCvowels_master_corrected_shorta.csv', newline='')
#pnc_file = open('/Users/TaraD/Downloads/refaved_PNCvowels_master_corrected_shorta.csv', newline='')
print('opened pnc file')
data = np.array(list(csv.reader(pnc_file)))
print('made data array')
pnc_words = (data[1:,11])
#pnc_vowel_freqs = (data[1:,13]) #CAN CHANGE TO DIFFERENT FREQUENCY COLUMN
pnc_trans = data[1:,34]
pnc_v_index = data[1:,32]
pnc_v_class = data[1:,51]
pnc_stress = data[1:,9]

print('reached first for loop', time.time() - t0)
for i in range(len(pnc_words)):
    pnc_words[i] = pnc_words[i].lower()
print("PNC length:", len(pnc_words))
#print("time for loading and making PNC lists:", time.time()-t0)


#LOADING COCA DICTIONARY
COCA_words = open('/home/tdacunha/pnc_project/dict_COCA_txt3.txt', 'r')
#COCA_words = open('/Users/TaraD/LING_Research/dict_COCA_txt3.txt', 'r')
COCA_list = COCA_words.readlines()

omitfile = open('/home/tdacunha/pnc_project/omitwords.csv')
#omitfile = open('/Users/TaraD/Downloads/omitwords.csv')
omitdata = list(csv.reader(omitfile))
omitwords = []
for i in range(1,len(omitdata)):
    line = (((omitdata)[i]))
    if line != []:
        omitwords.append(line[0].lower())
#print(omitwords)
#print(COCA_list[0:50])
                      
omitfile.close()
COCA_words.close()


t1 = time.time()
COCA_list = [value for value in COCA_list if value != '\n']
#print("time for list removal = ", time.time() - t1)
#print(COCA_list[0:50])

#Removing omitted words from COCA_list:
#for j in range(len(COCA_list)):
for line in COCA_list:
    #line = COCA_list[j]
    array = line.split(':')
    word = array[0][:-1]
    if (word in omitwords) == True:
        COCA_list.remove(line)
#print(COCA_list[0:50])
            

print('time for opening etc:',time.time()-t0)


# In[3]:



t1 = time.time()
pnc_words_list = list(pnc_words)
print("COCA_list length", len(COCA_list))

header = ['COCA word', 'COCA dict #', 'PNC word', 'Trans', 'v_index', 'v_class', 'Stress', 'PNC count']
PNCinCOCA = [header]

count = 0
for line in COCA_list:
    #if count < 21:
    if count%1000 == 0 or count==1 or count==2:
        print(count, time.time()-t1)
            
    #Getting COCA info
    #print("before splitting etc", time.time()-t1)
    array = line.split(':')
    word = array[0][:-1]
    number = (array[1].replace('\n',''))[1:]
    #line_list = [word, number]
        
    #IF COCA WORD IN PNC, GATHER INFO AND APPEND
    #print("before indices:", time.time()-t1)
    #indices = (np.where(pnc_words==word))[0]
    indices = [i for i in range(len(pnc_words_list)) if pnc_words_list[i]==word]
    
    #print("after indices:", time.time()-t1)
    if len(indices) != 0:
        list_array = []
        list_array_count = []
        for index in indices:
            line_list=[word, number, pnc_words[index], pnc_trans[index], pnc_v_index[index], pnc_v_class[index], pnc_stress[index], ]
                
            if (line_list not in list_array) == True:
                list_array.append(line_list)
                list_array_count.append(1)
                    
            else:
                ind = list_array.index(line_list)
                list_array_count[ind] +=1
        for i in range(len(list_array)):
            (list_array[i]).append(list_array_count[i])
                
                    
            
        PNCinCOCA.extend(list_array)
        
    #IF COCA WORD NOT IN PNC, PUT DASHES        
    else:
        line_list=[word,number,'-','-','-','-','-','-']
        PNCinCOCA.append(line_list)
    #print("after if/for loop:", time.time()-t1)
    
    count += 1
        
print('finished looping')        
PNCinCOCA = np.array(PNCinCOCA)
#print(PNCinCOCA)

print('finished PNCinCOCA array, now saving files')
np.savetxt('PNCinCOCA_full.txt',PNCinCOCA,'%-15s')
np.savetxt('PNCinCOCA_full.csv',PNCinCOCA, '%s',delimiter=",")

print(time.time()-t1)


# In[ ]:





# In[96]:


"""
list1 = [1,'2',5,'2']
list2 = [7,8,9]

list3 = [[1,2,3],[4,5,6]]
list1 in list3
list3.append(list2)
#print(list3)
indices = (np.where(np.array(list1)=='7'))[0]
print(len(indices))
"""


# ## Making reduced file with words in both pnc and coca, excluding those with less than 5% count

# In[27]:


import time
import csv
import numpy as np
import ast

t0 = time.time()
PC_file = open('/Users/TaraD/LING_Research/PNCinCOCA_full.csv', newline='')
#pnc_file = open('/Users/TaraD/Downloads/refaved_PNCvowels_master_corrected_shorta.csv', newline='')

print('opened pncincoca file')
#data = np.array(list(csv.reader(pnc_file)))
#print(np.shape(data))
data_array = np.array(list(csv.reader(PC_file)))
data_list_fixed = []
#print(data_array)
for row in data_array:
    if len(row) == 8:
        data_list_fixed.append(row)
    else:
        new_row = []
        number = len(row)-8
        string = ''
        for j in range(0,number+1):
            string += row[j]
        new_row.append(string)
        new_row.extend(row[number+1:])
        data_list_fixed.append(new_row)
data_array_fixed = np.array(data_list_fixed)
print(data_array_fixed[:10])

            

#data = np.array([np.array(xi) for xi in data_array])
print(np.shape(data_array_fixed))
#print(data_array_fixed[:10])
for i in data_array_fixed:
    if (len(i)) != 8:
        print(i, len(i))


# In[30]:


print("length of array:", np.shape(data_array_fixed))
header = ['COCA word', 'COCA dict #', 'PNC word', 'Trans', 'v_index', 'v_class', 'Stress', 'PNC count']

reduced_PNCinCOCA = [header]
t0 = time.time()
for i in range(1,len(data_array_fixed)):
    line = data_array_fixed[i]
    word = line[0]
    if word != data_array_fixed[i-1,0] and line[7] != '-':
        word_list = []
    #if line[7] =='1':
        #np.delete(data_array, (i), axis=0)
        #continue
    if line[7] != '-':
        word_list.append(line)
    else:
        continue
    # At last instance of word
    if i == (len(data_array_fixed)-1) or data_array_fixed[i+1,0] != word:
        word_array = np.array(word_list)
        #print(word_array)
        Sum = np.sum((word_array[:,7].astype(int)), axis=0)
        mask = (word_array[:,7].astype(int) >= (.05*Sum))
        reduced_word_array = word_array[mask]
        #print(reduced_word_array)
        #print(len(word_array), len(reduced_word_array))
        reduced_PNCinCOCA.extend((reduced_word_array).tolist())
    else: 
        #print('continue')
        continue

print(np.shape(reduced_PNCinCOCA))
#print(*reduced_PNCinCOCA, sep='\n')
print(time.time()-t0)

np.savetxt('PNCinCOCA_5pcdeleted.csv',reduced_PNCinCOCA, '%s',delimiter=",")
np.savetxt('PNCinCOCA_5pcdeleted.txt',reduced_PNCinCOCA,'%-15s')
        
        


# In[68]:


print(*reduced_PNCinCOCA, sep='\n')


# ## Finding Multiple High Frequency Pronunciations

# In[26]:


import time
import csv
import numpy as np
import ast

t0 = time.time()
PC_file = open('/Users/TaraD/LING_Research/PNCinCOCA_5pcdeleted.csv', newline='')
data_array = np.array(list(csv.reader(PC_file)))
#print(data_array[:5])
header = ['COCA word', 'COCA dict #', 'PNC word', 'Trans', 'v_index', 'v_class', 'Stress', 'PNC count']

reduced_PNCinCOCA2 = [header]
for i in range(1,len(data_array)):
    line = data_array[i]
    word = line[0]
    trans = line[3]
    if i == 1 or word != data_array[i-1,0]:
        word_list = []
        word_list.append(line)
        

    # MAKING WORD_LIST WITH UNIQUE TRANSCRIPTIONS, IF MULTIPLE TRANSCRIPTION, KEEPS ONE WITH MOST COUNTS
    word_list = np.array(word_list)
    if trans in word_list[:,3]:# and i !=1 and word == data_array[i-1,0]:
        index = (np.where(word_list[:,3]==trans))[0]
        if line[7].astype(int) > (word_list[index,7].astype(int)):
            word_list[index] = line
            word_list = word_list.tolist()
        #else:
            #continue
    else:
        word_list = word_list.tolist()
        word_list.append(line)
    
    # At last instance of word: Word list is now unique transcriptions. 
    if i == (len(data_array)-1) or data_array[i+1,0] != word:
        word_array = np.array(word_list)
        #print(word_array)
        #word_list2 = []
        #for k in word_array:
            #word_array2 = np.array(word_list2)
            #if k[3] == 
        
        # IF MULTIPLE TRANSCRIPTIONS
        if len(word_array) > 1:
            Sum = np.sum((word_array[:,7].astype(int)), axis=0)
            
            # MASK SO ONLY TRANSCRIPTIONS > 30% SUMMED COUNTS REMAIN
            mask = (word_array[:,7].astype(int) >= (.30*Sum))#&(word_array[:,7].astype(int) <= (.30*Sum))
            reduced_word_array = word_array[mask]
        #print(reduced_word_array)
        #print(len(word_array), len(reduced_word_array))
        #if (len(set(reduced_word_array[:,3])) > 1):
            #print(set(reduced_word_array[:,3]))
            
            # IF STILL MULTIPLE HIGH TRANSCRIPTIONS: RECORD AND APPEND.  V
            if len(reduced_word_array) > 1:
                reduced_PNCinCOCA2.extend((reduced_word_array).tolist())
    else: 
        #print('continue')
        continue    
print(np.shape(reduced_PNCinCOCA2))
print(*reduced_PNCinCOCA2, sep='\n')
np.savetxt('PNCinCOCA_HighFreqAlt.csv',reduced_PNCinCOCA2, '%s',delimiter=",")
np.savetxt('PNCinCOCA_HighFreqAlt.txt',reduced_PNCinCOCA2,'%-15s')
print(time.time()-t0)


# ## Removing Same Stress Vowel Entries from High Freq Alt

# In[31]:


import time
import csv
import numpy as np
import ast

t0 = time.time()
PC_file = open('/Users/TaraD/LING_Research/PNCinCOCA_HighFreqAlt.csv', newline='')
data_array = np.array(list(csv.reader(PC_file)))
print(data_array[:5])
header = ['COCA word', 'COCA dict #', 'PNC word', 'Trans', 'v_index', 'v_class', 'Stress', 'PNC count']


# In[40]:


reduced_PNCinCOCA3 = [header]
print("length of highfreqalt:", len(data_array[1:]))
for i in range(1,len(data_array[1:])):
    line = data_array[i]
    word = line[0]
    if i == 1 or word != data_array[i-1,0]:
        word_list = []
    word_list.append(line)
    if i == (len(data_array)-1) or data_array[i+1,0] != word:
        word_array = np.array(word_list)
        #indices = np.where(word_array[:,6] == 1)[0]
        if (len(word_array)==2) and (word_array[0,6].astype(int) == 1) and (word_array[0,6] == word_array[1,6]) and (word_array[0,5] == word_array[1,5]) and (word_array[0,4] == word_array[1,4]):
            print(word)
            continue
        else:
            reduced_PNCinCOCA3.extend(word_array.tolist())
print(len(reduced_PNCinCOCA3))
print(reduced_PNCinCOCA3)

np.savetxt('PNCinCOCA_HighFreqAlt_reduced.csv',reduced_PNCinCOCA3, '%s',delimiter=",")
np.savetxt('PNCinCOCA_HighFreqAlt_reduced.txt',reduced_PNCinCOCA3,'%-15s')


# In[ ]:




