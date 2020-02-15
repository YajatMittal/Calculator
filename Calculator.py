#This is a program which allows you too do the following operations
print("******************************")
print("*    MATHS CALCULATIONS      *")
print("******************************")
print("* 1. Addition                *")
print("* 2. Subtraction             *")
print("* 3. Multiplication          *")
print("* 4. Division                *")
print("* Press option for operation *")
print("******************************")

#Enter your option
option = int(input("Enter the Option ---->"))


if option ==1:
    print("You want to do addition...")
  
    firstnum = int(input("Enter the first number -->"))
  
    secondnum = int(input("Enter the second number -->"))
    resultAddition = firstnum + secondnum

    print("The result of addition of %s and %s is = %s"% (firstnum,secondnum,resultAddition))

elif option ==2:
    print ("You want to do subtraction")

    firstnum = int(input("Enter the first number -->"))

    secondnum = int(input("Enter the second number -->"))

    finalresult = firstnum - secondnum

    print("The difference between the two numbers is = %s"% (finalresult))

elif option ==3:
    print("You want to do multiplication")

    firstnum = int(input("Enter the first number -->"))

    secondnum = int(input("Enter the second number -->"))

    final = firstnum * secondnum
    print("The product of the two numbers is = %s"% (final))

elif option ==4:
    print("You want to do division")

    firstnum = int(input("Enter the first number-->"))

    secondnum = int(input("Enter the second number -->"))

    quotient = firstnum / secondnum
    print("The quotient is %s"%(quotient))

