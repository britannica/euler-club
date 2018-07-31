def _calc(num1, num2, _max):
    _sum = 0
    for i in range(0, _max):
        if i % num1 == 0 or i % num2 == 0:
            _sum = _sum + i

    print("sum of multiples of %d and %d below %d is :%d" % (num1, num2, _max, _sum))
    return


_calc(3, 5, 1000)
