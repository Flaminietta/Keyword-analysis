#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 7 Apr 2017
@author: Flaminia Catalli

=========================
COMPARATIVE TEST ANALYSIS
=========================

"""
import re
import codecs
from collections import Counter

#Functions
from keywords import keywords
from RemStopW import RemStopW
from piechart import piechart

# ==================
# List of stop words
# ==================
# (http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words)
with codecs.open('stopwords.txt', 'r', 'UTF-8') as s:
     stop = s.read()
stopwords = stop.split();
cap_stopwords = [word.upper() for word in stopwords] # Disregard differences due to capital letters
# ===================================================
# Read files: the original script and the transcripts
# ===================================================
# Disregard differences due to capital letters
# Eliminate stop-words
path='./scripts'
files=['script.txt','transcript_1.txt','transcript_2.txt','transcript_3.txt']
keytrans=[]
ini_tot=[]
tot=[]
for file_i in files:
    with codecs.open(path+'/'+file_i, 'r', 'UTF-8') as f:
        passage = f.read()
    lista = re.findall(r"[\w']+", passage)
    cap_list = [word.upper() for word in lista]
    scriptlist = RemStopW(cap_list, cap_stopwords) #list
    script = ' '.join(scriptlist) #script - cleaned 
# ==============
# Find key-words
# ==============
# For each text find the 20-most common key-words (single=k1, bigram=k2 or trigram=k3)
# excluding all the stop-words 
    [ini_tot_words,tot_words, k1, k2, k3] = keywords(script)
    keytrans.append([k1,k2,k3])   #list of list - k1,k2,k3 for each text
    ini_tot.append(ini_tot_words) # total # of words in the original text
    tot.append(tot_words)         # total # of words counted after cleaning
# ==================
# Printing some info
# ==================
for i,k in enumerate(keytrans):
    print('Total number of words in '+files[i])
    print(str(tot[i]))
    print('The 10 most common single key-words in '+files[i])
    for w in k[0][0:11]: print(str(w))
    print('The 5 most common bigram key-words in '+files[i])
    for w in k[1][0:6]: print(str(w))
    print('The 5 most common trigram key-words in '+files[i])
    for w in k[2][0:6]: print(str(w))
# =============================================================
# Plot pie-charts of most frequent key-words, bigrams, trigrams
# =============================================================
list_dicts=[]
for k in keytrans:
    k1_dic = dict(k[0][0:10])
    piechart(list(k1_dic.keys()),list(k1_dic.values()))
    k2_dic = dict(k[1][0:5])
    piechart(list(k2_dic.keys()),list(k2_dic.values()))
    k3_dic = dict(k[2][0:5])
    piechart(list(k3_dic.keys()),list(k3_dic.values()))
    list_dicts.append([k1_dic,k2_dic,k3_dic])
# ===================================================
# Common list of all n key-words and overall analysis
# ===================================================
# n=10
k1_tot_count = (Counter(list_dicts[0][0]) + Counter(list_dicts[1][0]) + Counter(list_dicts[2][0]) +
Counter(list_dicts[3][0]))

com_list_len = len(k1_tot_count)
k1_tot_ord = k1_tot_count.most_common(com_list_len)

# again the n-most common words of the list of the most common words found in all texts
k1_tot_val = [item[1] for item in k1_tot_ord]
k1_tot_keys = [item[0] for item in k1_tot_ord]

k1_tot_val_n = k1_tot_val[0:7]
k1_tot_keys_n = k1_tot_keys[0:7]

print('The '+str(com_list_len)+' most common single key-words in all texts')
for w in k1_tot_keys: print(str(w))
piechart(k1_tot_keys_n,k1_tot_val_n)

