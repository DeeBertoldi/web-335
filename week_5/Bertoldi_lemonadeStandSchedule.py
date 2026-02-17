"""
Author: Daniella Bertoldi
Date: 02/15/2026
File Name: Bertoldi_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand
using conditionals, lists, and loops.
"""

# List of tasks for the lemonade stand
tasks = ["Buy more lemons and sugar",
         "Prepare lemonade",
         "Set up the stand",
         "Clean the stand",
         "Restock supplies"]

# Print the weekly tasks
print("Weekly Lemonade Stand Tasks:")
for task in tasks:
    print(task)

# List of days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("\nDaily Schedule:")

for i in range(len(days)):
    if days[i] == "Saturday" or days[i] == "Sunday":
        print(days[i] + ": Day off! Time to rest.")
    else:
        print(days[i] + ": " + tasks[i-1])
