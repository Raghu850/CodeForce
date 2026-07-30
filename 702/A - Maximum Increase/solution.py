import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    a=list(map(int,input().split()))
    m=1
    ans=0
    for i in range(t-1,0,-1):
        if a[i]>a[i-1]:
            m+=1
        else:
            ans=max(ans,m)
            m=1
    ans=max(ans,m)
    print(ans)
        
if __name__ == "__main__":
    main()