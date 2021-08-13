import numpy as np
from random import randint
from os.path import join

filename_root = join('Maps','Map')


for map_num in range(51, 60):
    filename = filename_root+str(map_num)
    rr = randint(4, 100)
    rc = randint(4, 100)
    a = np.zeros((rr, rc), dtype=np.int8)
    percent = .3
    for i in range(int(percent*a.shape[0]*a.shape[1])):
        r = randint(0, a.shape[0]-1)
        c = randint(0, a.shape[1]-1)
        a[r][c] = 1
    np.save(filename, a)
    a = np.load(filename+'.npy')

    print(a)
    print()
