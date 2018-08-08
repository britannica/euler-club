var (sum, newCurrent) = (0,0);
var (current, previous) = (1,1);
repeat {
	if current % 2 == 0 {
		sum += current;
	}
	newCurrent = current + previous;
	previous = current;
	current = newCurrent;
} while current < 4000000

print(sum);
