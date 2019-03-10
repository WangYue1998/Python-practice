#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 18:59:40 2017

@author: wy
"""

# -*- coding: utf-8 -*-
"""
Gasoline Calculations

Prompts for:
- The number of gallons of gas to fill your carâ€™s gas tank (a float)
- The number of miles traveled since the last fill up (a float)

Reprints the input information along with the following:
- The number of pounds of CO2 emitted since the last fill up 
- The average miles per gallon since the last fill up
- The average pounds of CO2 emitted per mile since the last fill up
- The cost in USD to fill the gas tank 
"""

LBS_PER_GAL = 20
USD_PER_GAL = 2.29


# Prompt for the input values and convert them to floats

gas_prpt = float(input("How many gallons of gas were pumped to fill the tank? " ))
miles_prpt = float(input("How many miles did you drive since the last fillup? "))  

print()

# Calculate and print the pounds of CO_2 emmitted
CO_2= LBS_PER_GAL*gas_prpt
print(CO_2)
# Calculate and print the miles per gallon
miles_per_gallon=miles_prpt/gas_prpt
print(miles_per_gallon)
# Calculate and print the pounds of CO_2 emmitted per mile
CO_2_per_miles=CO_2/miles_prpt
print(CO_2_per_miles)
# Calculate and print the cost
cost= USD_PER_GAL*gas_prpt
print(cost)