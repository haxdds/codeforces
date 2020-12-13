

word = input().lower()

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

filtered_word = "".join(c for c in word if c not in vowels)

i = 0
while i < len(filtered_word):
    filtered_word =  filtered_word[:i] + '.' + filtered_word[i:]
    i += 2

print(filtered_word)





