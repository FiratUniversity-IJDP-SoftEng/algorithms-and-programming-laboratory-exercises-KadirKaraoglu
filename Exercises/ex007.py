# Your Student 230543005:
# Your Kadir and Karaoglu:
w = input("Please enter a text: ")
print("Character frequencies: ")
charCount = {}
for i in word:
    charCount[i] = charCount.get(i, 0) + 1
for i in sorted(charCount):
    print(f"{i}: {charCount[i]}")
