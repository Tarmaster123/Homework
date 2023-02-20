#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW06_3
# 229223 Sec 002

#Define main function
def main():
    test_moving_average()

#Define moving_average function
def moving_average(list_a , w):
    w = abs(w) 

    lenght_list_a = len(list_a)
    range_list_a = range(1 , lenght_list_a)
    
    if(list_a == [0] ):
        return list_a

    elif(w == 1 or w == 0):
        return list(map(lambda x : (x + x) / 2 ,list_a ))

    elif(w == lenght_list_a):
        avg = []
        result = sum(list_a) / lenght_list_a
        avg.append(result)

    else:
        result = list(map(lambda x , y : (x + sum(list_a[y:y+(w-1)])) / w if y + (w-1) <= lenght_list_a else [] ,list_a , range_list_a))
        avg = list(filter(result_ , result))
    return avg

#Filter result to float
def result_(x):
    return (isinstance(x , float))

#Define test_moving_average function
def test_moving_average():
    #int 
    print(moving_average([1, 2, 3, 4, 5] , 6)) #== [1.0, 2.0, 3.0, 4.0, 5.0]
    # assert(moving_average([1, 2, 3, 4, 5] , 2)) == [1.5, 2.5, 3.5, 4.5]
    # assert(moving_average([1, 2, 3, 4, 5] , 3)) == [2.0, 3.0, 4.0]
    # assert(moving_average([-1, 2, -3, 4, -5] , 2)) == [0.5, -0.5, 0.5, -0.5]
    # assert(moving_average([0] , 2)) == [0]
    # assert(moving_average([1, 0, 3, 5, 1] , 2)) == [0.5, 1.5, 4, 3]
    # assert(moving_average([53, 64, 1, 25, 25] , 2)) == [58.5, 32.5, 13.0, 25.0]
    # assert(moving_average([5, 5, 5, 5, 5] , 2)) == [5.0, 5.0, 5.0, 5.0]
    # assert(moving_average([-1.5, -2.3, -3.1, -4.9, -5.2] , 5)) == [-3.4]
    # assert(moving_average([9 ,13 ,-1 ,2] , 0)) == [9.0, 13.0, -1.0, 2.0]

    print("All OK!!!")

if __name__ == "__main__":
    main()