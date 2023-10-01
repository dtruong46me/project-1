import sys
from time import time

def main():

    n, k = [int(x) for x in input().split()]
    
    array = [int(x) for x in input().split()]

    count = 0
    cur_sum = sum(array[:k])

    for i in range(n-k+1):
        # if sum(array[i: i+k]) % 2 == 0:
        if cur_sum % 2 == 0:
            count += 1
        # print(cur_sum)
        
        if i + k < n:
            cur_sum = cur_sum - array[i] + array[i+k]
    
    print(count)
    return

if __name__ == '__main__':
    s = time()
    main()
    e = time()

    print(f"Execution time: {(e-s):.5f}")