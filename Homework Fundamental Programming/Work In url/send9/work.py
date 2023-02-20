def pascal_triangle(n, triangle=[[1]]):
    if n > len(triangle):
        last_row = triangle[-1]
        next_row = [a+b for (a, b) in zip([0] + last_row, last_row + [0])]
        return pascal_triangle(n, triangle + [next_row])
    else:
    	return 0
    return triangle
def main():
	n = int(input("Pascal's triangle size: "))
	print(*pascal_triangle(n), sep="\n")

main()

