
def main():
    n, m = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]

    count = 0
    seen = set()

    for i in range(n):
        if m - array[i] in seen:
            count += 1
        seen.add(array[i])

    print(count)

if __name__ == '__main__':
    main()