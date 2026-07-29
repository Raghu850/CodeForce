import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    a=list(map(int,input().split()))
    ans=[0]*t
    for i in range(t):
        reciver=a[i]
        ans[reciver-1]=i+1
    print(*ans)
 
if __name__ == "__main__":
    main()