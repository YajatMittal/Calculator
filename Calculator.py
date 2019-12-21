#This program has been created by Yajat Mittal
#The program has been created on 20th Sep 2019
#This has been created for learning and fun
import sys
print("******************************")
print("*    MATHS CALCULATIONS      *")
print("******************************")
print("* 1. Addition                *")
print("*                            *")
print("* 2. Subtraction             *")
print("*                            *")
print("* 3. Multiplication          *")
print("*                            *")
print("* 4. Division                *")
print("*                            *")
print("* 5. Exit Program            *")
print("*                            *")
print("* Press option for operation *")
print("*                            *")
print("******************************")

print("Enter the Option ---->")
option = int(sys.stdin.readline())

#print("You have entered option # %s" %option)

if option ==1:
  print("You want to do addition...")
  
  print("Enter the first number -->")
  firstnum = int(sys.stdin.readline())
  
  print("Enter the second number -->")
  secondnum = int(sys.stdin.readline())
  resultAddition = firstnum + secondnum

  print("The result of addition of %s and %s is = %s"% (firstnum,secondnum,resultAddition))

elif option ==2:
  print ("You want to do subtraction")

  print("Enter the first number-->")
  firstnum=int(sys.stdin.readline())

  print("Enter the second number-->")
  secondnum=int(sys.stdin.readline())

  finalresult=firstnum - secondnum

  print("The difference between the two numbers is = %s"% (finalresult))

elif option ==3:
  print("You want to do multiplication")

  print("Enter the  first number-->")
  firstnum=int(sys.stdin.readline())

  print("Enter the  second number-->")
  secondnum=int(sys.stdin.readline())

  final = firstnum * secondnum
  print("The product of the two numbers is = %s"% (final))

elif option ==4:
  print("You want to do division")

  print("Enter the first number-->")
  firstnum=int(sys.stdin.readline())

  print("Enter the second number-->")
  secondnum=int(sys.stdin.readline())

  quotient=firstnum / secondnum
  print("The quotient is %s"%(quotient))


else: 
  print("Exiting.....")
