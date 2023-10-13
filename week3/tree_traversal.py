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
            print("Found", v)
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
    def insert_(self, u:int, v:int):
        new_node = Node(value=u)

        if self.root is None:
            return
        
        # If the Node(u) and Node(v) are exist, do nothing
        if self.find_node(u, self.root) is not None:
            return
        
        if self.find_node(v, self.root) is None:
            return
        
        # Find the current node with the value "v"
        print(v)
        parent_node = self.find_node(v, self.root)
        print("parent_node:", parent_node)

        if parent_node is None:
            return

        if parent_node.left is None:
            parent_node.left = new_node
            print("inserted", u, v)
        
        else:
            curr_node = parent_node.left
            assert type(curr_node) == Node

            while curr_node.right is not None:
                curr_node = curr_node.right
            
            curr_node.right = new_node
    
    def pre_order(self, root:Node) -> None:
        if root is None:
            return

        if root is not None:
            print(root.value, end='--')

        curr_node =root.left

        while curr_node is not None:
            self.pre_order(curr_node)

            curr_node = curr_node.right
        
    
    def in_order(self, root=None) -> None:
        if root is None:
            return
        
        if root is not None:
            assert isinstance(root, Node)
            if root.left is not None:
                self.in_order(root.left)
            
            curr_node = root.left
            # assert isinstance(curr_node, Node)

            while curr_node is not None:
                print(curr_node.value, end='--')
                self.in_order(curr_node)
                curr_node = curr_node.right
    
    def post_order(self, root=None) -> None:
        if root is None:
            return
        
        curr_node = root.left
        while curr_node is not None:
            self.post_order(curr_node)
            curr_node = curr_node.right
        
        if curr_node is not None:
            print(curr_node, end='--')

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

        if cmd[0] == 'InOrder':
            tree.in_order()

        if cmd[0] == 'PostOrder':
            tree.post_order()

    return

if __name__ == '__main__':
    main()