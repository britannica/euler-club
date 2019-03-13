# initialize center point, spiral is 1x1
diagonal_points = [1]

# begin with 2x2 spiral, go until 1001x1001 (inclusive), 
# each spiral increases the edge by 2
for spiral_edge_size in range(2, 1002, 2):
    for i in range(0,4):
        diagonal_points.append(diagonal_points[-1] +  spiral_edge_size)

print(sum(diagonal_points))
