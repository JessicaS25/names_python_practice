#This programme will add up the amount of time taken for an individual to complete a triathlon. 
#It needs to add the number of minutes to complete the swim, bike and run together
#The time taken to complete will determine what awards are given. 
swim_time = input("Time taken in minutes to complete swim: ")
bike_time = input("Time taken in minutes to complete bike: ")
run_time = input("Time taken in minutes to complete run: ")
total_time = int(swim_time) + int(bike_time) + int(run_time)
print(total_time)
provincial_full_colours = 100
provincial_half_colours = 105
provincial_scroll = 110
no_award = 111

if total_time <= provincial_full_colours:
    print("You have won the Provincial Colours")
elif total_time <= provincial_half_colours:
    print("You have won the Provincial Half Colours")
elif total_time <= provincial_scroll:
    print("You have won the Provincial Scroll")
elif total_time >= no_award:
    print("You have not achieved an award")
