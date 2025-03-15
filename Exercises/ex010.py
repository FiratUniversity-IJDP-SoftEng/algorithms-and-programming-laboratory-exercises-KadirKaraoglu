# Your Student Id: 230543005
# Your Name and Surname: Kadir Karaoğlu
while True:
  operation = input(
      "which method do yopu want use ?\n please enter a for addition\n please enter s for subtraction\n please enter m for multiplication\n please enter d for division\n"
  ).lower()

  if operation == "a":
    num1 = int(input("please enter the firts number : "))
    num2 = int(input("please enter the second number : "))
    result = num1 + num2
    print(f"total is : {result}")

  elif operation == "s":
    num1 = int(input("please enter the firts number : "))
    num2 = int(input("please enter the second number : "))
    result = num1 - num2
    print(f"total is : {result}")
  elif operation == "m":
    num1 = int(input("please enter the firts number : "))
    num2 = int(input("please enter the second number : "))
    result = num1 * num2
    print(f"total is : {result}")
  elif operation == "d":
    num1 = int(input("please enter the firts number : "))
    num2 = int(input("please enter the second number but it can not be 0 : "))
    if num2 == 0:
      print("you can not divide by 0")
      break
    result = float(num1 / num2)
    print(f"total is : {result}")
  else:
    print("please enter a valid input")
  newOperation = input(
      "Do you want to do another operation ? [yes/ no] : ").lower()
  if newOperation != "yes":
    print("Exitting program.")
    break
