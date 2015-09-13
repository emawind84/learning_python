#!/usr/bin/env python3

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()
sense.low_light = True

d = [
    {
        'ori': 'yaw',
        'last_pos': (0, 0),
        'path': [0, 1, 2, 3, 4, 5, 6, 7, 15, 23, 31, 39, 47, 55, 63, 62, 61, 60, 59, 58, 57, 56, 48, 40, 32, 24, 16, 8]
    },
    {
        'ori': 'roll',
        'last_pos': (0, 0),
        'path': [6, 14, 22, 30, 38, 46, 54, 62, 5, 13, 21, 29, 37, 45, 53, 61]
    },
    {
        'ori': 'pitch',
        'last_pos': (0, 0),
        'path': [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    }
]

i = 0
while True:
    axis = d[i % 3]
    path = axis['path']
    ratio = len(path) / 360.0
    
    orientation = sense.get_orientation()
    ori = orientation[axis['ori']]
    print("pitch={pitch}, roll={roll}, yaw={yaw}".format(**orientation))
    
    pos = int(ori * ratio)
    
    #print( 'ori %s => %s' % (d[i % 2]['ori'], pos) );
    
    y = path[pos] // 8
    x = path[pos] % 8
    
    sense.set_pixel(x, y, 255, 255, 255)
    
    prev_pos = axis['last_pos']
    if prev_pos != (x, y):
        sense.set_pixel(prev_pos[0], prev_pos[1], 0, 0, 0)
        
    axis['last_pos'] = (x, y)
    
    i = i + 1