import sys 
input = sys.stdin.readline 
def main():
    t = int(input()) 
    for _ in range(t):
        a, b, c = map(int, input().split()) 
        if a < c:
            first = 1
        else: first = -1
        if a*b>c:
            second = b
        else: second = -1 
        print(first, second)
if __name__ == "__main__":
    main()