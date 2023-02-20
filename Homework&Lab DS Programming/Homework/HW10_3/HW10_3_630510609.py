#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW10_3
# 229223 Sec 002

def main():
    test_polynomial_addition()    

def polynomial_addition(p1, p2):
    new_p1 = sorted(p1, reverse=True)
    new_p2 = sorted(p2, reverse=True)

    i_1 = 0
    i_2 = 0
    result = []
    # print(new_p1)
    # print(new_p2)
    while i_1 < len(new_p1) and i_2 < len(new_p2):
        power_1 , coe_1 = new_p1[i_1]
        power_2 , coe_2 = new_p2[i_2]
        if(power_1 == power_2):
            power, coe = power_1, coe_1 + coe_2
            if(coe == 0):
                i_1 += 1
                i_2 += 1
                continue
            else:
                keep = power, coe
                i_1 += 1
                i_2 += 1
        elif(power_1 > power_2):
            keep = power_1, coe_1
            i_1 += 1
        else:
            keep = power_2, coe_2
            i_2 += 1
        result.append(keep)

    if(i_1 < len(new_p1)):
        result.extend(new_p1[i_1:])
    if(i_2 < len(new_p2)):
        result.extend(new_p2[i_2:])
    return result


def test_polynomial_addition():
    assert polynomial_addition([(2, 6), (1, 34), (0, -8)], [(2, -6), (0, 2), (1, 1) ]) == [(1, 35), (0, -6)]
    assert polynomial_addition([(4, -6), (3, 2), (2, 1), (1, 5)], [(3, 6), (0, -8)]) == [(4, -6), (3, 8), (2, 1), (1, 5), (0, -8)]
    assert polynomial_addition([(3, 6), (1, 34), (2, -8)], [(2, -6), (4, 2), (0, 1)]) == [(4, 2), (3, 6), (2, -14), (1, 34), (0, 1)]
    print("ALL OK!!!")

if __name__ == "__main__":
    main()