def main():

    n, m = [int(x) for x in input().split()]

    x = [0 for i in range(n+1)]

    def accept(i, k) -> bool:

        if sum(x[1:k]) + i > m:
            return False
        
        return True

    def Try(k):
        if k == n+1 and sum(x[1:n+1])==m:
            # print(' '.join(map(str, x[1:])))
            for i in range(1, n+1):
                print(x[i], end=' ')
            print()
        
        if k <= n:
            for i in range(1, m):
                if accept(i, k):
                    x[k] = i
                    Try(k+1)

    Try(1)

if __name__ == '__main__':
    main()

