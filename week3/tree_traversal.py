import sys

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.root = None

    def make_root(self, u:int):
        if self.root == None:
            self.root = Node(u)

        return None
    
    def find_node(self, v) -> Node:

        if self.root is None:
            return None
        
        if self.root.value == v:
            return self.root
        
        if self.root.left == None:
            return None
        
        else:
            # Find the left subtree
            curr_node = self.root.left
            assert type(curr_node) == Node

            left_result = curr_node.find_node(v)
            if left_result is not None:
                return left_result
            
            # Find the right sibling subtree
            while curr_node.right is not None:
                curr_node = curr_node.right
                
                assert type(curr_node) == Node

                right_result = curr_node.find_node(v)
                if right_result is not None:
                    return right_result
                
        return None
    
    def insert_(self, u:int, v:int):

        new_node = Node(value=u)

        if self.root == None:
            return
        
        # If the Node(u) and Node(v) are exist, do nothing
        if self.find_node(u) is not None:
            return
        
        if self.find_node(v) is not None:
            return
        
        # Find the current node with the value "v"
        parent_node = self.find_node(v)

        if parent_node.left is None:
            parent_node.left = new_node
        
        else:
            curr_node = parent_node.left
            assert type(curr_node) == Node

            while curr_node.right is not None:
                curr_node = curr_node.right
            
            curr_node.right = new_node
    
    def pre_order(self) -> None:
        return
    
    def in_order(self) -> None:
        return
    
    def post_order(self) -> None:
        return

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
            tree.pre_order()

        if cmd[0] == 'InOrder':
            tree.in_order()

        if cmd[0] == 'PostOrder':
            tree.post_order()

    return

if __name__ == '__main__':
    main()