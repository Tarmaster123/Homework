#!/usr/bin/env python3
# Krittamet_Thaijaroen
# 630510609
# Lab06_2
# 229223 Sec 002

#Define main function 
def main():
    test_classify()

#Define classify function
def classify(list_x):
    list_a = list(filter(lambda x : isinstance(x , int) , list_x))
    list_b = list(filter(lambda x : isinstance(x , float) , list_x))
    list_c = list(filter(lambda x : isinstance(x , str) , list_x))
    return list_a , list_b , list_c

#Define test function
def test_classify():
    #classify([10 , 'hello' , 23.5 , 4])
    assert(classify([10 , 'hello' , 23.5 , 4])) == ([10, 4] , [23.5] , ['hello'])
    print("All OK!!!")

if __name__ == "__main__":
    main()
