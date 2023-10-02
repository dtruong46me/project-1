
def main():
    n = int(input())

    if n <= 1:
        print(0)
        return
    
    if n == 2:
        print(1)
        return
    

    dp = [0] * (n+1)

    dp[2] = 1    

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[n])

if __name__ == '__main__':
    main()