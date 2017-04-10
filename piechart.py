#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============
Basic pie chart
===============

Few optional features:
* slice labels
* auto-labeling the percentage
* offsetting a slice with "explode"
* drop-shadow
* custom start angle

Note about the custom start angle:
The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""

import matplotlib.pyplot as plt
#from pylab import title

def piechart(labels,sizes):
    piechart.counter += 1
    # Pie chart, where the slices will be ordered and plotted counter-clockwise
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #title('Frequency of key-words', bbox={'facecolor':'0.8', 'pad':5}, loc='left')

    plt.show()
    fig1.savefig('./Figures/piechart' + str(piechart.counter) + '.pdf', bbox_inches='tight')
    
    return(fig1)
    
piechart.counter = 0    