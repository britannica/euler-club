# euler24

import time
t0 = time.time()

def permutations():
    count = 0
    perm = [0,0,0,0,0,0,0,0,0,0]
    for i0 in range(0,10):
        perm[0] = i0
        for i1 in range(0,10):
            if i1 in perm[0:1]:
                continue
            else:
                perm[1] = i1   
                for i2 in range(0,10):
                    if i2 in perm[0:2]:
                        continue
                    else:
                        perm[2] = i2
                        for i3 in range(0,10):
                            if i3 in perm[0:3]:
                                continue
                            else:
                                perm[3] = i3
                                for i4 in range(0,10):
                                    if i4 in perm[0:4]:
                                        continue
                                    else:
                                        perm[4] = i4
                                        for i5 in range(0,10):
                                            if i5 in perm[0:5]:
                                                continue
                                            else:
                                                perm[5] = i5
                                                for i6 in range(0,10):
                                                    if i6 in perm[0:6]:
                                                        continue
                                                    else:
                                                        perm[6] = i6
                                                        for i7 in range(0,10):
                                                            if i7 in perm[0:7]:
                                                                continue
                                                            else:
                                                                perm[7] = i7
                                                                for i8 in range(0,10):
                                                                    if i8 in perm[0:8]:
                                                                        continue
                                                                    else:
                                                                        perm[8] = i8
                                                                        for i9 in range(0,10):
                                                                            if i9 in perm[0:9]:
                                                                                continue
                                                                            else:
                                                                                perm[9] = i9
                                                                                count += 1
                                                                                if count == 1000000:
                                                                                    return perm
                                                                                #print perm:


perm = permutations()
print('perm=', perm)
t1 = time.time()
elapsed = t1 - t0
print('time=', elapsed)




perm= [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
time=6.9679999351501465
