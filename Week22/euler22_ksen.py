def wordVal(w):
    s = 0
    for chr in w:
        s = s + ord(chr) - 64
    return s       

with open("/Users/ksen/Desktop/p022_names.txt") as f:
    content = f.read().replace('"',"").split(',')
    content.sort()
order = 0
sum = 0
for s in content:
    order = order+1
    sum = sum + order * wordVal(s)
print (sum)
