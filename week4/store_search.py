import sys

class Database:
    def __init__(self) -> None:
        self.database = {}
    
    def encode(self, item: str):
        return sum([ord(c) for c in item]) % 10
    
    def find_item(self, item: str):
        code = self.encode(item)

        if code not in self.database:
            return 0
        else:
            if item in self.database[code]:
                return 1
            return 0
    
    def insert_item(self, item: str):
        code = self.encode(item)

        if code not in self.database:
            self.database[code] = [item]
            return 1
        
        # encode of item in database
        else:
            if item in self.database[code]:
                return 0
            else:
                self.database[code].append(item)
                return 1

def main():

    # Define Database
    db = Database()
    while True:
        line = sys.stdin.readline().split()
        if line[0] == '*':
            break
        
        # Encode and Add to database
        code = db.encode(line[0])
        if code not in db.database:
            db.database[code] = [line[0]]

        else:
            assert isinstance(db.database[code], list)
            db.database[code].append(line[0])
    
    # Define Commands
    commands = []
    while True:
        line = sys.stdin.readline().split()
        if line[0] == '***':
            break

        commands.append((line[0], line[1]))
    
    for cmd in commands:
        if cmd[0] == 'find':
            print(db.find_item(cmd[1]))

        if cmd[0] == 'insert':
            print(db.insert_item(cmd[1]))

if __name__ == '__main__':
    main()