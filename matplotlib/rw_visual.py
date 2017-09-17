#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

from random_walk import RandomWalk

if sys.version[0] == '2':
    input = raw_input

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.figure(figsize=(10, 6))
    plt.scatter(rw.x_values, 
                rw.y_values, 
                s=10,
                edgecolors=None,
                c=point_numbers,
                cmap=plt.cm.Blues
                )

    plt.scatter(0, 0, 
                c='green', 
                edgecolors=None,
                s=100
                )

    plt.scatter(rw.x_values[-1], 
                rw.y_values[-1],
                c='red',
                edgecolors=None,
                s=100
                )

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    #plt.savefig('plot.png', bbox_inches='tight')

    keep_running = input("Make a new one? (y/n): ")
    if keep_running == 'n':
        break