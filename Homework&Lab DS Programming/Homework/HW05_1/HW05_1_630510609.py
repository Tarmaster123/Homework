#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# HW05_1
# 229223 Sec 002

#Define main fuction for use test function
def main():
    test_palindrome_without()

#Cut and replace
def cut_replace(text , c):
    text = text.lower()
    if(" " in text):
        text = text.replace(" " , "")
    if(" " in c):
        c = c.replace(" " , "")
    if(text == c):
        return False
    new_text = text.replace(c , "")
    return new_text


#Define palinedrome_without fuction for palindrome check
def palindrome_without(text , c):
    palin_check = cut_replace(text , c)
    if(palin_check == False):
        return False

    if(palin_check == palin_check[::-1]):
        return True
    else:
        return False
    

#Define test_palinedrome_without fuction for test input
def test_palindrome_without():
    assert(palindrome_without("Banana" , "c")) == False
    assert(palindrome_without(" Swap of paws " , "f ")) == True
    assert(palindrome_without("T" ,"a")) == True
    assert(palindrome_without("T " ,"t")) == False
    assert(palindrome_without("T " ,"t ")) == False
    assert(palindrome_without("T " ,"")) == True
    print("All OK!!!!")

if __name__ == '__main__':
    main()
