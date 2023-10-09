# import sympy as sp

# # Chuỗi đầu vào
# # expression_str = "x^2+sin(x^4+5.2)+log(x^2+4,16)+sqrt(x^4+1)"
# expression_str = "x^2 + log((x/5 + 1/x), 50) + sin(x^ 2)"

# # Chuyển chuỗi thành biểu thức sympy
# x = sp.symbols('x')
# expression = sp.sympify(expression_str)

# # In biểu thức
# print("Biểu thức gốc:", expression)

# # Tính giá trị của biểu thức cho một giá trị x cụ thể
# x_value = 2.0
# result = expression.subs(x, x_value)
# print(f"Giá trị của biểu thức với x = {x_value}: {result}")


import math


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None

class ParseTree:
    def __init__(self, expression:str) -> None:
        self.expression = expression
        self.tokens = self.tokenize(expression)
        self.root = self.build_parse_tree()

    def tokenize(self, expression: str) -> list:

        # tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        tokens = []
        curr_token = ""
        # is_inside_brackets = False

        for char in expression:
            if char.isdigit() or char.isalpha() or char == '.':
                curr_token += char

            else:
                if curr_token:
                    tokens.append(curr_token)
                
                if char.strip():
                    tokens.append(char)
                
                curr_token = ""
        
        if curr_token:
            tokens.append(curr_token)

        return tokens

    def build_parse_tree(self) -> Node:

        stack = []
        root = None
        curr_node = None

        for token in self.tokens:
            if token == '(':
                if curr_node is not None:
                    stack.append(curr_node)
                
                curr_node = None
            
            if token == ')':
                if stack:
                    popped_node = stack.pop() 
                    assert type(popped_node) == Node

                    if popped_node.left is None:
                        popped_node.left = curr_node
                    
                    else:
                        popped_node.right = curr_node

                    curr_node = popped_node
            
            if token in ('log', 'sin', 'cos', 'tan', 'cot', 'sqrt'):
                new_node = Node(token)

                if curr_node:
                    new_node.left = curr_node
                    curr_node = new_node
                
                else:
                    curr_node = new_node

            else:
                curr_node = Node(token)
        
        if root is None:
            root = curr_node
        
        return root

    def print_tree(self, node=None, tabs=0) -> None:
        
        if node is not None:
            node = self.root
        
        if node:
            print(' ' * tabs + str(node.value))

            if node.left:
                self.print_tree(node=node.left, tabs=tabs+2)
            
            if node.right:
                self.print_tree(node=node.right, tabs=tabs+2)
    
    def evaluate(self, x_value):
        
        return self.evaluate_tree(self.root, x_value)
    
    def evaluate_tree(self, node: Node, x_value):
        
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            if node.value == 'x':
                return x_value
            
            else:
                return float(node.value)
    
        left_value = self.evaluate_tree(node=node.left, x_value=x_value)
        right_value = self.evaluate_tree(node=node.right, x_value=x_value)

        if node.value == '+':
            return left_value + right_value
        
        if node.value == '-':
            return left_value - right_value
        
        if node.value == '*':
            return left_value * right_value
        
        if node.value == '/':
            return left_value / right_value
        
        if node.value == '^' or node.value == '**':
            return left_value ** right_value
        
        if node.value == 'sin':
            return math.sin(left_value)
        
        if node.value == 'cos':
            return math.cos(left_value)
        
        if node.value == 'tan':
            return math.tan(left_value)
        
        if node.value == 'cot':
            return 1 / math.tan(left_value)
        
        if node.value == 'log':
            if node.right is None:
                return math.log10(left_value)
            return math.log(x=left_value, base=right_value)
        
        if node.value == 'ln':
            return math.log(x=left_value, base=math.e)
        
        if node.value == 'sqrt':
            return math.sqrt(left_value)

