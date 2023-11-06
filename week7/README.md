## Bank Transaction

**Description**

The data about bank transactions consists of a sequence of transactions: the information of each transaction has the following format:

`<from_account>   <to_account>   <money>   <time_point>   <atm>`

In which:
> - <from_account>: the account from which money is transferred (which is a string of length from 6 to 20 )
> - <to_account>: the account which receives money in the transaction (which is a string of length from 6 to 20)
> - <money>: amount of money transferred in the transaction (which is an integer from 1 to 10000)
> - <time_point>: the time point at which the transaction is performed, it is a string under the format HH:MM:SS  (hour: minute: second)
> - <atm>: the code of the ATM where the transaction is taken (a string of length from 3 to 10)

**Example:**

T00112233445 T001234002 2000 08:36:25 BIDV (at the ATM BIDV, account T00112233445 transfers 2000$ to account T001234002 at time point 08:36:25 (08 hour, 36 minutes, 25 seconds))

A transaction cycle of length k starting from account a1 is defined to be a sequence of distinct account a1, a2, …, ak  in which there are transactions from account a1 to a2, from a2 to a3, …, from ak to a1.

Write a program that process the following queries: 

- `?number_transactions`: compute the total number of transactions of the data

- `?total_money_transaction`: compute the total amount of money of transactions

- `?list_sorted_accounts`: compute the sequence of bank accounts (including sending and receiving accounts) appearing in the transaction (sorted in an increasing (alphabetical) order) 

- `?total_money_transaction_from <account>`: compute the total amount of money transferred from the account <account>

- `?inspect_cycle <account> k` : return 1 if there is a transaction cycle of length k, starting from <account>, and return 0, otherwise

**Input**

The input consists of 2 blocks of information: the data block and the query block

- The data block consists of lines:
    
    - Each line contains the information about a transaction described above
    
    - The data is terminated by a line containing #
- The query block consists of lines:
    
    - Each line is a query described above
    
    - The query block is terminated by a line containing #

**Output**

Print to stdout (in each line) the result of each query described above

**Example**

Input

    T000010010 T000010020 1000 10:20:30 ATM1
    T000010010 T000010030 2000 10:02:30 ATM2
    T000010010 T000010040 1500 09:23:30 ATM1
    T000010020 T000010030 3000 08:20:31 ATM1
    T000010030 T000010010 4000 12:40:00 ATM2
    T000010040 T000010010 2000 10:30:00 ATM1
    T000010020 T000010040 3000 08:20:31 ATM1
    T000010040 T000010030 2000 11:30:00 ATM1
    T000010040 T000010030 1000 18:30:00 ATM1
    #
    ?number_transactions
    ?total_money_transaction
    ?list_sorted_accounts
    ?total_money_transaction_from T000010010
    ?inspect_cycle T000010010 3
    #

Output

    9
    19500
    T000010010 T000010020 T000010030 T000010040
    4500
    1


## Analyze Sales Order

**Description**

Data about sales in an e-commerce company (the e-commerce company has several shops) consists a sequence of lines, each line (represents an order) has the following information:

`<CustomerID> <ProductID> <Price> <ShopID> <TimePoint>`

In which the customer `<CustomerID>` buys a product `<ProductID>` with price `<Price>` at the shop `<ShopID>` at the time-point `<TimePoint>`

> - `<CustomerID>`: string of length from 3 to 10
> - `<ProductID>`: string of length from 3 to 10
> - `<Price>`: a positive integer from 1 to 1000
> - `<ShopID>`: string of length from 3 to 10
> - `<TimePoint>`: string representing time-point with the format HH:MM:SS (for example, 09:45:20 means the time-point 9 hour 45 minutes 20 seconds)

Perform a sequence of queries of following types:

- `?total_number_orders`: return the total number of orders

- `?total_revenue`: return the total revenue the e-commerce company gets

- `?revenue_of_shop <ShopID>`: return the total revenue the shop `<ShopID>` gets 

- `?total_consume_of_customer_shop <CustomerID> <ShopID>`: return the total revenue the shop `<ShopID>` sells products to customer `<CustomerID>` 

- `?total_revenue_in_period <from_time> <to_time>`: return the total revenue the e-commerce gets of the period from `<from_time>` to `<to_time> `(inclusive)

**Input**

The input consists of two blocks of data:
- The first block is the operational data, which is a sequence of lines (number of lines can be upto 100000), each line contains the information of a submission with above format. The first block is terminated with a line containing the character #

- The second block is the query block, which is a sequence of lines (number of lines can be upto 100000), each line is a query described above. The second block is terminated with a line containing the character #

**Output**

Write in each line, the result of the corresponding query 

**Example**

Input

    C001 P001 10 SHOP001 10:30:10
    C001 P002 30 SHOP001 12:30:10
    C003 P001 40 SHOP002 10:15:20
    C001 P001 80 SHOP002 08:40:10
    C002 P001 130 SHOP001 10:30:10
    C002 P001 160 SHOP003 11:30:20
    #
    ?total_number_orders
    ?total_revenue
    ?revenue_of_shop SHOP001
    ?total_consume_of_customer_shop C001 SHOP001 
    ?total_revenue_in_period 10:00:00 18:40:45
    #

Output 

    6
    450
    170
    40
    370