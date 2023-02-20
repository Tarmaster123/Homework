#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW11_1
# 229223 Sec 002

def main():
    display_calendar(2, 2023)


def display_calendar(month, year):
    # Formula h = (q + floor(13(m + 1) /5 + K + floor(k/4) + floor(J/4) - 2J))

    # for Jan and Feb
    if month == 1 or month == 2:
        year -= 1
    if month == 1:
        m = 13
    if month == 2:
        m = 14

    # variable
    q = 1 # 1
    m = (13 * (m + 1)) // 5 # 13 * (14 + 1) // 5 == 39
    k = year % 100 # 22
    k_floor = k //4 # 22 //4 == 5
    j = year // 100 #20
    j_floor = j // 4 # 20 // 4 == 5

    # Find h
    h = q + m + k + k_floor + j_floor - (2*j)
    print(h)

    # Set Day
    # if h == 0:
    #     start = "Sa"
    # elif h == 1:
    #     start = "Su"
    # elif h == 2:
    #     start = "Mo"
    # elif h == 3:
    #     start = "Tu"
    # elif h == 4:
    #     start = "We"
    # elif h == 5:
    #     start = "Th"
    # else:
    #     start = "Fr" 

    day_print = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
    day_count = ["Sa", "Su", "Mo", "Tu", "We", "Th", "Fr"]

    if month == 3 or month == 5 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        for i in range(1, 32):

            if(i % 7 != 0):
                print(day_print[i], end="")
            else:
                print("\n")
    


    
if __name__ == "__main__":
    main()