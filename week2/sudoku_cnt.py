import sys

def main():

    global count
    count = 0

    # BEGIN: Read input from user
    def read_input() -> list:
        array = []

        for i in range(9):
            line = [int(x) for x in sys.stdin.readline().split()]
            array.append(line)

        return array
    
    array = read_input()

    
    ## BEGIN: Check if accept
    def accept(r, c, num):
        
        # Check for rows and columns
        for i in range(9):
            if array[r][i] == num or array[i][c] == num:
                return False

        # Check for subsquares
        r_square = 
    
    def Try(k):
        row = k // 3
        col = k % 3

        if k == 81:
            return
        
        else:
            for i in range

        return
    
    Try(0)

if __name__ == '__main__':
    main()