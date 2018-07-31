func figureItOut(num: Int) -> Int {
    if (num % 3 == 0) {
        return num;
    } else if (num % 5 == 0) {
        return num;
    }
    return 0;
}

let range = 0...999;
var total: Int = 0;

for i in range {
    total += figureItOut(num: i)
}

print(total);


