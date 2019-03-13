diagonal_points = [1]

for spiral_edge_size in range(1, 1001, 2):
    spiral_edge_size += 2
    for i in range(0,4):
        diagonal_points.append(diagonal_points[-1] +  spiral_edge_size - 1)

print(sum(diagonal_points))
