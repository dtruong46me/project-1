import sys

class CitizenDB:
    def __init__(self) -> None:
        self.codes = dict()
        self.dob = []
        self.father = []
        self.mother = []
        self.is_alive = []
        self.region_code = []
    
    def read_input(self):
        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '*':
                break
            code, dob, father, mother, is_alive, region = [x for x in line]
            
            if code not in self.codes:
                self.codes[code] = []
            
            self.codes[code].append((dob, father, mother, is_alive, region))
        
        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '***':
                break

    
    def number_people(self) -> int:
        pass

    def born_at(self, date: str) -> int:
        pass

    def max_unrelated_people(self) -> int:
        pass

    def most_alive_ancestor(self, code: str) -> int:
        pass

    def born_between(self, from_date: str, to_date: str) -> int:
        pass

if __name__ == '__main__':
    citizen_db = CitizenDB()
    citizen_db.read_input()
    for code, info in citizen_db.codes.items():
        print(code, info)