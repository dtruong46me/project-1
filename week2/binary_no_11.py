
def main():

    n = int(input())

    x = [0 for _ in range(n+1)]

    def accept(i, k) -> bool:
        if i==1 and x[k-1]==1:
            return False
        
        return True

    def Try(k):

        if k == n+1:
            print(''.join(map(str, x[1:])))

        else:
            for i in range(2):
                if accept(i, k):
                    x[k] = i
                    Try(k+1)

        return
    
    Try(1)

    return

if __name__ == '__main__':
    main()