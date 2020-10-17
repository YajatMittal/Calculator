#This is a program which allows you too do the following operations
print("* 1. Addition                *")
print("* 2. Subtraction             *")
print("* 3. Multiplication          *")
print("* 4. Division                *")


def op_1():
    user_input = input("How many numbers do you want to add?:")
    numbers = []
    for x in range(1,user_input+1):
        num = int(input("Enter the number:"))
        numbers.append(num)

    return f"The answer is {sum(numbers)}"

def op_2():
    user_input = input("How many numbers do you want to subtract?:")
    numbers = []
    calculate = 1
    
    for x in range(1,user_input+1):
        num = int(input("Enter the number:"))
        numbers.append(num)

    for x in range(1,numbers+1):
        calculate = calculate - numbers[x]
    
    return f"The answer is {calculate}"
    

       


def op_3():
    user_input = input("How many numbers do you want to multiply?:")
    numbers = []
    calculate = 1

    for x in range(1,user_input+1):
        num = int(input("Enter the number:"))
        numbers.append(num)
    for x in range(1,numbers+1):
        calculate = calculate * numbers[x]
    
    return f"The answer is {calculate}"
    
def op_4():
    user_input = input("How many numbers do you want to divide?:")
    numbers = []
    calculate = 1

    for x in range(1,user_input+1):
        num = int(input("Enter the number:"))
        numbers.append(num)
    for x in range(1,numbers+1):
        calculate = calculate / numbers[x]

    return f"The answer is {calculate}"

def main():
    option = int(input("Enter the Option ---->"))        
    if option == 1:
        op_1()
    elif option == 2:
        op_2()
    elif option ==3:
        op_3()
    elif option ==4:
        op_4()

main()

play_again = True
while play_again:
    again = str(input("Do you want to play again?ENter Y/N:"))
    if again.lower() == "y":
        main()
    else:
        play_again = False