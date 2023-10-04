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
        r_square = r // 3
        c_square = c // 3
        for i in range(3*r_square, 3*r_square+3):
            for j in range(3*c_square, 3*c_square+3):
                if array[i][j] == num:
                    return False
        
        return True
    
    def solve():
        global count

        for row in range(9):
            for col in range(9):
                
                # Check if array[i][j] = 0
                if array[row][col] == 0:
                    for num in range(1, 10):
                        if accept(row, col, num):
                            array[row][col] = num

                            # Recursive to solve
                            if solve():
                                
                                return

                            # Return array[i][j] to 0
                            array[row][col] = 0
                    
                    return

        count += 1

        
        for row in array:
            print(' '.join(map(str, row)))

        # return
    
    # Solve Sudoku
    solve()
    print(count)

if __name__ == '__main__':
    main()

'''
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0 
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
'''