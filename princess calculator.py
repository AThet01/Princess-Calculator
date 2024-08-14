print("===Welcome from 'Princess calculator'==="  )
while 1:
    print("What would u like to do ? ")
    print("1.Addition ")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Remainder")
    print("6.EXIT.... ")

    choice=int(input("Choose from 1 to 6: "))
    if choice==1:
        input1=int(input("Enter number 1: "))
        input2=int(input("Enter number 2: "))
        print("Output is : ",input1+input2)
    elif choice==2:
        input1=int(input("Enter number 1: "))
        input2=int(input("Enter number 2: "))
        print("Output is : ",input1-input2)
    elif choice==3:
        input1=int(input("Enter number 1: "))
        input2=int(input("Enter number 2: "))
        print("Output is : ",input1*input2)
    elif choice==4:
        input1=int(input("Enter number 1: "))
        input2=int(input("Enter number 2: "))
        print("Output is : ",input1/input2)
    elif choice==5:
        input1=int(input("Enter number 1: "))
        input2=int(input("Enter number 2: "))
        print("Output is : ",input1%input2)
    elif choice==6:
        print("Exiting.......")
    break
print()
    
    
    