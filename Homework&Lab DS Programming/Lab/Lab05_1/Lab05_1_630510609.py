#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# Lab05_1
# 229223 Sec 002

#Define main function test german_num_format function
def main():
    test_german_num_format()

#Define german_num_format function to Change ',' to '.' and .'' to ','
def german_num_format(num_str):
    count = num_str.count(',')
    if("." in num_str):
        num_str = num_str.replace('.' , ',')
        if("," in num_str):
            num_str = num_str.replace(',' , '.' , count)
    elif("," in num_str):
            num_str = num_str.replace(',' , '.')
    return str(num_str)

#Define test function for check input 
def test_german_num_format():
    assert(german_num_format("1,234")) == "1.234"
    assert(german_num_format("1,020.50")) == "1.020,50"
    print("All OK!!!")


if __name__ == "__main__":
    main()