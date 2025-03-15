# Your Student 230543005:
# Your Kadir and Karaoglu:
myList = [1,3,9,2,9,5,4,10,3,6]
print("original list is:\n" ,myList)

print("reversed list: ")
reversedList = myList[::-1] 
print(reversedList)

print("adding numbers")
addNumList =[12,11,13]
reversedList.extend(addNumList)
print(reversedList)

length = len(reversedList)
print(f"The length of the list is {length}")

print("removing numbers")
reversedList.pop(0)
reversedList.pop(-1)
print(reversedList)

length = len(reversedList)
for i in range(length - 1):  
    shortest = i     
    for j in range(i + 1, length):  
        if reversedList[j] < reversedList[shortest]:
            shortest = j  
    
    reversedList[i], reversedList[shortest] = reversedList[shortest], reversedList[i]
print("Sorted list: \n",reversedList)

newList = []
for num in reversedList:
    if num % 2 == 0:
        newList.append(num)
print("The new list is:\n",newList)
