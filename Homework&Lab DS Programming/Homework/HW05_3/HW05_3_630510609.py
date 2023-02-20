#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์
# 630510609
# HW05_3
# 229223 Sec 002

#Define main function to call substitude_once function
def main():
    test_substitude_once()

#Define substitude_once function to replace bubstring 
def substitute_once(text , old , new):
    #sub not in text
    if(old not in text):
        return text

    #find old index
    old_index = text.find(old)

    #find new start point
    new_start = old_index + len(old)

    new_text = text[:old_index] + new + text[new_start:]
    return new_text


#Define test_substitude_once for check input and answer
def test_substitude_once():
    assert(substitute_once("battle" , "b" , "c")) == "cattle"
    assert(substitute_once("Bidding" , "i" , "u")) == "Budding"
    assert(substitute_once("doesn't" , "n't" , " not" )) == "does not"
    assert(substitute_once("doesn'tSuperman" , "n't" , " not " )) == "does not Superman"
    assert(substitute_once("IU" , "L" , "u")) == "IU"

    print("All OK!!!")

if __name__ == "__main__":
    main()
