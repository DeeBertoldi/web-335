"""
Author: Daniella Bertoldi
Date: 02/01/2026
File Name: bertoldi_lemonadeStand.py
Description: This program calculates the cost and profit of a lemonade stand using functions.
"""

# Function to calculate total cost
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost
    return total_cost


# Function to calculate profit
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    profit = selling_price - total_cost
    return profit


# Variables to test the functions
lemons_cost = 5
sugar_cost = 3
selling_price = 12


# Call calculate_cost and build output string
total_cost = calculate_cost(lemons_cost, sugar_cost)
cost_output = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(total_cost)

print(cost_output)


# Call calculate_profit and build output string
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)
profit_output = "Selling Price: " + str(selling_price) + " - Total Cost: " + str(total_cost) + " = " + str(profit)

print(profit_output)
