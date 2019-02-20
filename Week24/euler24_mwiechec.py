import math

nums = [0,1,2,3,4,5,6,7,8,9]
start = 1000000
answer = []
for position in range(9, -1, -1):
    x = math.factorial (position)
    digit = start // x
    answer.append(nums[digit])
    del nums[digit]
    start = start % x
print (answer)


# [2, 7, 8, 3, 9, 1, 5, 6, 0, 4]

