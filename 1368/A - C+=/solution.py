import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        a,b,n=map(int,input().split())
        ans=0
        while max(a,b)<=n:
            if a<b:
                a+=b
            else:
                b+=a
            ans+=1
        print(ans)
 
if __name__ == "__main__":
    main()