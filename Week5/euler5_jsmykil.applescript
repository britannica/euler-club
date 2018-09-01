on isDivisible(i)
	set tmp to i mod 20
	if tmp = 0 then
		set tmp to i mod 19
		if tmp = 0 then
			set tmp to i mod 18
			if tmp = 0 then
				set tmp to i mod 17
				if tmp = 0 then
					set tmp to i mod 16
					if tmp = 0 then
						set tmp to i mod 15
						if tmp = 0 then
							set tmp to i mod 14
							if tmp = 0 then
								set tmp to i mod 13
								if tmp = 0 then
									set tmp to i mod 12
									if tmp = 0 then
										set tmp to i mod 11
										if tmp = 0 then
											return true
										end if
									end if
								end if
							end if
						end if
					end if
				end if
			end if
		end if
	end if
	return false
end isDivisible

set x to (1 = 2)
set i to 20

repeat while x = false
	set answer to isDivisible(i)
	if answer = true then
		display dialog i
		set x to (1 = 1)
	end if
	
	set i to (i + 10)
end repeat