#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW01_3
# 229223 Sec 002

#Import math module
import math

#Input
oldprice = float(input("Old price: "))

#Calculate Price according to problem
oldprice /= 100
newprice = (math.floor(oldprice + 0.5)  * 100 ) - 2

#Display Answer
print("New Price: %.0f" %newprice)