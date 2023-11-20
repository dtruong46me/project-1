import sys
from datetime import datetime

class CitizenDatabase:
    def __init__(self) -> None:
        self.people = dict()
        self.queries = list()
    
    def read_input(self):
        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '*':
                break

            code, dob, father, mother, is_alive, region = line
            
            self.people[code] = {'dob': dob, 'father': father, 'mother': mother, 'alive': is_alive, 'region': region}

        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '***':
                break
            self.queries.append(line)

    def number_people(self) -> int:
        return len(self.people)

    def born_at(self, date: str) -> int:
        date = datetime.strptime(date, '%Y-%m-%d')
        return sum(1 for person in self.people.values() if datetime.strptime(person['dob'], '%Y-%m-%d')==date)

    def max_unrelated_people(self) -> int:
        unrelated_sets = []
        visited = set()

        def dfs(code, current_set):
            visited.add(code)
            current_set.add(code)

            for relative_code in [self.people[code]['father'], self.people[code]['mother']]:
                if relative_code not in visited and relative_code != '0000000':
                    dfs(relative_code, current_set)

        for code in self.people.keys():
            if code not in visited:
                current_set = set()
                dfs(code, current_set)
                unrelated_sets.append(current_set)

        return max(len(s) for s in unrelated_sets)

    def most_alive_ancestor(self, code: str) -> int:
        def find_ancestor_depth(person_code, depth):
            if person_code == '0000000' or person_code not in self.people:
                return depth - 1
            return max(find_ancestor_depth(self.people[person_code]['father'], depth + 1), find_ancestor_depth(self.people[person_code]['mother'], depth + 1))

        return find_ancestor_depth(code, 0)

    def born_between(self, from_date: str, to_date: str) -> int:
        from_date = datetime.strptime(from_date, '%Y-%m-%d')
        to_date = datetime.strptime(to_date, '%Y-%m-%d')

        return sum(1 for person in self.people.values() if from_date <= datetime.strptime(person['dob'], '%Y-%m-%d') <= to_date)

    def handle_requests(self):
        for query in self.queries:
            if query[0] == 'NUMBER_PEOPLE':
                print(self.number_people())
            
            if query[0] == 'NUMBER_PEOPLE_BORN_AT':
                print(self.born_at(query[1]))
            
            if query[0] == 'MOST_ALIVE_ANCESTOR':
                print(self.most_alive_ancestor(query[1]))
            
            if query[0] == 'NUMBER_PEOPLE_BORN_BETWEEN':
                print(self.born_between(query[1], query[2]))
            
            if query[0] == 'MAX_UNRELATED_PEOPLE':
                print(self.max_unrelated_people())

def main():
    citizen_db = CitizenDatabase()
    citizen_db.read_input()
    citizen_db.handle_requests()

if __name__ == '__main__':
    main()

'''
0000001 1920-08-10 0000000 0000000 Y 00002
0000002 1920-11-03 0000000 0000000 Y 00003
0000003 1948-02-13 0000001 0000002 Y 00005
0000004 1946-01-16 0000001 0000002 Y 00005
0000005 1920-11-27 0000000 0000000 Y 00005
0000006 1920-02-29 0000000 0000000 Y 00004
0000007 1948-07-18 0000005 0000006 Y 00005
0000008 1948-07-18 0000005 0000006 Y 00002
0000009 1920-03-09 0000000 0000000 Y 00005
0000010 1920-10-16 0000000 0000000 Y 00005
*
NUMBER_PEOPLE
NUMBER_PEOPLE_BORN_AT 1919-12-10
NUMBER_PEOPLE_BORN_AT 1948-07-18
MAX_UNRELATED_PEOPLE
MOST_ALIVE_ANCESTOR 0000008
MOST_ALIVE_ANCESTOR 0000001
NUMBER_PEOPLE_BORN_BETWEEN 1900-12-19 1928-11-16
NUMBER_PEOPLE_BORN_BETWEEN 1944-08-13 1977-12-15
NUMBER_PEOPLE_BORN_BETWEEN 1987-01-24 1988-06-03
***
'''