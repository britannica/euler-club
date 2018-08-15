def sum():
    result = 0
    start = 1
    point = 2
    while point < 4000000:
        if point%2==0:
            result=result+point
        temp = point
        point = start + point
        start = temp
    return result
        
