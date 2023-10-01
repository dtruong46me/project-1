
def find_occur(text: str, pattern: str) -> list:
    
    occur = []
    i = 0

    while i < len(text):
        if text[i: i+len(pattern)] == pattern:
            occur.append(i)
            i += len(pattern)

        else:
            i += 1
    
    return occur

def replace_text(text: str, old_pattern: str, new_pattern: str) -> str:
    # print(1)
    occur = find_occur(text, old_pattern)

    if len(occur) == 0:
        return text
    
    text_replace = []
    pointer = 0

    for i in occur:
        # print(text_replace)
        # print(1)
        text_replace.append(text[pointer: i])
        text_replace.append(new_pattern)
        pointer = i + len(old_pattern)

    text_replace.append(text[pointer:])

    return ''.join(text_replace)

def main():

    p1 = input()

    p2 = input()

    t = input()

    result = replace_text(text=t, old_pattern=p1, new_pattern=p2)

    # result = t.replace(p1, p2)

    print(result)

if __name__ == '__main__':
    main()