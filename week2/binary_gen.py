
def main():
    n = int(input())

    x = [0 for _ in range(n+1)]

    def accept(i, k) -> bool:

        return True

    def Try(k):
        """
        Backtracking(k)
            for([Mỗi phương án chọn i(thuộc tập D)])
                if ([Chấp nhận i])
                    [Chọn i cho X[k]];
                    if ([Thành công])
                        [Đưa ra kết quả];
                    } else
                        Backtracking(k+1);
                        [Bỏ chọn i cho X[k]];
        """
        if k == n+1:
            print(''.join(map(str, x[1:])))
        
        else:
            for i in range(2):
                if accept(i, k):
                    x[k] = i
                    Try(k+1)

    Try(1)

if __name__ == '__main__':
    main()