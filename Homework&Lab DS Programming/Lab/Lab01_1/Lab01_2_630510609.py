#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# Lab01_1
# 229223 Sec 002

#Import Math Module
import math

#Input 
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#Calculate Area
s = (a + b + c)//2
area = math.ceil((s*(s-a)*(s-b)*(s-c))**(0.5))

#Display Answer
print("area: ",area)

