#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW08_3
# 229223 Sec 002

def main():
    patterned_message("123", "** *** ** ** *")

def patterned_message(message, pattern, indexm = 0, indexp = 0 ):
    #base case
    if(indexp == len(pattern) - 1):
        print()
    else:
        if(indexm == len(message)):
            indexm = 0
        if(pattern[indexp] == "*"):
            pattern.replace("*" , message[indexm])
            return patterned_message(message, pattern, indexp + 1, indexm + 1)
        if(pattern[indexp] == " "):
            print(" ")
            return patterned_message(message, pattern, indexp + 1)

if __name__ == "__main__":
    main()