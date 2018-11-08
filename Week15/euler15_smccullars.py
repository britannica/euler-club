grid_size = 20 

start_point = (0,0)
routes = {}

for i in range(0, grid_size):
    for j in range(i, grid_size):
        points = [(i,j),(j,i)] if i != j else [(i,j)]
        for point in points:
            if point[0] > 0:
                parent = (point[0]-1,point[1])
                if routes.get(point):
                    routes[point] += routes[parent]
                else:
                    routes[point] = routes[parent]
            else:
                routes[point] = 1
            if point[1] > 0:
                parent = (point[0],point[1]-1)
                if routes.get(point):
                    routes[point] += routes[parent]
                else:
                    routes[point] = routes[parent]
            else:
                routes[point] = 1
print(routes[(grid_size-1,grid_size-1)]*2)
