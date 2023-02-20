#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# HW04_2
# 229223 Sec 002

def main():
    test_min_diff()

# implement this function
def min_diff(hour1, min1, peroid1, hour2, min2, peroid2):
    hour1 = int(abs(hour1))
    hour2 = int(abs(hour2))
    min1 = int(abs(min1))
    min2 = int(abs(min2))

    #Same peroid
    if(peroid1 == peroid2):
        #AM
        if(peroid1 == "AM"):
            if(hour1 == 12):
                hour1 -= 12
            if(hour2 == 12):
                hour2 -= 12
        #PM
        else:
            if(hour1 < 12):
                hour1 += 12
            if(hour2 < 12):
                hour2 += 12

        if(hour1 == hour2):
            min = abs(abs(hour1 - hour2) * 60 - abs(min1 - min2))
        elif(hour1 < hour2):
            if(min1 < min2):
                min = abs(hour1 - hour2) * 60 + abs(min1 - min2)
            else:
                min = abs(hour1 - hour2) * 60 - abs(min1 - min2)
        else:
            if(min1 > min2):
                min = abs(hour1 - hour2) * 60 + abs(min1 - min2)
            else:
                min = abs(hour1 - hour2) * 60 - abs(min1 - min2)
    else:
        #AM , PM
        if(peroid1 == "AM"):
            if(hour2 == 0):
                hour2 += 12
            if(hour1 == 12):
                hour1 -= 12
            if(hour2 < 12):
                hour2 += 12
            if(hour1 <= hour2):

                if(min1 > min2):
                    min = abs(hour1 - hour2) * 60 - abs(min1 - min2)
                else:
                    min = abs(hour1 - hour2) * 60 + abs(min1 - min2)
        #PM ,AM
        else:
            if(hour1 == 0):
                hour1 += 12
            if(hour1 < 12):
                hour1 += 12
            if(hour2 == 12):
                hour2 -= 12

            if(min1 > min2):
                min = abs(hour1 - hour2) * 60 + abs(min1 - min2)
            else:
                min = abs(hour1 - hour2) * 60 - abs(min1 - min2)
    return min

