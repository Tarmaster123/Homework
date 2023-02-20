#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ กีตาร์                                                 
# 630510609
# Lab11_1
# 229223 Sec 002

import string

def main():
    test_word_count()

def word_count(text):
    # case insenseitive
    text = text.lower()
    result = {}
    text = text.split()
    #remove punctuation
    list_text = list(map(lambda x : x.strip(string.punctuation), text))

    #find key and value
    for element in list_text:
        count  = 1 + result.get(element, 0)

        result[element] = count
    return result

def test_word_count():
    print(word_count('''
    "He doesn't want to pay $40,000 for a 
    new car, but his wife doesn't seem to 
    care."
    '''))

if __name__ == "__main__":
    main()

# def most_frequent(a):
#     max_value = None
#     max_count = 0
#     frequency = dict()
#     for elememt in a:
#         print("element in a is: ", elememt)
#         print("element getted: ", frequency.get(elememt, 0))
#         count = 1 + frequency.get(elememt, 0)

#         print("count is: ", count)
#         frequency[elememt] = count
#         print("frequency: ", frequency)
#         print()
#         if (count > max_count):
#             max_count = count
#             max_value = elememt
#     return max_value

# print(most_frequent([2, 5, 3, 4, 6, 4, 2, 4, 5]))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         