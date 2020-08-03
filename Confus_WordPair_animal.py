#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time as time
import numpy as np

# LOADING WP AS WP_DICT
import pickle as pickle
with open('WPdict_COCA_pkl.pkl','rb') as fp:
    WP_dict = pickle.load(fp)
print('type and shape of WP_dict',type(WP_dict),len(WP_dict))

# LOADING CMU DATA AND MAKING DICTIONARY
file = open("/home/tdacunha/pnc_project/cmudict-updated-plotnik.dict", 'r')
data = file.read().splitlines()
data = np.array(data)
#print((data))
pron = []
for i in range(len(data[:])):
    sep = (data[i]).split(' ',1)
    pron.append(sep)
#print(np.array(pron))
file.close()
print('shape of pron',np.shape(pron))

CMU_dict = {}
count = 0
for line in pron[:]:
    k,v = line[0],line[1]
    if k not in CMU_dict:
        CMU_dict[k] = v
        count +=1
    elif k in CMU_dict:
        CMU_dict[k] = CMU_dict[k]+','+v
        count+=1
print("done, shape of cmu_dict",len(CMU_dict))

#MAKING TP_dict,H_dict:

t0 = time.time()
TP_dict = {}
H_dict = {}
Dict = WP_dict
num = 0
for key in Dict:
    if num%1000000==0:
        print(num, time.time()-t0)
    #if num == 1000:
        #break
    num+=1
    
    wp_list = key.split(',')
    count = Dict[key]
    word1 = wp_list[0].upper()
    word2 = wp_list[1].upper()
    if word1 in CMU_dict and word2 in CMU_dict:
        trans_list1 = CMU_dict[word1].split(',')
        trans_list2 = CMU_dict[word2].split(',')
    else:
        continue
    for i in range(len(trans_list1)):
            for j in range(len(trans_list2)):
                trans1 = trans_list1[i]
                trans2 = trans_list2[j]
                tp = trans1+','+trans2
                info = key + ':' + str(count)
                if tp in TP_dict:
                    if H_dict[tp] !=  info: #dealing with random double like "kept" in cmu
                        TP_dict[tp] = TP_dict[tp]+count
                        H_dict[tp] = H_dict[tp]+ ';' + info
                else:
                    TP_dict[tp] = count
                    H_dict[tp] = key + ':' + str(count)
                    

print(len(TP_dict),len(H_dict))
#print(TP_dict)
import pickle as pickle
with open('TP_dict.pkl','wb') as fp:
    pickle.dump(TP_dict,fp)
with open('H_dict.pkl','wb') as fp1:
    pickle.dump(H_dict,fp1)

# NEW DICT VERSION: CONFUSABILITY FULL BEFORE
print('starting confusability')
t0 = time.time()

V = ['owr', 'e', 'i', 'ow', 'eyF', 'ay0', 'ey', 'o', 'ae', 'uh', 'oh', 'ahr', 'iy', 'aeh', 'ay', 'Tuw', 'aeBR', 'aw', '*hr', 'uw', 'eyr', 'owL', 'uwr', 'owF', 'iyr', 'oy', 'u', 'ah', 'uwL']
C_full_before = np.zeros((len(V))) # Confusability Matrix
print("V=",V)

# CALCULATING NTOT
Ntot=0
for tp in TP_dict:
    Ntp = TP_dict[tp] #float(WP_CMU1[i,2])
    Ntot += Ntp
print("Ntot=", Ntot, time.time()-t0)

# CONFUSABILITY CALCULATION
for i in range(len(V)):
    vi = V[i]
    print("vi=",vi)
    vi_1 = ' ' + vi + '.1'
    
    V_altered = [x for x in V if x != vi]
    #V_altered.remove(vi)
    print("vi", vi)
    
    # FIRST SUM
    num=0
    TPlist_to_sum = []
    for tp in TP_dict:
        #print(num,time.time()-t0)
        if num%100000==0:
            print(num,time.time()-t0)
        #if num==1000:
            #break
        num+=1
        
        count = TP_dict[tp]
        tp_list = tp.split(',')
        trans1 = tp_list[0]
        trans2 = tp_list[1]
        #print(num,'trans1=',trans1)
        trans_alt = ' '+ trans2 #CHANGED FOR BEFORE
        if vi_1 in (trans_alt):
            d = 1
        else:
            continue
        Ntp = count
        coeff = (Ntp)/Ntot
        
        # SECOND SUM
        Vjlist_to_sum = []
        for j in range(len(V_altered)):
            vj = V_altered[j]
            vj_1 = ' ' + vj + '.1'
            trans_vj = (trans_alt.replace(vi_1, vj_1, 1)).lstrip()
            tp_vj = trans1 + ','+trans_vj #trans_vj+','+trans2 # CHANGED FOR BEFORE
            #print(j,vj,'trans_vj=',trans_vj)
            #print("t_vj is:",t_vj,"t is:",t)
            if tp_vj in TP_dict:
                Ntp_vj = TP_dict[tp_vj]
                #print('MUTATION FOUND',tp_vj)
                #print('trans1=',trans1,'trans2=',trans2,'trans_vj=',trans_vj, 'n=',n,'j=',j)
                #print('Ntp_vj=',Ntp_vj)
            else:
                Ntp_vj = 0
            inner_term = Ntp_vj/(Ntot)
            #print("inner term", inner_term)
            Vjlist_to_sum.append(inner_term)
        #print('aftervj loop',time.time()-t0)
        SumVj = sum(Vjlist_to_sum)
        term = coeff*SumVj
        TPlist_to_sum.append(term)
    SumTP = sum(TPlist_to_sum)
    C_full_before[i] = SumTP
    
print("Confusability before = ", C_full_before)
print("time=", time.time()-t0)



#SAVING CONFUSABILITY TO FILE 
C_dict_full_before = {}
for i in range(29):
    C_dict_full_before[V[i]]= C_full_before[i]
print(np.array(C_dict_full_before))

text = open("Confus_WP_full_before.txt", "w")
for k, v in C_dict_full_before.items():
    text.write(str(k) + ' : '+str(v)+'\n\n')
text.close()

print('Confusability saved, done')

    

    

    


# In[ ]:





# In[ ]:




