# euler28

from collections import defaultdict
import time
t0 = time.time()

grid_size = 1001
grid = defaultdict(dict)

for x in range(0, grid_size+2):
    for y in range(0, grid_size+2):
        grid[x][y] = 0

center = (grid_size + 1) / 2
x = y = center
grid[x][y] = 1
for i in range(2, grid_size*grid_size+1):
    if grid[x][y+1] == 0 and grid[x-1][y] != 0:  # check for down
        y = y + 1
    elif grid[x-1][y] == 0 and grid[x][y-1] != 0:  # check for left
        x = x - 1
    elif grid[x][y-1] == 0 and grid[x+1][y] != 0:  # check for up
        y = y - 1
    else:
        x = x + 1
    grid[x][y] = i
#    print('x=',x,'y=',y,'val=',grid[x][y])
    
diag_sum = 0;
for i in range(1, grid_size+1):
    diag_sum += grid[i][i] + grid[i][grid_size-i+1]

print('sum=',diag_sum-1)    
      

t1 = time.time()
elapsed = t1 - t0
print('time={0}'.format(elapsed))


sum=669171001
time=1.22399997711
