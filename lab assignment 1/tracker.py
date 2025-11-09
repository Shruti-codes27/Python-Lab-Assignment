# Author: Shruti
# Date: 29 Oct 2025
# Project Title: Daily Calorie Tracker

print(" Welcome to Daily Calorie Tracker ")
print("This tool helps you track your meals and total calorie intake.\n")

# Ask how many meals the user wants to enter
num_meals = int(input("How many meals do you want to have today? "))

meal_names = []
calorie = []

for i in range(num_meals):
    meal = input(f"\nEnter meal name #{i+1}: ")
    cal = float(input(f"Enter calorie for {meal}: "))
   
    meal_names.append(meal)
    calorie.append(cal)

print("\nMeal names entered:", meal_names)
print("calories entered:", calorie)

total_calorie = sum(calorie)
average_calorie = total_calorie / num_meals

daily_limit = float(input("\nEnter your daily calorie limit: "  ))

print("\n-----Calorie Report-----")
print(f"Total calorie consumed: {total_calorie} kcal")
print(f"Average calorie per meal: {average_calorie:.2f} kcal")
print(f"Your daily limit: {daily_limit} kcal")

if total_calorie > daily_limit:
    print("\n Warning: You have exceeded your daily calorie limit!")
    print("Try to reduce your intake tomorrow to stay on track!")
elif total_calorie == daily_limit:
    print("\n You have exactly met your daily calorie limit.")    
else:
    print("\n Good job! You are within your daily calorie limit.") 
    print("Keep up the healthy eating habits!")


# Task 5: Neatly Formatted Output

print("\n\n-----Calorie Summary-----")
print(f"{'Meal Name':<15}{'Calorie (kcal)':>10}")
print("-" * 27)

for i in range(num_meals):
    print(f"{meal_names[i]:<15}{calorie[i]:>10.2f}")

print("-" * 27)
print(f"{'Total':<15}{total_calorie:>10.2f}")
print(f"{'Average':<15}{average_calorie:>10.2f}")

# Task 6:  Save Session Log to File

import datetime 

save = input("\nDo you want to save this session log to a file? (yes/no): ").strip().lower()
if save == "yes":
    filename = "calorie_log.txt"

    with open(filename, "w") as f:
        f.write("Daily calorie tracker Log\n")
        f.write(f"Timestamo: {datetime.datetime.now()}\n\n")

        f.write(f"{'Meal Name':<15}{'Calorie':>10}\n")
        f.write("-" * 27 + "\n")

        
        for i in range(num_meals):
            f.write(f"{meal_names[i]:<15}{calorie[i]:>10.2f}\n")

        f.write("-" * 27 + "\n")
        f.write(f"{'Total:':<15}{total_calorie:>10.2f}\n")
        f.write(f"{'Average:':<15}{average_calorie:>10.2f}\n")
        f.write(f"{'Daily Limit:':<15}{daily_limit:>10.2f}\n")
   
        if total_calorie > daily_limit:
            f.write("Status: Exceeded Limit \n")
        elif total_calorie == daily_limit:
            f.write("Status: Exactly at Limit \n")
        else:
            f.write("Status: Within Limit \n")

    print(f"\n Report saved successfully as '{filename}'")
else:
    print("\n 3 No worries! Report not saved.")    
