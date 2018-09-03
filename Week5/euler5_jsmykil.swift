func isDivisible(index: Int) -> Bool {
    if (    
        index%20 == 0 &&
        index%19 == 0 &&
        index%18 == 0 &&
        index%17 == 0 &&
        index%16 == 0 &&
        index%15 == 0 &&
        index%14 == 0 &&
        index%13 == 0 &&
        index%12 == 0 &&
        index%11 == 0
        ) {
        return true;
    }
    return false;
}

var i:Int = 20;
var stop:Bool = false;
while stop == false {
    if (isDivisible(index:i)) {
        stop = true;
        print(i);
    }
    i+=10;
}