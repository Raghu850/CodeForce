import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n,m=map(int,input().split())
        grid=[list(input().strip()) for i in range(n)]
        ans=0
        for i in range(m):
            if grid[n-1][i]=='D':
                ans+=1
        for i in range(n):
            if grid[i][m-1]=="R":
                ans+=1
        print(ans)
if __name__ == "__main__":
    main()