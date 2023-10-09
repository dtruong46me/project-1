
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class ParseTree:
    def __init__(self, expression: str) -> None:
        self.expression = expression
        self.tokens = self.tokenize(expression)
        self.root = self.build_parse_tree()

    def tokenize(self, expression: str) -> list:

        tokens = []

        for e in expression:
            tokens.append(e)

        return tokens

    def build_parse_tree(self) -> Node:

        return 
        

expression = "5*x^2+4*x-18"
pt = ParseTree(expression=expression)