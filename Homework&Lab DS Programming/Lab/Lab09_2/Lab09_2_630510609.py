#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# Lab09_2
# 229223 Sec 002

def main():
    test_sum_prime_in_range()
    #print(sum_prime_in_range(3, 3))

#Check prime number
def is_prime(n , div):
    if(div > n**0.5):
        return True

    elif(n%div == 0):
        return False
    else:                                                                               
        return is_prime(n , div + 1)
        

def sum_prime_in_range(x, y):
    #find sum of prime number
    n_range = range(x , y+1)
    prime = list(filter(lambda x : is_prime(x , 2) == True , n_range))
    result = sum(prime)
    return result


    

def test_sum_prime_in_range():
    assert sum_prime_in_range(3, 20) == 75
    assert sum_prime_in_range(3, 3) == 3
    print("All Ok!!!!")

if __name__ == "__main__":
    main()