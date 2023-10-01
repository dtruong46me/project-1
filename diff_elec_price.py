
def old_evn(e: int) -> float:
    """
    e: electricity consuming (kWh)
    return: the total money according to the electricity consuming
    """

    if (e >= 0 and e <= 50):
        return 1.728 * e
    
    if (e >= 51 and e <= 100):
        return 1.728 * 50 + 1.786 * (e - 50)
    
    if (e >= 101 and e < 200):
        return 1.728 * 50 + 1.786 * 50 + 2.074 * (e - 100)
    
    if (e >= 201 and e <= 300):
        return 1.728 * 50 + 1.786 * 50 + 2.074 * 100 + 2.612 * (e - 200)
    
    if (e >= 301 and e <= 400):
        return 1.728 * 50 + 1.786 * 50 + 2.074 * 100 + 2.612 * 100 + 2.919 * (e - 300)
    
    if (e >= 401):
        return 1.728 * 50 + 1.786 * 50 + 2.074 * 100 + 2.612 * 100 + 2.919 * 100 + 3.015 * (e - 400)
    
    else:
        return 0
    


def new_evn(e: int) -> float:
    if (e >= 0 and e <= 100):
        return 1.728 * e
    
    if (e >= 101 and e <= 200):
        return 1.728 * 100 + 2.074 * (e - 100)
    
    if (e >= 201 and e < 400):
        return 1.728 * 100 + 2.074 * 100 + 2.612 * (e - 200)
    
    if (e >= 401 and e <= 700):
        return 1.728 * 100 + 2.074 * 100 + 2.612 * 200 + 3.111 * (e - 400)
    
    if (e >= 701):
        return 1.728 * 100 + 2.074 * 100 + 2.612 * 200 + 3.111 * 300 + 3.457 * (e - 700)
    
    else:
        return 0
    
def main():

    n = int(input())

    evn1 = old_evn(n) * 1000
    evn2 = new_evn(n) * 1000

    print(f"{1.1 * (evn2 - evn1):.2f}")

if __name__ == "__main__":
    main()