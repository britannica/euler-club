modified_prefixes = {3: "thir", 5: "fif", 8: "eigh"}

def format_as_letters(n, modifier=False):
    digits = list(str(n))
    first_int = int(digits[0])
    second_int = int(digits[1]) if len(digits) > 1 else None

    if n == 1000:
        return "one" + "thousand"
    elif n >= 100:
        last_two_digits = int(''.join(digits[1:]))
        british_compliance = "and" if n % 100 != 0 else ""
        return format_as_letters(first_int) + "hundred" + british_compliance + format_as_letters(last_two_digits)
    elif n > 12:
        if first_int == 1:
            return format_as_letters(second_int, modifier=True) + "teen"
        elif first_int in [2,4]:
            return [None, None, "twenty", None, "forty"][first_int] + format_as_letters(second_int)
        else:
            return format_as_letters(first_int, modifier=True) + "ty" + format_as_letters(second_int)
    else:
        if modifier and n in modified_prefixes:
            return modified_prefixes.get(n)
        else:
            return ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"][n]


letter_total = 0

for n in range(1,1001):
    letter_total += len(list(format_as_letters(n)))

print(letter_total)
