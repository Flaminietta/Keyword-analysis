# Keywords-analysis
Compared keyword analysis

DESCRIPTION
===========

This is a Python 3 package, which generates the most important key-phrase (or key-words) from a document based on a corpus.
It reads one script file (script.txt) and 3 transcript files (transcript1,2,3.txt) and:

1. compute the most important key-words (a key-word can be between 1-3 words) in the script and transcripts;

2. select the top 10 keywords and the top 5 bigrams and trigrams for visualization and comparison;

3. the visualization in piecharts shows the percentage of occurrence of these top n-words in each text and overall.

NOTES
=====

The texts are intially cleaned from a list of stopwords (http://ir.dcs.gla.ac.uk/resources/linguistic_utils/stop_words). 
Differences due to capital letters and singular/plural nouns are disregarded. The top 10keywords and the top 5 bigrams and trigrams give a simplified but significative idea of keyword distribution. 

EXECUTION
=========

The code can be run through text_analysis.py. Functions include:
- keywords.py (count key-words in a text)
- ngram.py (get the frequency of any n-gram (composition of n-words))
- RemStopW.py (remove stopwords from a text)
- piecharts.py (visualize percentage of occurrence in a piechart)

Stopwords are stored in a file.

REQUIREMENTS
============
codecs
re
counter
inflect
tee
islice
matplotlib
title
