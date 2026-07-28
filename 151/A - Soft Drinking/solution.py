import sys
 
input = sys.stdin.readline
 
def main():
    n,k,l,c,d,p,nl,np= map(int,input().split())
    a=(k*l)//nl
    b=c*d
    i=p//np
    ans=min(a,b,i)//n
    print(ans)
if __name__ == "__main__":
    main()