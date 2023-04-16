from statistics import mean

#Programme to calculate the average of numbers entered

total = 0

#This gets user to enter a number
user_number = int(input("Enter a number:"))

while user_number !=-1:

    total += user_number # this calculates the total ready for average calculation
    # take integer input again
    user_number = int(input("Enter a number:"))

    if user_number ==-1:
        break       #this stops the need to input more numbers if value ==-1

print("Total: ", total) #this shows the total of all the numbers entered

total_number = int(input("How many numbers did you enter: ")) #this will determine the number to divide the total by to get the average
avg_number = total/total_number #this calculates the average

print("Average number: ", avg_number) #this shows the average number
