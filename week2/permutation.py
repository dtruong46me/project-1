
def main():
    n = int(input())

    x = [0 for _ in range(n+1)]

    def check(i, k) -> bool:
        for j in range(1, k):
            if x[j] == i:
                return False

        return True

    def Try(k):

        if k == n+1:
            # print(' '.join(map(str, x[1:])))
            for v in range(1, n+1):
                print(x[v], end=' ')
            print()

        else:
            for i in range(1, n+1):
                if check(i, k):
                    x[k] = i
                    Try(k+1)

        return
    
    Try(1)

    return

if __name__ == '__main__':
    main()