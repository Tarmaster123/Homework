#!/usr/bin/env python3
# Krittamet_Thaijaroen
# 630510609
# Lab07_2
# 229223 Sec 002

def main():
    assert(uniform("HaPpY") == "HAPPY")
    assert(uniform("cOdINg") == "coding")
    assert(uniform("coMP scI!!!") == "comp sci!!!")
    print("All OK!!!")

#Define Up function to check upper case
def Up(x):
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if(x in up):
        return True

#Define Up function to check lower case
def Low(x):
    low = "abcdefghijklmnopqrstuvwxyz"
    if(x in low):
        return True

def uniform(line):
    line_list = list(line)
    up_list = list(filter(lambda x : Up(x) == True , line_list))
    low_list = list(filter(lambda x : Low(x) == True , line_list))

    Up_len = len(up_list)
    Low_len = len(low_list)

    #Upper equal Lower
    if(Up_len == Low_len):
        if(Up(line[0]) == True):
            line = line.upper()
        else:
            line = line.lower()

    #Upper more than Lower
    elif(Up_len > Low_len):
        line = line.upper()
    #Upper less than Lower
    else:
        line = line.lower()
    
    return line

if __name__ == "__main__":
    main()