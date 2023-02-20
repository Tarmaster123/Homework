#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW07_3
# 229223 Sec 002

def main():
    assert(num_to_word(14) == "fourteen")
    assert(num_to_word(248) == "two hundred forty-eight")
    assert(num_to_word(111) == "one hundred eleven")
    assert(num_to_word(0) == "zero")
    print(num_to_word(42641323862)) #== "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two")
    # print(num_to_word(12389))
    # print(num_to_word(1001000000))
    print("All OK")

# ตืนต่าคำอ่าน ภาษา อังกฤษ ของจำนวนเต็ม
def three_digits_to_word(n):
    unit_list = ["", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"]

    ten_list = ["", "", "twenty" ,"thirty", "forty", "fifty" ,"sixty" ,"seventy" ,"eighty" , "ninety" ]

    # less than twenty
    if(n < 20):
        word = unit_list[n]
        return word

    # less than 100
    elif(n < 100 and n >= 20):
        ten , unit = divmod(n , 10)
        if(unit != 0):
            word = ten_list[ten] + "-" + unit_list[unit]    
        else:
            word = ten_list[ten]
        return word
    else:
        ten , unit = divmod(n , 100)
        if(unit != 0 ):
            hundred_unit = unit_list[ten] + " hundred "
        else:
            hundred_unit = unit_list[ten] + " hundred"

        if(unit < 20):
            word =  hundred_unit + unit_list[unit]
        else:
            ten , unit = divmod(unit , 10)
            if(unit != 0):
                word = hundred_unit + ten_list[ten] + "-" + unit_list[unit]
            else:
                word = hundred_unit + ten_list[ten]
        return word

# คืนค่าคำอ่านของจพนวนเต็ม
def num_to_word(num):
    # num is zero
    if(num == 0):
        word = "zero"

    # less than thousand
    elif(num >= 1 and num < 10**3):
        word = three_digits_to_word(num)

    # thousand to before million
    elif(num >= 10**3 and num < 10**6):
        if(num % 10**3 == 0):
            word = three_digits_to_word(num//10**3) + " " + "thousand"
        else:
            word = three_digits_to_word(num//10**3) + " " + "thousand " + three_digits_to_word(num%10**3)
    # million to before billion
    elif(num >= 10**6 and num < 10**9):
        if(num % 10**6 == 0):
            word = three_digits_to_word(num//10**6) + " " + "million "
        else:
            numcal = num - ((num//10**6) * 10**6)
            word = three_digits_to_word(num//10**6) + " " + "million " + three_digits_to_word(numcal//10**3) + " " + "thousand " + three_digits_to_word(num%10**3)

    # more than equal billion
    else:
        if(num % 10**9 == 0):
            word = three_digits_to_word(num//10**9) + " " + "billion "
        elif((num - (num // 10**9)*10**9) % 10**6 == 0):
            numcal = num - (num//10**9)*10**9
            word = three_digits_to_word(num//10**9) + " " + "billion " + three_digits_to_word(numcal//10**6) + " " +"million "
        else:
            numcal = num - (num//10**9)*10**9
            numcal1 = (numcal % 10**6)//10**3
            word = three_digits_to_word(num//10**9) + " " + "billion " + three_digits_to_word(numcal//10**6) + " " +"million " + three_digits_to_word(numcal1) + " " + "thousand " + three_digits_to_word(num % 10**3)


    return word

if __name__ == "__main__":
    main()