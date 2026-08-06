import sys
 
input = sys.stdin.readline
 
def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    current = 1
    while current < t:
        current += a[current - 1]
    if current == t:
        print("YES")
    else:
        print("NO")
 
if __name__ == "__main__":
    main()