
import sys

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    # Insert Node(k)
    def insert(self, k):
        if self.value < k:
            if self.right is None:
                self.right = Node(k)
            else:
                self.right.insert(k)
        
        if self.value > k:
            if self.left is None:
                self.left = Node(k)
            else:
                self.left.insert(k)

class BinarySearchTree:
    def __init__(self, root=None) -> None:
        self.root = root

    # Insert Node(k)
    def insert_(self, k):
        if self.root is None:
            self.root = Node(k)
        else:
            self.root.insert(k)
    
    # Print Tree
    def pre_order(self):
        if self.root is not None:
            self._pre_order(self.root)

    def _pre_order(self, node: Node):
        if node is None:
            return

        if node is not None:
            print(node.value, end=' ')
            self._pre_order(node.left)
            self._pre_order(node.right)

def main():
    bst = BinarySearchTree()

    values = []
    while True:
        line = sys.stdin.readline().split()

        if line[0] == '#':
            break

        if line[0] == 'insert':
            values.append(int(line[1]))
    
    for k in values:
        bst.insert_(k)
    
    bst.pre_order()

if __name__ == '__main__':
    main()