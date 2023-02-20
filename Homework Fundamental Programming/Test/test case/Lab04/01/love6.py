def love6(first, second):
    if first == 6 or second == 6 or first + second == 6 or abs(first - second) == 6:
        return True
    else:
        return False
    
def main():
    first = int(input(""))
    second = int(input(""))
    print(love6(first, second))

if __name__=='__main__':
    main()


    





    
    
