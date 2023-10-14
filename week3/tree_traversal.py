import sys

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None

    # Make Root
    def make_root(self, u:int):
        if self.root is None:
            self.root = Node(u)
        return None
    
    # Find Node with the id 'v'
    def find_node(self, v, root:Node) -> Node:

        if root is None:
            return 
        
        if root.value == v:
            return root

        curr_node = root.left
        while curr_node != None:
            assert isinstance(curr_node, Node)
            result = self.find_node(v, root=curr_node)
            
            if result is not None:
                return result
            
            curr_node = curr_node.right
        
        return
    
    # Insert Node(u) - The child of Node(v) 
    def insert_(self, u: int, v: int):
        new_node = Node(u)

        if self.root is None:
            return
        
        # If the Node(u) is exist or Node(v) is not exist, do nothing
        if self.find_node(u, self.root) is not None:
            return
        
        if self.find_node(v, self.root) is None:
            return
        
        # Find the current node with the value "v"
        parent_node = self.find_node(v, self.root)

        if parent_node.left is None:
            parent_node.left = new_node
        
        else:
            curr_node = parent_node.left
            assert isinstance(curr_node, Node)
            while curr_node.right is not None:
                curr_node = curr_node.right
            
            curr_node.right = new_node
    
    def pre_order(self, root:Node) -> None:
        if root is None:
            return

        print(root.value, end=' ')

        curr_node = root.left

        while curr_node is not None:
            assert isinstance(curr_node, Node)
            self.pre_order(curr_node)
            curr_node = curr_node.right
        
    
    def in_order(self, root:Node) -> None:
        if root is None:
            return
        
        self.in_order(root.left)

        print(root.value, end=' ')

        curr_node = root.left
        
        while curr_node is not None:
            if curr_node.right is not None:
                self.in_order(curr_node.right)
            curr_node = curr_node.right
    
    def post_order(self, root: Node) -> None:
        curr_node = root.left

        while curr_node is not None:
            assert isinstance(curr_node, Node)
            self.post_order(curr_node)
            curr_node = curr_node.right
        
        if root is None:
            return
        
        print(root.value, end=' ')

def main():

    commands = []

    while True:
        line = sys.stdin.readline().split()
        
        if line[0] == '*':
            break

        commands.append(line)

    tree = Tree()

    for cmd in commands:
        if cmd[0] == 'MakeRoot':
            tree.make_root(u=int(cmd[1]))

        if cmd[0] == 'Insert':
            tree.insert_(u=int(cmd[1]), v=int(cmd[2]))

        if cmd[0] == 'PreOrder':
            tree.pre_order(tree.root)
            print()

        if cmd[0] == 'InOrder':
            tree.in_order(tree.root)
            print()

        if cmd[0] == 'PostOrder':
            tree.post_order(tree.root)
            print()

    return

if __name__ == '__main__':
    main()