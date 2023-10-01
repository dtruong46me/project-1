
def check_month(month: str):
    if len(month) != 2:
        return False
    
    if int(month) < 1 or int(month) > 12:
        return False
    
    return True

def check_day(day: str):
    if len(day) != 2:
        return False
    
    if int(day) < 1 or int(day) > 31:
        return False
    
    return True

def main():
    date = [x for x in input().split("-")]

    if len(date) != 3:
        print("INCORRECT")
        return
    
    if check_month(date[1]) == False or check_day(date[2]) == False:
        print("INCORRECT")
        return
    
    print(int(date[0]), int(date[1]), int(date[2]))

    return

if __name__ == '__main__':
    main()