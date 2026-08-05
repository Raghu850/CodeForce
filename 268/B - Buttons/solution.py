import sys
 
input = sys.stdin.readline
 
def main():
    n = int(input()) 
    ans = n 
    for i in range(1, n):
        ans += (n - i) * i 
    print(ans)
if __name__ == "__main__":
    main()