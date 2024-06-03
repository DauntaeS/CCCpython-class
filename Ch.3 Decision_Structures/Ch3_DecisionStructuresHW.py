# One cause for speeding is the desire to shorten the time spent traveling. Create a program that calculates the total amount of time saved if you are traveling with an average speed that is above the speed-limit as compared to traveling with an average speed exactly at the speed-limit. Ask the user for the average speed, speed limit and distance travelled. Calculate the amount of time saved for the distance travelled. THE TIME SAVED SHOULD BE REPORTED IN MINUTES

# Input:
# user average speed
# speed limit
# distance traveled

# Process:
# How much time is saved?
# convert to minutes

# Output:
# Time saved in (Mins)

user_speed = int(input("How fast are you going? "))
speed_limit = int(input("What is the posted Speed limit? "))
distance = int(input("What is the distance that you are traveling? "))

posted_avg_time = distance / speed_limit * 60
user_time = distance / user_speed * 60

time_Saved = posted_avg_time - user_time

if user_speed == speed_limit:
    print(f"Average Speed Limit Time: {posted_avg_time:.2f} Minutes ")
elif user_speed > speed_limit:
    print(f"Time saved: {time_Saved:.2f} Minutes ")
else:
    print("Your going a little slow buddy")
