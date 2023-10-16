
import sys

def main():
    n = int(input())
    array = [int(x) for x in input().split()]
    output = []

    seen = set()
    for i in range(n):
        if array[i] not in seen:
            output.append(0)
            seen.add(array[i])
        else:
            output.append(1)
    
    print('\n'.join(str(x) for x in output))

if __name__ == '__main__':
    main()