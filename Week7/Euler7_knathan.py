n = 6
x = 15

def isprime(x) :
	i = 3
	while  i < x :
		j = x % i
#		print (i,x,j)
		if j != 0 :
			i += 2
			if i == x :
				return True
		else :
			i = x
			return False
			
while n < 10001 :
	x += 2
	if isprime(x):
		n += 1
print (x)



