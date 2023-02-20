#!/usr/bin/env python3
# เมธาพร เม้ยกำเนิด (เฟรช)
# 631610317
# HW07_3
# 229223 Sec002

def main():
    #test_three_digits_to_word()
    print(num_to_word(996862))

def three_digits_to_word(n):
    unit_list = ["", "one", "two", "three", "four", "five",
                "six", "seven", "eight", "nine", "ten",
                "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                "sixteen", "seventeen", "eighteen", "nineteen"]
    
    list_ty = ["", "", "twenty", "thirty", "forty", "fifty", 
                "sixty", "seventy", "eighty", "ninety"]

    list_hundred = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred",
                    "six hundred", "seven hundred", "eight hundred", "nine hundred"]

    if len(str(n)) == 1: 
        return unit_list[n] 
    if len(str(n)) == 2:
        if (n) <= 19:
            return unit_list[n] 
        if (n) > 19:
            ty, unit = divmod(n, 10)
            ty = list_ty[ty]
            unit = unit_list[unit]
            return ty + '-' + unit 
    if len(str(n)) == 3:
        hun,ty = divmod(n, 100) 
        hun = list_hundred[hun]
        if ty == 0:
            return hun
        if ty <= 19: 
            return hun + ' ' + unit_list[ty] 
        else:
            ty,unit = divmod(ty, 10)
            ty = list_ty[ty]
            if(unit == 0):
                return hun + ' ' + ty 
            else:
                unit = unit_list[unit]
                return hun + ' ' + ty + '-' + unit 

def num_to_word(num):
    if num == 0:
        return 'zero'
    if num < 1000:
        return three_digits_to_word(num)

    elif num >= 1000 and num < 1000000:
        thou,hun = divmod(num,1000)
        thousand = three_digits_to_word(thou)
        hundred = three_digits_to_word(hun)
        if hun == 0:
            return thousand + ' ' + 'thousand'
        return thousand + ' ' + 'thousand ' + hundred 

    elif num >= 1000000 and num < 1000000000:
        mil,thou = divmod(num, 1000000)
        million = three_digits_to_word(mil)
        if thou == 0:
            return million + ' ' + 'million'
        else:
            thou,hun = divmod(thou,1000)
            thousand = three_digits_to_word(thou)
            if hun == 0:
                return million + ' ' + 'million ' + thousand + ' ' + 'thousand'
            hundred = three_digits_to_word(hun)
            return million + ' ' + 'million ' + thousand + ' ' + 'thousand ' + hundred 
    else: 
        bil,mil = divmod(num, 1000000000)
        billion = three_digits_to_word(bil)
        if mil == 0:
            return billion + ' ' + 'billion'
        else:
            mil,thou = divmod(mil, 1000000)            
            million = three_digits_to_word(mil)
            if thou == 0:
                return billion + ' ' + 'billion ' +  million + ' ' + 'million'
            thou,hun = divmod(thou,1000)
            thousand = three_digits_to_word(thou)
            if hun == 0:
                return billion + ' ' + 'billion ' + million + ' ' + 'million ' + thousand + ' ' + 'thousand'
            else:
                hundred = three_digits_to_word(hun)
                return billion + ' ' + 'billion ' + million + ' ' + 'million ' + thousand + ' ' + 'thousand ' + hundred
        
def test_three_digits_to_word():
    assert num_to_word(14) == 'fourteen'
    assert num_to_word(248) == 'two hundred forty-eight'
    assert num_to_word(111) == 'one hundred eleven'
    assert num_to_word(0) == 'zero'
    assert num_to_word(1000) == 'one thousand'
    assert num_to_word(100000) == 'one hundred thousand'
    assert num_to_word(1000000) == 'one million'
    assert num_to_word(9999999) == 'nine million nine hundred ninety-nine thousand nine hundred ninety-nine'
    assert num_to_word(1000000000) == 'one billion'
    assert num_to_word(42641323862) == 'forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two'
    # add
    assert num_to_word(1001000000) == 'one billion one million'
    assert num_to_word(1001001000) == 'one billion one million one thousand'
    assert num_to_word(1001000) == 'one million one thousand'
    assert num_to_word(99999) == 'ninety-nine thousand nine hundred ninety-nine'
    assert num_to_word(900990) == 'nine hundred thousand nine hundred ninety'

    print("all ok")

if __name__ == '__main__':
    main()