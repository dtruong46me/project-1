
import sys

class SaleOrder:
    def __init__(self) -> None:
        self.queries = list()
        self.shops = dict()
        self.orders = [0 for _ in range(24*60*60+1)]
    
    def convert_date(self, datestring: str) -> int:
        # datestring: 10:45:30 -> 10*60*60 + 45*60 + 30
        hh, mm, ss = [int(x) for x in datestring.split(':')]
        return hh*60*60 + mm*60 + ss

    def read_input(self):
        while True:
            line = sys.stdin.readline().split()
            if line[0] == '#':
                break

            cus_id, prod_id, price, shop_id, timepoint = line

            time_index = self.convert_date(timepoint)
            if self.orders[time_index] != 0:
                self.orders[time_index] += int(price)
            else:
                self.orders[time_index] = int(price)

            if shop_id not in self.shops:
                self.shops[shop_id] = dict()
            
            if cus_id not in self.shops[shop_id]:
                self.shops[shop_id][cus_id] = []
            
            self.shops[shop_id][cus_id].append(int(price))

        while True:
            line = sys.stdin.readline().split()
            if line[0] == '#':
                break
            self.queries.append(line)

    def total_number_orders(self):
        return sum(sum(len(orders) for orders in self.shops[shop].values()) for shop in self.shops.keys())
    
    def total_revenue(self):
        return sum(sum(sum(orders) for orders in self.shops[shop].values()) for shop in self.shops.keys())
    
    def revenue_of_shop(self, shopid: str) -> int:
        if shopid not in self.shops.keys():
            return 0
        return sum(sum(sum(orders) for orders in self.shops[shop].values()) for shop in self.shops.keys() if shop==shopid)
    
    def total_cunsume_of_customer_shop(self, cusid: str, shopid: str) -> int:
        if shopid not in self.shops.keys():
            return 0
        if cusid not in self.shops[shopid].keys():
            return 0
        return sum(sum(sum(orders) for cus, orders in self.shops[shop].items() if cus==cusid) for shop in self.shops.keys() if shop==shopid)
    
    def total_revenue_in_period(self, start_time: str, end_time: str) -> int:
        start = self.convert_date(start_time)
        end = self.convert_date(end_time)

        return sum(self.orders[start:end])

    def handle_requests(self):
        for query in self.queries:
            if query[0] == '?total_number_orders':
                print(self.total_number_orders())
            
            if query[0] == '?total_revenue':
                print(self.total_revenue())
            
            if query[0] == '?revenue_of_shop':
                print(self.revenue_of_shop(query[1]))
            
            if query[0] == '?total_consume_of_customer_shop':
                print(self.total_cunsume_of_customer_shop(query[1], query[2]))

            if query[0] == '?total_revenue_in_period':
                print(self.total_revenue_in_period(query[1], query[2]))


def main():
    sales = SaleOrder()
    sales.read_input()
    sales.handle_requests()

if __name__ == '__main__':
    main()