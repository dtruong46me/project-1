# from time import time

class SegmentTree:
    def __init__(self, array) -> None:
        self.n = len(array)
        self.tree = [0] * (4 * self.n)
        self.build(array, 1, 0, self.n - 1)

    def build(self, array, v, tl, tr):
        if tl == tr:
            self.tree[v] = array[tl]
        
        else:
            tm = (tl + tr) // 2
            self.build(array, v * 2, tl, tm)
            self.build(array, v * 2 + 1, tm + 1, tr)
            self.tree[v] = max(self.tree[v * 2], self.tree[v * 2 + 1])
    
    def query(self, v, tl, tr, l, r):
        if l > r:
            return float('-inf')
        
        if l == tl and r == tr:
            return self.tree[v]
        
        tm = (tl + tr) // 2

        left = self.query(v*2, tl, tm, l, min(r, tm))
        right = self.query(v*2+1, tm+1, tr, max(l, tm+1), r)

        return max(left, right)


def find_max(array: list):
    return max(array)

def find_min(array: list):
    return min(array)

def find_sum(array: list):
    return sum(array)

def find_max_segment(array: list, i, j):
    # return max(array[i-1:j])
    max_val = array[i-1]
    
    for k in range(i-1, j):
        if array[k] >= max_val:
            max_val = array[k]
    
    return max_val

# def read_input():
#     return

def main():

    demands = {
        1: "find-max",
        2: "find-min",
        3: "find-max-segment",
        4: "sum"
    }

    n = int(input())
    array = [int(x) for x in input().split()]
    _ = input()

    segment_tree = SegmentTree(array)

    result = []

    while True:
        line = input().split()
        if line[0] == '***':
            break

        if line[0] == demands[1]:
            result.append(find_max(array))

        if line[0] == demands[2]:
            result.append(find_min(array))

        if line[0] == demands[3]:
            l, r = int(line[1])-1, int(line[2]) - 1
            result.append(segment_tree.query(1, 0, n-1, l, r)) 
            # result.append(find_max_segment(array, int(line[1]), int(line[2])))
        
        if line[0] == demands[4]:
            result.append(find_sum(array))

    output = "\n".join(map(str, result))
    print(output)
    # return

if __name__ == '__main__':
    # start_time = time()
    main()
    # end_time = time()

    # print(f"Execution time: {(end_time - start_time):.5f}")