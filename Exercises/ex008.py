# Your Student 230543005:
# Your Kadir and Karaoglu:
number = (int)(input("Enter a number: "))
for i in range(number):
    for j in range(number - i - 1):        
        print(" ",end="")
    for j in range(2*i + 1):
        print("*",end="")
    print()
