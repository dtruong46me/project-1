
def check(p:str, s:str) -> bool:
    o = ['{', '[', '(']
    c = ['}', ']', ')']

    if o.index(p) != c.index(s):
        return False
    
    return True

def main():

    string_ = input()
    stack = []

    for s in string_:

        if s in '{[(':
            stack.append(s)
        
        if s in '})]':
            if len(stack) == 0:
                print(0)
                return
            
            else:
                p = stack.pop()

                if check(p, s) == False:
                    print(0)
                    return
                
    if len(stack) != 0:
        print(0)
        return
    
    print(1)
    # return

if __name__ == '__main__':
    main()