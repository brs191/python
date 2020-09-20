#import numpy as np
import matplotlib.pyplot as plt
#import numpy.linalg as la
import matplotlib.image as mpimg

mario = mpimg.imread('mario_big.png')

luigi = mario

dim = luigi.shape
width = dim[0]
height = dim[1]

plt.imshow(mario)
print(mario[25, 100])
print(mario[225, 150])
print(mario[300, 50])

for i in range(width):
    for j in range(height):
        temp = luigi[i][j]
        if temp[0] >= .8:
            temp[0] = 0
        
        temp[1] = 1
        
        temp[2] = 0
            
        luigi[i][j] = temp

print(luigi[25, 100])
print(luigi[225, 150])
print(luigi[300, 50])

plt.imshow(luigi)