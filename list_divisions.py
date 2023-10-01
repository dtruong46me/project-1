
def main():

    n = int(input())

    num_down = int(100/n)
    num_top = int(999/n)

    for i in range(num_down, num_top + 1):
        if (i*n >= 100 and i*n <= 999):
            print(i * n, end = " ")
    
if __name__ == '__main__':
    main()