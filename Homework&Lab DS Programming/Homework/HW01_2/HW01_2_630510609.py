#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW01_2
# 229223 Sec 002

#Input
x = int(input("x: "))
y = int(input("y: "))

#Calculate sum untill x to y
x -= 1
sum = y*(y + 1) // 2 - x*(x + 1) // 2

#Display Answer
print("sum is: " ,sum)