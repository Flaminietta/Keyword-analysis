#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================
Remove stop words from a text
=============================

"""

def RemStopW(wlist, stopwords):
    return [w for w in wlist if w not in stopwords]