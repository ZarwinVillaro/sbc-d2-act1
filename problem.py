word = "summer bootcamp"

print(word.title())
print(word[0].upper() + word[1:-1] + word[-1].upper())
print(word.replace("b", "L")[7:-4])
print(word.replace("p", "E")[11:])
print(word.replace("a", "A")[12:-2] + word[5].upper())

word1 = word.replace(" ", "")
print(word1.isalpha())