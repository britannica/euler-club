grid_size = 20 

routes_to_points = {}

def calculate_route_counts(point, previous):
    if routes_to_points.get(previous):
        if routes_to_points.get(point):
            # already did one of the two inbound routes, so add the 
            # second inbound route total to the first
            routes_to_points[point] += routes_to_points[previous]
        else:
            # this point is new, but the route has a previous point,
            # so carry its total forward
            routes_to_points[point] = routes_to_points[previous]
    else:
        # there is no previous point, there can only be one route
        routes_to_points[point] = 1

for i in range(0, grid_size):
    for j in range(i, grid_size):
        # this builds all the possible points (without double counting
        # the points on the diagonal)
        points = [(i,j),(j,i)] if i != j else [(i,j)]
        for point in points:
            x = point[0]
            y = point[1]
            previous_point_in_route_from_left = (x-1,y)
            calculate_route_counts(point, previous_point_in_route_from_left)
            previous_point_in_route_from_above = (x,y-1)
            calculate_route_counts(point, previous_point_in_route_from_above)


last_point = (grid_size-1, grid_size-1)

# the route map is mirrored on the diagnoal and i only did one half,
# so we need to double the count

print(routes_to_points[last_point]*2)
