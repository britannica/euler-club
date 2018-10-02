func trippleSum(x:Int, y:Int) -> Int {
    return [(y*y - x*x), 2*y*x, y*y + x*x].reduce(0,+)
}
func trippleProduct(x:Int, y:Int) -> Int {
    return [(y*y - x*x), 2*y*x, y*y + x*x].reduce(1,*)
}

var x = 1
var y = 2
var sum = 0

while sum < 1100 {
    sum = trippleSum(x:x, y:y)
    if (sum == 1000) {
        print(trippleProduct(x:x, y:y))
        break
    }
    else if (sum > 1000) {
        x = x + 1;
        y = x + 2;
    } else {
        y = y + 1
    }
}