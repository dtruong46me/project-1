
import sys

class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.root = None

    # Creat Linked List
    def creat(self, arrays: list):
        for i in arrays:
            self.addlast(i)

    # Check if Node(k) in the Linked List
    def check(self, k) -> Node:
        curr_node = self.root
        if self.root is None:
            return

        while curr_node is not None:
            if curr_node.value == k:
                return curr_node
            curr_node = curr_node.next

    # Add Node(k) to the last of Linked List
    def addlast(self, k: int):
        new_node = Node(k)

        curr_node = self.root
        if self.root is None:
            self.root = new_node
            return

        if self.root == k:
            return

        while curr_node.next is not None:
            if curr_node.value == k:
                return
            curr_node = curr_node.next
        
        curr_node.next = new_node
    
    # Add Node(k) to the first of Linked List
    def addfirst(self, k: int):
        new_node = Node(k)
        
        result = self.check(k)
        if result is not None:
            return
        
        new_node.next = self.root
        self.root = new_node

    # Add Node(u) after Node(v)
    def addafter(self, u: int, v: int):
        check_u = self.check(u)
        if check_u is not None:
            return

        check_v = self.check(v)
        if check_v is not None:
            new_node = Node(u)
            new_node.next, check_v.next = check_v.next, new_node

        return

    # Add Node(u) before Node(v)
    def addbefore(self, u: int, v: int):
        new_node = Node(u)

        check_u = self.check(u)
        if check_u is not None:
            return
        
        curr_node = self.root
        if curr_node.value == v:
            new_node.next = self.root
            self.root = new_node
        
        else:
            while curr_node is not None:
                if curr_node.value == v:
                    break

                prev_node = curr_node
                curr_node = curr_node.next
            
            new_node.next = prev_node.next
            prev_node.next = new_node
    
    # Remove Node(k)
    def remove(self, k: int):
        curr_node = self.root
        prev_node = None

        check_k = self.check(k)
        if check_k is None:
            return

        while curr_node is not None and curr_node.value == k:
            self.root = curr_node.next
            curr_node = self.root
        
        while curr_node is not None and curr_node.value != k:
            prev_node = curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            return self.root
        
        prev_node.next = curr_node.next
        curr_node = prev_node.next

    # Reverse Linked List
    def reverse(self):
        curr_node = self.root
        prev_node = None

        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        self.root = prev_node
    
    # Print Linked List
    def print(self):
        if self.root is None:
            print()
            return
        
        curr_node = self.root
        while curr_node is not None:
            print(curr_node.value, end=' ')
            curr_node = curr_node.next

def main():
    n = int(sys.stdin.readline())

    arrays = [int(x) for x in sys.stdin.readline().split()]

    commands = []
    while True:
        line = sys.stdin.readline().split()
        
        if line[0] == '#':
            break

        commands.append(line)
    
    linked_list = LinkedList()
    linked_list.creat(arrays)

    for cmd in commands:
        if cmd[0] == 'addlast':
            linked_list.addlast(k=int(cmd[1]))
        
        if cmd[0] == 'addfirst':
            linked_list.addfirst(k=int(cmd[1]))

        if cmd[0] == 'addafter':
            linked_list.addafter(u=int(cmd[1]), v=int(cmd[2]))

        if cmd[0] == 'addbefore':
            linked_list.addbefore(u=int(cmd[1]), v=int(cmd[2]))
        
        if cmd[0] == 'remove':
            linked_list.remove(k=int(cmd[1]))
        
        if cmd[0] == 'reverse':
            linked_list.reverse()
    
    linked_list.print()
    return

if __name__ == '__main__':
    main()
