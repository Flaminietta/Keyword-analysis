#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
============================================
Find key-words in a text and their frequency
============================================

Key-words can be of 1,2 or 3 grouped words

"""

import re
import inflect
inflect = inflect.engine()
from collections import Counter
from ngrams import ngrams

def keywords(passage):
    # List words and make all singular nouns
    word = []
    words = re.findall(r'\w+', passage)
    ini_tot_words = len(words)
    for w in words:
        if w=='000': w='THOUSAND' # Future work: generalize!
        if w !='' and len(w) >= 2: 
           if inflect.singular_noun(w) is False:
              word.append(w)   
              continue
           else:
              s = inflect.singular_noun(w)
              word.append(s)
              
    tot_words = len(word)
       
    # Count words and select the n-most repeated ones   
    word_counts = Counter(word)
    key_word_1 = word_counts.most_common(20)        # The n-most common single key-word
                                                    # excluding words shorter than 3 characters                                      
    all_2key_words = Counter(ngrams(word, 2))
    key_words_2 = all_2key_words.most_common(20)    # The n-most common bigram (double key-word)
                                                    # excluding words shorter than 3 characters           
    all_3key_words = Counter(ngrams(word, 3))
    key_words_3 = all_3key_words.most_common(20)    # The n-most common trigram (triple key-word)
                                                    # excluding words shorter than 3 characters                                         
    return(ini_tot_words, tot_words, key_word_1, key_words_2, key_words_3)
                                           