#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# Lab09_1
# 229223 Sec 002

import string
def main():
    test_is_anagram()

def is_anagram(s1, s2, i_s1=0):
    #Change to insensitive
    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace(" ","")
    s2 = s2.replace(" ","")

    #anagram check
    if(len(s1) != len(s2)):
        return False

    #base case
    if(i_s1 == len(s1)):
        return True

    #anagram check
    else:
        if(s1[i_s1] in s2):
            word = s2.find(s1[i_s1])
            s1 = s1.replace(s1[i_s1] , "")
            s2 = s2.replace(s2[word] , "")
            return is_anagram(s1, s2)
        else:
            return False

def test_is_anagram():
    assert is_anagram("Tom Marvolo Riddle", "I am Lord Voldemort") == True
    assert is_anagram("cat", "tab") == False
    assert is_anagram("Eleven plus two", "Twelve plus one") == True

    assert is_anagram("ABC A", "BB   CA") == False
    print("All OK!!!!")

if __name__ == "__main__":
    main()