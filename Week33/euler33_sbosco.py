# euler33

import time
t0 = time.time()

tot = float(1)
for n1 in range(1,10):
    for n2 in range(1,10):
        n = int(str(n1) + str(n2))
        for d1 in range(1,10):
            for d2 in range(1,10):
                d = int(str(d1) + str(d2))
                if float(n) < d:
                    if n1 == d1:
                        if (float(n2)/d2) == (float(n)/d):
                            print(n2,d2,n,d)
                            tot = tot * n2 / d2
                    if n1 == d2:
                        if (float(n2)/d1) == (float(n)/d):
                            print(n2,d1,n,d)
                            tot = tot * n2 / d1
                    if n2 == d1:
                        if (float(n1)/d2) == (float(n)/d):
                            print(n1,d2,n,d)
                            tot = tot * n1 / d2
                    if n2 == d2:
                        if (float(n1)/d1) == (float(n)/d):
                            print(n1,d1,n,d)
                            tot = tot * n1 / d1

print('tot=',tot)


t1 = time.time()
elapsed = t1 - t0
print('\ntime={0}'.format(elapsed))



# 1, 4, 16, 64
# 1, 5, 19, 95
# 2, 5, 26, 65
# 4, 8, 49, 98
# tot= 0.01

#time=0.0110001564026
