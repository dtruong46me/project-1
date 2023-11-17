import sys

'''
<from_account> <to_account> <money> <time_point> <atm>

- <from_account>: the account from which money is transferred (which is a string of length from 6 to 20 )
- <to_account>: the account which receives money in the transaction (which is a string of length from 6 to 20)
- <money>: amount of money transferred in the transaction (which is an integer from 1 to 10000)
- <time_point>: the time point at which the transaction is performed, it is a string under the format HH:MM:SS  (hour: minute: second)
- <atm>: the code of the ATM where the transaction is taken (a string of length from 3 to 10)
'''
class Transaction:
    def __init__(self) -> None:
        self.queries = []
        self.accounts = set()
        self.transactions = dict()

    # Read input
    def read_input(self):
        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '#':
                break
            from_acc, to_acc, money, time, bank = [ele for ele in line]
            
            self.accounts.add(from_acc)
            self.accounts.add(to_acc)
            
            if from_acc not in self.transactions:
                self.transactions[from_acc] = [(int(money), to_acc)]
            
            else:
                self.transactions[from_acc].append((int(money), to_acc))
        
        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '#':
                break

            self.queries.append(line)
    

    # Total number of transactions
    def number_transactions(self) -> int:
        return sum([len(self.transactions[from_acc]) for from_acc in self.transactions.keys()])
    
    
    # Total money of transactions
    def total_money_transaction(self) -> int:
        total_money = 0
        for acc in self.transactions.keys():
            total_money += sum(self.transactions[acc][x][0] for x in range(len(self.transactions[acc])))

        return total_money
    

    # List all account in transactions
    def list_sorted_accounts(self):

        return sorted(list(self.accounts))
    

    # Total money transaction from <account>
    def total_money_transaction_from(self, account: str) -> int:
        if account not in self.transactions:
            return 0
        return sum(self.transactions[account][x][0] for x in range(len(self.transactions[account])))
    

    # Check cycle transaction
    def inspect_cycle(self, account: str, k: str) -> bool:
        if account not in self.transactions:
            return False

        def dfs(node, start, k: int, visited: set):
            if k == 0:
                if node == start:
                    return True
                return False
            
            visited.add(node)
            
            if node in self.transactions:
                for _, next_node in self.transactions[node]:
                    if next_node not in visited and dfs(next_node, start, k-1, visited):
                        return True
            
            visited.remove(node)
            return False

        visited = set()
        
        for _, next_node in self.transactions[account]:
            if dfs(next_node, account, int(k)-1, visited):
                return True

        return False
    

    # Read Request
    def handle_requests(self):
        for query in self.queries:
            if query[0] == '?number_transactions':
                print(self.number_transactions())
            
            if query[0] == '?total_money_transaction':
                print(self.total_money_transaction())

            if query[0] == '?list_sorted_accounts':
                print(' '.join(self.list_sorted_accounts()))
            
            if query[0] == '?total_money_transaction_from':
                print(self.total_money_transaction_from(query[1]))
            
            if query[0] == '?inspect_cycle':
                if self.inspect_cycle(query[1], query[2]) == True:
                    print(1)
                else:
                    print(0)


def main():
    trans = Transaction()
    trans.read_input()

    trans.handle_requests()

    return

if __name__ == '__main__':
    main()