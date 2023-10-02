
def main():
    k, n = [int(x) for x in input().split()]

    if k==1:
        print(n)
        return
    
    if k==n:
        print(1)
        return
    
    dp = [[0] * (n+1) for _ in range(k+1)]

    for i in range(n+1):
        dp[1][i] = i

    for i in range(2, k+1):
        for j in range(1, n+1):

            # C_k_n = C_k-1_n-1 + C_k_n-1
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    
    print(dp[k][n])

if __name__ == '__main__':
    main()