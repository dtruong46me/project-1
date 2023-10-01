
def check_correct(elements: list) -> bool:

    if int(elements[0]) > 23 or int(elements[0]) < 0:
        # print(1)
        return True
    
    if int(elements[1]) > 59 or int(elements[2]) > 59 or int(elements[1]) < 0 or int(elements[2]) < 0:
        return True

    for e in elements:
        
        if len(e) != 2:
            return True
    return

def main():
    elements = input().split(":")

    if len(elements) != 3:
        print("INCORRECT")
        return

    if check_correct(elements):
        print("INCORRECT")
        return
    
    result = int(elements[0]) * 3600 + int(elements[1]) * 60 + int(elements[2])

    print(result)


if __name__ == '__main__':
    main()
