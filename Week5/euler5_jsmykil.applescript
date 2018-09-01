on isDivisible(i)
	set tmp to i mod 20
	if (i mod 20 = 0) and (i mod 19 = 0) and (i mod 18 = 0) and (i mod 17 = 0) and (i mod 16 = 0) and (i mod 15 = 0) and (i mod 14 = 0) and (i mod 13 = 0) and (i mod 12 = 0) and (i mod 11 = 0) then
		return true
	end if
	return false
end isDivisible

set x to false
set i to 20

repeat while x = false
	set answer to isDivisible(i)
	if answer = true then
		display dialog i
		set x to true
	end if
	
	set i to (i + 10)
end repeat