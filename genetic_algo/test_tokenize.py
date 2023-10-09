
from parse_tree import ParseTree

test_expression = "x ^ 2+log((x/5+1/x),50 ) + sin( x^2 +1)+sqrt (x^2+1)-5.5*x"
# test_expression = test_expression.strip()

test_parse_tree = ParseTree(expression=test_expression)

tokens = test_parse_tree.tokenize(expression=test_expression)
print(tokens)