# test function
def test_min_diff():
    # #Same peroid
    # assert(min_diff(11, 00, "AM", 12, 00, "AM")) == 660# 11.00 AM - 00.00 AM == 00.00 AM - 11.00 AM 
    # assert(min_diff(12, 00, "AM", 11, 00, "AM")) == 660
    # assert(min_diff(12, 00, "AM", 1, 00, "AM")) == 60# 00.00 AM - 01.00 AM
    # assert(min_diff(1, 00, "AM", 5, 00, "AM")) == 240# 01.00 AM - 05.00 AM
    # assert(min_diff(5, 00, "AM", 11, 00, "AM")) == 360# 05.00 AM - 11.00 AM
    # assert(min_diff(12, 00, "AM", 12, 00, "AM")) == 0# 00.00 AM - 00.00 AM
    # assert(min_diff(12, 00, "PM", 12, 00, "PM")) == 0# 12.00 PM - 12.00 PM
    # assert(min_diff(12, 00, "PM", 1, 00, "PM")) == 60# 12.00 PM - 13.00 PM
    # assert(min_diff(1, 00, "PM", 11, 00, "PM")) == 600# 13.00 PM - 23.00 PM

    # #Peroid1 is AM
    # assert(min_diff(12, 00, "AM", 12, 00, "PM")) == 720# 00.00 AM - 12.00 PM
    # assert(min_diff(0, 00, "AM", 0, 00, "PM")) == 720# 00.00 AM - 12.00 PM
    # assert(min_diff(8, 00, "AM", 8, 00, "PM")) == 720# 08.00 AM - 20.00 PM
    # assert(min_diff(12, 00, "AM", 5, 00, "PM")) == 1020# 00.00 AM - 17.00 PM == 17.00 PM - 00.00 PM
    # assert(min_diff(12, 00, "AM", 11, 00, "PM")) == 1380# 00.00 AM - 23.00 PM
    # assert(min_diff(8, 00, "AM", 12, 00, "PM")) == 240# 08.00 AM - 12.00 PM
    # assert(min_diff(8, 00, "AM", 1, 00, "PM")) == 300# 08.00 AM - 13.00 PM
    # assert(min_diff(11, 00, "AM", 12, 00, "PM")) == 60# 11.00 AM - 12.00 PM
    # assert(min_diff(11, 00, "AM", 9, 00, "PM")) == 600# 11.00 AM - 21.00 PM



    # #Peroid1 is PM
    # assert(min_diff(12, 00, "PM", 12, 00, "AM")) == 720# 12.00 PM - 00.00 AM
    # assert(min_diff(8, 00, "PM", 8, 00, "AM")) == 720# 08.00 AM - 20.00 PM
    # assert(min_diff(1, 00, "PM", 12, 00, "AM")) == 780# 13.00 PM - 00.00 AM
    # assert(min_diff(5, 00, "PM", 2, 00, "AM")) == 900# 17.00 PM - 02.00 AM
    # assert(min_diff(9, 00, "PM", 11, 00, "AM")) == 600# 21.00 PM - 11.00 AM

    #Same peroid
    #AM , AM
    assert(min_diff(12, 00, "AM", 12, 00, "AM")) == 0
    assert(min_diff(0, 0, "AM", 0, 0, "AM")) == 0
    assert(min_diff(12, 00, "AM", 0, 00, "AM")) == 0
    assert(min_diff(0, 00, "AM", 12, 00, "AM")) == 0
    assert(min_diff(12, 00, "AM", 11, 00, "AM"))  == 11 * 60
    assert(min_diff(11, 00, "AM", 12, 00, "AM")) == 11 * 60
    assert(min_diff(00, 00, "AM", 11, 00, "AM")) == 11 * 60
    assert(min_diff(11, 00, "AM", 00, 00, "AM")) == 11 * 60

    #PM , PM
    assert(min_diff(12, 00, "PM", 12, 00, "PM")) == 0
    assert(min_diff(12, 00, "PM", 0, 00, "PM")) == 0
    assert(min_diff(0, 00, "PM", 12, 00, "PM")) == 0
    assert(min_diff(5, 00, "PM", 12, 00, "PM")) == 5 * 60
    assert(min_diff(12, 00, "PM", 5, 00, "PM")) == 5 * 60
    assert(min_diff(13, 00, "PM", 14, 00, "PM")) == 60
    assert(min_diff(12, 00, "PM", 14, 00, "PM")) == 2 * 60
    assert(min_diff(14, 00, "PM", 12, 00, "PM")) == 2 * 60
    assert(min_diff(14, 00, "PM", 2, 00, "PM")) == 0
    assert(min_diff(5, 00, "PM", 7, 00, "PM")) == 2 * 60

    #Differnt peroid
    #AM , PM
    assert(min_diff(12, 00, "AM", 12, 00, "PM")) == 12 * 60
    assert(min_diff(0, 00, "AM", 12, 00, "PM")) == 12 * 60
    assert(min_diff(12, 00, "AM", 0, 00, "PM")) == 12 * 60
    assert(min_diff(12, 00, "AM", 13, 00, "PM")) == 13 * 60
    assert(min_diff(0, 00, "AM", 13, 00, "PM")) == 13 * 60
    assert(min_diff(12, 00, "AM", 2, 00, "PM")) == 14 * 60
    assert(min_diff(0, 00, "AM", 14, 00, "PM")) == 14 * 60
    assert(min_diff(7, 00, "AM", 12, 00, "PM")) == 5 * 60
    assert(min_diff(8, 00, "AM", 13, 00, "PM")) == 5 * 60
    assert(min_diff(9, 00, "AM", 2, 00, "PM")) == 5 * 60
    assert(min_diff(3, 00, "AM", 3, 00, "PM")) == 12 * 60
    assert(min_diff(4, 00, "AM", 16, 00, "PM")) == 12 * 60

    #PM , AM
    assert(min_diff(12, 00, "PM", 12, 00, "AM")) == 12 * 60
    assert(min_diff(12, 00, "PM", 0, 00, "AM")) == 12 * 60
    #assert(min_diff(13, 30, "PM", 12, 50, "AM")) == 760
    assert(min_diff(13, 00, "PM", 0, 00, "AM")) == 13 * 60
    assert(min_diff(2, 00, "PM", 12, 00, "AM")) == 14 * 60
    assert(min_diff(2, 00, "PM", 00, 00, "AM")) == 14 * 60
    assert(min_diff(12, 00, "PM", 7, 00, "AM")) == 5 * 60
    assert(min_diff(13, 00, "PM", 8, 00, "AM")) == 5 * 60
    assert(min_diff(2, 00, "PM", 9, 00, "AM")) == 5 * 60
    assert(min_diff(3, 00, "PM", 3, 00, "AM")) == 12 * 60
    assert(min_diff(16, 00, "PM", 4, 00, "AM")) == 12 * 60


    #From TA
    assert min_diff(8, 23, 'AM', 8, 24, 'AM') == 1

    assert min_diff(8, 24, 'AM', 1, 23, 'PM') == 299
    assert min_diff(1, 23, 'PM', 8, 24, 'AM') == 299

    assert min_diff(1, 24, 'PM', 8, 23, 'AM') == 301
    assert min_diff(8, 23, 'AM', 1, 24, 'PM') == 301

    assert min_diff(1,  0, 'AM', 1,  0, 'AM') == 0

    assert min_diff(1,  30, 'AM', 1,  50, 'PM') == 740

    assert min_diff(1,  0, 'PM', 1,  0, 'AM') == 12*60
    assert min_diff(12, 0, 'PM', 11, 0, 'AM') == 60
    assert min_diff(11, 0, 'PM', 12, 0, 'AM') == 60*23 

    print("All OK!!!!")



if __name__ == "__main__":
    main()
