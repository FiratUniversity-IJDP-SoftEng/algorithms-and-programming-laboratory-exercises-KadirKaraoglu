# Your Student Id: 230543005
# Your Name and Surname: Kadir Karaoğlu
w = input("Please enter a text: ")
print("Character frequencies: ")
charCount = {}
for i in w:
    charCount[i] = charCount.get(i, 0) + 1
for i in sorted(charCount):
    print(f"{i}: {charCount[i]}")
