import time

def test_a(a, sum_terms):
	b_start = a + 1
	b_max = sum_terms - (2 * a) - 1
	for b in range(b_start, b_max):
			c = sum_terms - a - b
			c_test = c**2
			c_sq = a**2 + b**2
			if c_sq == c_test:
				return (a,b,c)
	return None
				
def find_triplet(sum_terms):
	a_start = 1
	a_max = sum_terms - a_start - 2
	for a in range(a_start, a_max):
		res = test_a(a, sum_terms)
		if res:
			print("Found it: a={}, b={}, c={}".format(res[0],res[1],res[2]))
			break
	else:
		print ("No Pythagorean triplet for {}".format(sum_terms) )
	return

if __name__ == '__main__':
    start = time.time()
    find_triplet(1000)
    end = time.time()
    print(end - start)