# euler18

import time
t0 = time.time()
TREE_SIZE = 15

inputdata = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1, 23, 75, 3, 34, 88, 2, 
         77, 73, 7, 63, 67, 99, 65, 4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 41, 
         48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14, 70, 11, 33, 
         28, 77, 73, 17, 78, 39, 68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48, 63, 
         66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 
         38, 53, 60, 4, 23]

# load tree
index = 0
tree = [[0] * TREE_SIZE for i in range(TREE_SIZE)]
for i in range(0, TREE_SIZE):
    for j in range(0, i+1):
        tree[i][j] = inputdata[index]
        index += 1    
# print tree

#traverse tree from bottom
branchtot = [[0] * TREE_SIZE for i in range(TREE_SIZE)]
branchpath = [[0] * TREE_SIZE for i in range(TREE_SIZE)]
for i in range(TREE_SIZE-1, -1, -1):
    for j in range(0, i+1):
        if i == TREE_SIZE-1:
            branchtot[i][j] = tree[i][j]
            branchpath[i][j] = str(tree[i][j])
        else:
            if branchtot[i+1][j] > branchtot[i+1][j+1]:
                branchtot[i][j] = tree[i][j] + branchtot[i+1][j]
                branchpath[i][j] = str(tree[i][j]) + '-' + branchpath[i+1][j]
            else:
                branchtot[i][j] = tree[i][j] + branchtot[i+1][j+1]
                branchpath[i][j] = str(tree[i][j]) + '-' + branchpath[i+1][j+1]
#             print i, j, branchtot[i][j], branchpath[i][j]

print branchtot[i][j], branchpath[i][j]

t1 = time.time()
elapsed = t1 - t0
print 'time=', elapsed


1074 75-64-82-87-82-75-73-28-83-32-91-78-58-73-93
time= 0.000999927520752
