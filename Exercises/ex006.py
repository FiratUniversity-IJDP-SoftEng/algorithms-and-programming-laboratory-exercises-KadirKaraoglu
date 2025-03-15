# Your Student Id: 230543005
# Your Name and Surname: Kadir Karaoğlu
myList = [1, 3, 9, 2, 9, 5, 4, 10, 3, 6]
print("Original list is:\n", myList)

reversedList = myList[::-1]  
print("reversed list:", reversedList)

print("Numbers will add")
addNumList = [12, 11, 13]
reversedList.extend(addNumList)  
print(reversedList)


length = len(reversedList)
print(f"The length of the list is {length}")

print("Removing numbers")
reversedList.pop(0)  
reversedList.pop(-1) 
print(reversedList)

even_numbers = sorted([num for num in reversedList if num % 2 == 0])
print("Sorted even numbers:", even_numbers)
