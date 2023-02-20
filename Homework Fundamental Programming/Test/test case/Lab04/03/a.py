def calculate_p2p_evolve_exp(p, c):
    a = 11
    if c//a <= p:
        exp = 500 * (c//a)
        return exp
    else :
        exp = (500 * (c//a))-((c//a) - p) *500
        return exp
    
def main():
    p = int(input(""))
    c = int(input(""))
    exp = calculate_p2p_evolve_exp(p, c)
    print(exp)
    
if __name__ == '__main__':
    main()
    
