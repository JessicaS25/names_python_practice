user_name = input("Enter your full name: ")
if len(user_name) <1:
    print ("You haven't entered anything. Please enter your full name")
elif len(user_name) <4:
    print ("You have entered less than 4 characters. Please make sure you have entered your full name")
elif len(user_name) >25:
    print ("You have entered more than 25 characters. Please make sure that you have only entered your full name")
else:
    print ("Thank you for entering your full name")
