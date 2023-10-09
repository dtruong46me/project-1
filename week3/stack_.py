import sys

def main():

    stack = []
    commands = []

    while True:
        line = sys.stdin.readline().split()

        if line[0] == '#':
            break

        if line[0] == 'PUSH':
            commands.append([line[0], int(line[1])])

        if line[0] == 'POP':
            commands.append([line[0]])
    
    for cmd in commands:
        if cmd[0] == 'PUSH':
            stack.append(cmd[1])
        
        if cmd[0] == 'POP':
            if len(stack) == 0:
                print('NULL')

            else:
                p = stack.pop()
                print(p)

    return

if __name__ == '__main__':
    main()