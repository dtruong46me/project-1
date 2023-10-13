
class State:
    def __init__(self, a, b, step) -> None:
        self.a = a
        self.b = b
        self.step = step


def check_finish(s: State, c) -> bool:
    if s.a == c or s.b == c:
        return True
    
    return False


def solve():

    return

def main():
    a, b, c = [int(x) for x in input().split()]