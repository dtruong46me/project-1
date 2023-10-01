
def main():
    a, b = [int(x) for x in input().split()]

    try:
        print(a + b, a - b, a * b, int(a / b))
    except:
        print(ZeroDivisionError)    

if __name__ == '__main__':
    main()