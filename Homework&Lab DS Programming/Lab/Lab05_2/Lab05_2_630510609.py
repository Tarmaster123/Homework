#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# Lab05_1
# 229223 Sec 002

#Define main function for use test function
def main():
    test_zodiac_element()

#Define zodiac_element calculate Yin/Yang , zodiac year and element for input
def zodiac_element(year):
    #Calculate Yin/Yang
    y = Find_Yin_Yang(year)

    #Calculate zodiac year
    z = Find_zodiac(year)

    #Calculate element
    e = Find_element(year)

    return ("%s %s %s" %(y ,e ,z))

#Define Find_Yin_Yang for calculate Yin or Yang from year 
def Find_Yin_Yang(year):
    if(year % 2 == 0):
        Yin_Yang = "Yang"
    else:
        Yin_Yang = "Yin"
    return Yin_Yang

#Define Find_zodiac for calculate zodiac from year
def Find_zodiac(year):
    if(year % 12 == 1996 % 12):
        zodiac = "Rat"
    elif(year % 12 == 1997 % 12):
        zodiac = "Ox"
    elif(year % 12 == 1998 % 12):
        zodiac = "Tiger"
    elif(year % 12 == 1999 % 12):
        zodiac = "Rabbit"
    elif(year % 12 == 2000 % 12):
        zodiac = "Dragon"
    elif(year % 12 == 2001 % 12):
        zodiac = "Snake"
    elif(year % 12 == 2002 % 12):
        zodiac = "Horse"
    elif(year % 12 == 2003 % 12):
        zodiac = "Goat"
    elif(year % 12 == 1992 % 12):
        zodiac = "Monkey"
    elif(year % 12 == 1993 % 12):
        zodiac = "Rooster"
    elif(year % 12 == 1994 % 12):
        zodiac = "Dog"
    else:
        zodiac = "Pig"
    return zodiac


#Define Find_element for calculate element from year
def Find_element(year):
    if(year % 10 == 0 or year % 10 == 1 ):
        element = "Metal"
    elif(year % 10 == 2 or year % 10 == 3 ):
        element = "Water"
    elif(year % 10 == 4 or year % 10 == 5 ):
        element = "Wood"
    elif(year % 10 == 6 or year % 10 == 7 ):
        element = "Fire"
    else:
        element = "Earth"
    return element

#Define test zodiac_element function for test input 
def test_zodiac_element():
    assert(zodiac_element(1997)) == "Yin Fire Ox"
    assert(zodiac_element(2022)) == "Yang Water Tiger"
    print("All OK!!!")

if __name__ == "__main__":
    main()