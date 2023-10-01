# from time import time

def main():

    n = int(input())
    s = 0

    array = [int(x) for x in input().split()]

    print(sum(array))

if __name__ == '__main__':
    # s = time()
    main()
    # e = time()

    # print(f"Execution time: {(e-s):5f}")