
import sys

class FamilyTree:
    def __init__(self, root=None) -> None:
        self.root = root
        self.family = {}
    
    def creat_tree(self, members: list):
        for child, parent in members:
            if parent not in self.family:
                self.family[parent] = []
            
            assert isinstance(self.family[parent], list)
            self.family[parent].append(child)

    # Get the number of descendants of {name}
    def descedants(self, name: str) -> int:
        if name not in self.family:
            return 0

        if len(self.family[name]) == 0:
            return 0
        
        else:
            count = 0
            count += len(self.family[name])
            for child in self.family[name]:
                count += self.descedants(child)
        
        return count
    
    # Get the number of Generations of the descendants of {name}
    def generations(self, name: str) -> int:
        if name not in self.family:
            return 0
        
        if len(self.family[name]) == 0:
            return 0
        
        else:
            count = 1
            count += max([self.generations(child) for child in self.family[name]])
        
        return count

def main():
    # Get Child-Parent from the First Block
    members = []
    while True:
        line = sys.stdin.readline().split()
        
        if line[0] == '***':
            break

        members.append(line)

    # Get Commands from the Second Block
    commands = []
    while True:
        line = sys.stdin.readline().split()

        if line[0] == '***':
            break

        commands.append(line)
    
    # Create Family Tree
    family_tree = FamilyTree()
    family_tree.creat_tree(members)

    # Handle Commands
    for cmd in commands:
        if cmd[0] == 'descendants':
            d = family_tree.descedants(name=cmd[1])
            print(d)
        if cmd[0] == 'generation':
            g = family_tree.generations(name=cmd[1])
            print(g)
    

if __name__ == '__main__':
    main()

'''
Peter Newman
Michael Thomas
John David
Paul Mark
Stephan Mark
Pierre Thomas
Mark Newman
Bill David
David Newman
Thomas Mark
***
descendants Newman
descendants Mark
descendants David
generation Mark
***
'''