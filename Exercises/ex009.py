# Your Student Id: 230543005
# Your Name and Surname: Kadir Karaoğlu

    respond= input("""which opartion do you use ?\n if you want Celsius to convert Fahrebheit enter "c" \n 
     if you want Fahrenheit to convert Celsius enter "f" """).upper()

    if respond == "F":
        fahrenheit= (int)(input("What is the temperature for Fahrenheit that you want convert:: "))
        c = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}° fahrenheit is {c:.2f}° celsius")
     

    elif respond == "C":
        celsius = (int)(input("What is the temperature for Celsius thar you want convert: "))
        f = (celsius * 9/5) + 32
        print(f"{celsius}° celsius is {f:.2f}° fahrenheit")
  
    else :
        print("Invalid input please try again.\n")
