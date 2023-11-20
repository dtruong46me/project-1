import sys
from datetime import datetime

class SaleOrders:
    def __init__(self) -> None:
        self.queries = list()
        self.shops = [list() for _ in range(1000)]
        self.orders = list()
        self.count_order = 0
        self.revenue = 0
    
    def handle_input(self):
        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '#':
                break
            cus_id, prod_id, price, shop_id, timepoint = line
            price = int(price)
            timepoint = datetime.strptime(timepoint, '%H:%M:%S')

            shop_idx = int(shop_id[1:])

            self.shops[shop_idx].append((cus_id, price))
            self.orders.append((price, timepoint))
            self.count_order += 1
            self.revenue += price

        while True:
            line = [x for x in sys.stdin.readline().split()]
            if line[0] == '#':
                break
            self.queries.append(line)
    
    def total_number_orders(self) -> int:
        return self.count_order
    
    def total_revenue(self) -> int:
        return self.revenue
    
    def revenue_of_shop(self, shop_id: str) -> int:
        shop_idx = int(shop_id[1:])
        if len(self.shops[shop_idx]) == 0:
            return 0
        return sum(price for _, price in self.shops[shop_idx])
    
    def total_consume_of_customer_shop(self, cus_id, shop_id):
        shop_idx = int(shop_id[1:])
        if len(self.shops[shop_idx]) == 0 or cus_id not in self.shops[shop_idx]:
            return 0
        return sum(price for cus, price in self.shops[shop_idx] if cus == cus_id)
    
    def total_revenue_in_period(self, from_time:str, to_time:str):
        from_time = datetime.strptime(from_time, '%H:%M:%S')
        to_time = datetime.strptime(to_time, '%H:%M:%S')
        return sum(price for price, timepoint in self.orders if from_time <= timepoint <= to_time)

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
                print(self.total_revenue_in_period(query[1], query[2]))
   
def main():
    sale_db = SaleOrders()
    sale_db.handle_input()
    sale_db.handle_requests()

if __name__ == '__main__':
    main()