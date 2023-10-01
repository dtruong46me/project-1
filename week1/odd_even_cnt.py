
def main():
    n = int(input())

    array = [int(x) for x in input().split()]

    numbers = [0 if num % 2 == 0 else 1 for num in array]

    count_even = numbers.count(0)
    count_odd = numbers.count(1)

    print(count_odd, count_even)

if __name__ == '__main__':
    main()