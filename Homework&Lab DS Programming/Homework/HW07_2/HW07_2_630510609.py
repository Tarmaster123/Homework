#!/usr/bin/env python3
# Krittamet Thaijaroen
# 630510609
# HW07_2
# 229223 Sec 002

def main():
    assert medal_allocation ([9, 8, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7],) 
    assert medal_allocation ([9, 8, 7, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7, 7])
    assert medal_allocation ([9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8])
    assert medal_allocation ([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9, 9, 9] , [] , [])
    assert medal_allocation ([9, 9, 9, 9, 8, 7, 6, 5, 9, 3, 2]) == ([9, 9, 9, 9, 9] , [] , [])
    assert medal_allocation ([10, 10, 0, 0 , 0]) == ([10 , 10] , [] , [])
    assert medal_allocation ([1, 8, 7, 2, 9]) == ([9] , [8] , [7])
    assert medal_allocation ([9, 9, 9, 9, 7]) == ([9, 9, 9, 9] , [] , [])
    assert medal_allocation ([7, 9, 7, 9, 7]) == ([9, 9] , [] , [7, 7, 7])

    assert medal_allocation ([0, 0, 0, 0, 0]) == ([] , [] , [])
    assert medal_allocation ([9, 9, 9, 9, 9]) == ([9,9,9,9,9] , [] , [])
    assert medal_allocation ([10, 0, 0, 0, 0]) == ([10] , [] , [])
    assert medal_allocation ([6, 6, 0, 0, 0]) == ([6,6] , [] , [])
    print("All OK!!!")


def medal_allocation(list_a):
    #sort max to min score
    list_a = sorted(list_a)

    # don't consider zero score
    zero = list(filter(lambda x : x == 0 , list_a))
    index_del_zero = len(zero)

    del list_a[:index_del_zero]

    if(list_a == []):
        gold_medal = []
        silver_medal = []
        bronze_medal = []
        return gold_medal, silver_medal, bronze_medal

    list_a.sort(reverse = True)

    # Medal list
    #Gold Medal
    max_to_gold = max(list_a)
    gold_medal = list(filter(lambda x : x == max_to_gold ,list_a))
    index_del_gold = len(gold_medal)

    del list_a[:index_del_gold]
        
    # Silver Medal
    if(list_a != []):
        max_to_silver = max(list_a)
        silver_medal = list(filter(lambda x : x == max_to_silver , list_a))
        index_del_silver = len(silver_medal)
        del list_a[:index_del_silver]
    else:
        silver_medal = []

    # Bronze Medal
    if(list_a != []):
        max_to_bronze = max(list_a)
        bronze_medal = list(filter(lambda x :x == max_to_bronze ,  list_a))
    else:
        bronze_medal = []

    # lenght each medal
    taken_gold = len(gold_medal)
    taken_silver = len(silver_medal)


    if(taken_gold >= 2):
        if(taken_gold == 2):
            bronze_medal = silver_medal
            silver_medal = []
        else:
            silver_medal = []
            bronze_medal = []
    else:
        if(taken_silver >= 2):
            bronze_medal = []

    return gold_medal , silver_medal , bronze_medal

if __name__ == "__main__":
    main()