#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW01_1
# 229223 Sec 002

#Input
m1 = float(input("m1: "))
b1 = float(input("b1: "))
m2 = float(input("m2: "))
b2 = float(input("b2: "))

#Calculate X point
x = ((b2 - b1)/(m1 - m2)) 

#Calculate Y point
y = (m1 * x) + b1

#Display Answer
print("Lines intersect at (%.2f,%.2f)" %(x,y))