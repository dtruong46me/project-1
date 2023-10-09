
from parse_tree import ParseTree

test_expression = "x ^ 2+log((x/5+1/x),50 ) + sin( x^2 +1)+sqrt (x^2+1)-5.5*x"

parse_tree = ParseTree(expression=test_expression)

print("Parse Tree: ")
parse_tree.print_tree()

x0 = 2.0

result = parse_tree.evaluate(x_value=x0)

print(result)