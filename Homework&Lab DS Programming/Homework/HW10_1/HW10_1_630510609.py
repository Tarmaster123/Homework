#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW10_1
# 229223 Sec 002
def main():
    test_float_to_base_b()
    #print(float_to_base_b(-3.1415, 3))
    

def float_to_base_b(x, b):
    first = int(x)
    last = abs(x - int(x))
    if(x < 0):
        first_part = "-" + find_first_part(first, b)
    else:
        first_part = find_first_part(first, b)
    last_part = find_last_part(last, b)
    return first_part + "." + last_part 
  
def find_first_part(first, b):

    list_first_part = []
    first = abs(first) 
    if(first == 0):
        return "0"
    else:
        while(first != 0):
            remainder = first % b
            if(remainder < 10):
                list_first_part.insert(0, str(remainder))
            else:
                if(remainder == 10):
                    remainder = "A"
                elif(remainder == 11):
                    remainder = "B"
                elif(remainder == 12):
                    remainder = "C"
                elif(remainder == 13):
                    remainder = "D"
                elif(remainder == 14):
                    remainder = "E"
                else:
                    remainder = "F"
                list_first_part.insert(0, str(remainder))
            first = first // b
        first_result = "".join(list_first_part)
        return first_result

def find_last_part(last, b):
    print(last, b)
    if(last == 0):
        return "000000"
    else:
        list_last_part = []   
        for i in range (6):
            remainder = int(last * b)
            #print(remainder)
            if(remainder < 10):
                list_last_part.append(str(remainder))
            else:
                if(remainder == 10):
                    remainder = "A"
                elif(remainder == 11):
                    remainder = "B"
                elif(remainder == 12):
                    remainder = "C"
                elif(remainder == 13):
                    remainder = "D"
                elif(remainder == 14):
                    remainder = "E"
                else:
                    remainder = "F"
                list_last_part.append(str(remainder))
            last = (last * b) - int(last * b)
            #print(last)
        last_result = "".join(list_last_part)
        return last_result
    

def test_float_to_base_b():
    # float_to_base_b(44.1875, 2) == "101100.001100"
    # float_to_base_b(0.99999999, 2) == "0.111111"
    # float_to_base_b(-3.1415, 3) == "-10.010211"
    # float_to_base_b(0.9375, 16) == "0.F00000"
    #print(float_to_base_b(0, 16))
    print (float_to_base_b(-0.14, 2))
    print("ALL OK!!!")

if __name__ == "__main__":
    main()