import sys

class SalesOrder:
    def __init__(self) -> None:
        self.queries = []
        self.shops = dict()

    # Read Input
    def read_input(self):
        while True:
            line = sys.stdin.readline().split()
            if line[0] == '#':
                break
            cus_id, prod_id, price, shop_id, time = [x for x in line]

            if shop_id not in self.shops:
                self.shops[shop_id] = dict()
                self.shops[shop_id][cus_id] = [int(price)]
            
            else:
                if cus_id not in self.shops[shop_id]:
                    self.shops[shop_id][cus_id] = [int(price)]
                    
                else:
                    self.shops[shop_id][cus_id].append(int(price))
        
        while True:
            line = sys.stdin.readline().split()
            if line[0] == '#':
                break
            self.queries.append(line)
    
    # Total number of Orders
    def total_number_orders(self) -> int:
        orders = 0

        for shop in self.shops.keys():
            orders += sum(len(self.shops[shop][cus]) for cus in self.shops[shop].keys())

        return orders
    
    # Total revenue of data
    def total_revenue(self) -> int:
        revenue = 0

        for shop in self.shops.keys():
            revenue += sum(sum(self.shops[shop][cus]) for cus in self.shops[shop].keys())

        return revenue 

    # Total revenue of shop <shop_id>
    def revenue_of_shop(self, shop_id:str) -> int:
        if shop_id not in self.shops:
            return 0
        return sum(sum(self.shops[shop_id][cus]) for cus in self.shops[shop_id].keys())

    # Total consume of customer <customer_id> at shop <shop_id>
    def total_consume_of_customer_shop(self, customer_id:str, shop_id:str) -> int:
        if shop_id not in self.shops:
            return 0
        
        if customer_id not in self.shops[shop_id]:
            return 0
        
        return sum(self.shops[shop_id][customer_id])

    # Total revenue in period <from_time> to <to_time>
    def toal_revenue_in_period(self, from_time, to_time) -> int:
        return
    

    # Handle requests
    def handle_requests(self):
        for query in self.queries:
            if query[0] == '?total_number_orders':
                print(self.total_number_orders())
            
            if query[0] == '?total_revenue':
                print(self.total_revenue())

            if query[0] == '?revenue_of_shop':
                print(self.revenue_of_shop(query[1]))

            if query[0] == '?total_consume_of_customer_shop':
                print(self.total_consume_of_customer_shop(query[1], query[2]))
            
            if query[0] == '?total_revenue_in_period':
                print(self.toal_revenue_in_period(query[1], query[2]))

def main():
    sale_data = SalesOrder()
    sale_data.read_input()
    sale_data.handle_requests()

if __name__ == '__main__':
    main()