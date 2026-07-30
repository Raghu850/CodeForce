import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        x=input().strip()
        d=int(x[0])
        n=len(x)
        ans=(d-1)*10+n*(n+1)//2
        print(ans)
 
if __name__ == "__main__":
    main()