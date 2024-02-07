#!/usr/bin/python3
'''
this is a module
'''
import sys


def solve(n, i, a, b, c):
    '''
    a function
    '''
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                for solution in solve(n, i+1, a+[j], b+[i+j], c+[i-j]):
                    yield solution
    else:
        yield a


def print_solution(solution):
    '''
    a function
    '''
    result = []
    for i in range(len(solution)):
        result.append([i, solution[i]])
    print(result)


def main():
    '''
    a function
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solve(n, 0, [], [], []):
        print_solution(solution)


if __name__ == "__main__":
    main()
