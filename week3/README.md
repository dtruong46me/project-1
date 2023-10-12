## Linked List Manipulation
**Description**

Viết chương trình thực hiện công việc sau:

Xây dựng danh sách liên kết với các khóa được cung cấp ban đầu là dãy a1, a2, …, an, sau đó thực hiện các thao tác trên danh sách bao gồm: thêm 1 phần tử vào đầu, vào cuối danh sách, hoặc vào trước, vào sau 1 phần tử nào đó trong danh sách, hoặc loại bỏ 1 phần tử nào đó trong danh sách

**Input**
- Dòng 1: ghi số nguyên dương n (1 <= n <= 1000)

- Dòng 2: ghi các số nguyên dương a1, a2,...an

- Các dòng tiếp theo lần lượt là các lệnh để thao tác (kết thúc bởi ký hiệu #) với các loại sau:

    - addlast  k: thêm phần tử có key bằng k vào cuối danh sách (nếu k chưa tồn tại)

    - addfirst  k: thêm phần tử có key bằng k vào đầu danh sách (nếu k chưa tồn tại)

    - addafter  u  v: thêm phần tử có key bằng u vào sau phần tử có key bằng v trên danh sách (nếu v đã tồn tại trên danh sách và u chưa tồn tại)
    
    - addbefore  u  v: thêm phần tử có key bằng  u vào trước phần tử có key bằng v trên danh sách (nếu v đã tồn tại trên danh sách và u của tồn tại)
    
    - remove  k: loại bỏ phần tử có key bằng k khỏi danh sách
    
    - reverse: đảo ngược thứ tự các phần tử của danh sách (không được cấp phát mới các phần tử, chỉ được thay đổi mối nối liên kết)

**Output**
- Ghi ra dãy khóa của danh sách thu được sau 1 chuỗi các lệnh thao tác đã cho

**Example**

***Input:***

5

5 4 3 2 1

addlast 3

addlast 10

addfirst 1

addafter 10 4

remove 1

\#

***Output***

5 4 3 2 10 


## Family Tree

**Description**

Given a family tree represented by child-parent (c,p) relations in which c is a child of p. Perform queries about the family tree:

- descendants <name>: return number of descendants of the given <name>

- generation <name>: return the number of generations of the descendants of the given <name>

Note that: the total number of people in the family is less than or equal to 10^4

**Input**

Contains 2 blocks. 

- The first block contains information about child-parent, including lines (terminated by a line containing \*\*\*), each line contains: <child> <parent> where <child> is a string represented the name of the child and <parent> is a string represented the name of the parent. 

- The second block contains lines (terminated by a line containing ***), each line contains two string <cmd> and <param> where <cmd> is the command (which can be descendants or generation) and <param> is the given name of the person participating in the  query.

**Output**

Each line is the result of a corresponding query.

**Example**

***Input***

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

\***

descendants Newman

descendants Mark

descendants David

generation Mark

\***

***Output***

10

5

2

2


## BST - Insertion and PreOrder 

**Description**

Given a BST initialized by NULL. Perform a sequence of operations on a BST including:

- insert k: insert a key k into the BST (do not insert if the key k exists)

**Input**

- Each line contains command under the form: “insert k”

- The input is terminated by a line containing #

**Output**

- Write the sequence of keys of nodes visited by the pre-order traversal (separated by a SPACE character)

**Example**

***Input***

insert 20

insert 10

insert 26

insert 7

insert 15

insert 23

insert 30

insert 3

insert 8

\#

***Output***

20 10 7 3 8 15 26 23 30


## Water Jugs

**Description**

There are two jugs, a-litres jug and b-litres jug (a, b are positive integers). There is a pump with unlimited water. Given a positive integer c, how to get exactly c litres.

**Input**
- Line 1: contains positive integers a,   b,  c  (1 <= a, b, c <= 900)

**Output**
- Write the number of steps or write -1 (if no solution found)

**Example**

***Input***

6 8 4

***Output***

4


## Tree Manipulation & Traversal

**Description

Mỗi nút trên cây có trường id (identifier) là một số nguyên (id của các nút trên cây đôi một khác nhau)
Thực hiện 1 chuỗi các hành động sau đây bao gồm các thao tác liên quan đến xây dựng cây và duyệt cây

- MakeRoot u: Tạo ra nút gốc u của cây

- Insert u v: tạo mới 1 nút u và chèn vào cuối danh sách nút con của nút v (nếu nút có id bằng v không tồn tại hoặc nút có id bằng u đã tồn tại thì không chèn thêm mới)

- PreOrder: in ra thứ tự các nút trong phép duyệt cây theo thứ tự trước

- InOrder: in ra thứ tự các nút trong phép duyệt cây theo thứ tự giữa

- PostOrder: in ra thứ tự các nút trong phép duyệt cây theo thứ tự sau

**Input:** Bao gồm các dòng, mỗi dòng là 1 trong số các hành động được mô tả ở trên, dòng cuối dùng là * (đánh dấu sự kết thúc của dữ liệu).

**Kết quả:** Ghi ra trên mỗi dòng, thứ tự các nút được thăm trong phép duyệt theo thứ tự trước, giữa, sau của các hành động PreOrder, InOrder, PostOrder tương ứng đọc được từ dữ liệu đầu vào

**Example**

***Input***

MakeRoot 10

Insert 11 10

Insert 1 10

Insert 3 10

InOrder

Insert 5 11

Insert 4 11

Insert 8 3

PreOrder

Insert 2 3

Insert 7 3

Insert 6 4

Insert 9 4

InOrder

PostOrder

\*

***Output***

11 10 1 3

10 11 5 4 1 3 8

5 11 6 4 9 10 1 8 3 2 7

5 6 9 4 11 1 8 2 7 3 10