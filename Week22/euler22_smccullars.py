names = set()
with open('names.txt') as names_text_file:
    for name in names_text_file.read().split(','):
        names.add(name.strip('"'))

total_name_score = 0
for idx, name in enumerate(sorted(names)):
    letters_sum = 0
    for letter in list(name):
        #capital letters in ascii begin after 64...aka uppercase A is 65
        letters_sum += ord(letter) - 64
    # idx is zero-based, but we want to start at 1
    total_name_score += letters_sum * (idx+1)

print(total_name_score)
