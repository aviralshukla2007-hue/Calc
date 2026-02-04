while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")

    #Taking the input of two numbers
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))

    #Taking the choice
    choice=int(input("Enter your choice between 1 to 5:"))

    #1.Addition
    if choice==1:
        print("The sum of two numbers are:",num1+num2)
        break
    elif choice==2:
        print("The difference between two numbers:",num1-num2)
        break
    elif choice==3:
        print("The product between the two numbers:",num1*num2)
        break
    elif choice==4:
        print("The quotient between the two numbers is:",num1/num2)
        break
    elif choice==5:
        break
    else:
        print("Invalid input! Please enter between 1 to 5.")
    user_choice = input("Do you want to continue?(YES/NO):")
    if user_choice=="Yes":
        continue
    else: 
        break

        

