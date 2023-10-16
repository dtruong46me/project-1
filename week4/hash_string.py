import sys
from time import time

def compute_power(k: int, m: int):
    powers = [1]
    base = 256

    for i in range(1, k):
        powers.append((powers[-1] * base) % m)
    
    return powers

def hash(s: str, m: int, powers: list) -> int:
    k = len(s)
    # powers = compute_power(200, m)

    h = sum([ord(s[x]) * powers[k-x-1] for x in range(k)]) % m

    return h

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]

    strings = []
    maxlen = 0
    for _ in range(n):
        string = sys.stdin.readline()[:-1]
        if len(string) > maxlen:
            maxlen = len(string)

        strings.append(string)

    powers = compute_power(maxlen, m)
    for string in strings:
        print(hash(string, m, powers))

if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print(f"Execution time: {(end-start):.5f}")
