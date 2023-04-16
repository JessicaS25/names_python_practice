file = None
try:
    file = open("calculator.txt", "a")
    #this will open the calculator file
except FileNotFoundError:
    print("The file does not exist")

# This function adds two numbers
def add(x, y):
    result = (f"{x} + {y} = {x+y} \n") 
    file.write(result)
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    result = (f"{x} - {y} = {x-y} \n")
    file.write(result)
    return x - y
# This function multiplies two numbers
def multiply(x, y):
    result = (f"{x} * {y} = {x*y} \n")
    file.write(result)
# This function divides two numbers
def divide(x, y):
    result = (f"{x} / {y} = {x/y} \n")
    file.write(result)
    return x / y

print("Select mathematical function.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
        except ValueError:
            print("You have not entered a number, please try again with a number")
            continue

        if choice == '1':
            print(number_1, "+", number_2, "=", add(number_1, number_2))

        elif choice == '2':
            print(number_1, "-", number_2, "=", subtract(number_1, number_2))

        elif choice == '3':
            print(number_1, "*", number_2, "=", multiply(number_1, number_2))

        elif choice == '4':
            print(number_1, "/", number_2, "=", divide(number_1, number_2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do you require another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Error - Invalid input")

finished_step = input("Do you want to read the file? (yes/no): ")
if finished_step == "yes":
    f = open("calculator.txt", "r")
    print(f.read())
file.close()
