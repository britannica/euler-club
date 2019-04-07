# euler31

import time
t0 = time.time()
combos = 0

#print('L2+L1+p50+p20+p10+p5+p2+p1')
for L2 in range(0,2):
    for L1 in range(0,3):
        for p50 in range(0,5):
            for p20 in range(0,11):
                for p10 in range(0,21):
                    for p5 in range(0, 41):
                        for p2 in range(0, 101):
                            total = 200*L2+100*L1+50*p50+20*p20+10*p10+5*p5+2*p2
                            if total > 200:
                                break
                            for p1 in range(0, 201):
                                total = 200*L2+100*L1+50*p50+20*p20+10*p10+5*p5+2*p2+p1
                                if total > 200:
                                    break
                                if total == 200:
#                                    print('{0}+{1}+{2}+{3}+{4}+{5}+{6}+{7}'.format(L2,L1,p50,p20,p10,p5,p2,p1))
                                    combos += 1


        
print('\ntotal combos={0}'.format(combos))
 

t1 = time.time()
elapsed = t1 - t0
print('\ntime={0}'.format(elapsed))



total combos=73682

time=2.56900000572
