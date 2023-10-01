import math

def delta(a, b, c) -> float:
    return b ** 2 - 4 * a * c

def main():
    
    a, b, c = [int(x) for x in input().split()]

    d = delta(a, b, c)

    if d < 0:
        print("NO SOLUTION")
        return
    
    if d == 0:
        x0 = - b / (2 * a)
        print(f"{x0:.2f}")
        return
    
    if d > 0:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)

        print(f"{x1:.2f} {x2:.2f}")
        return
    
if __name__ == "__main__":
    main()