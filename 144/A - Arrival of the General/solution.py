import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    a=list(map(int,input().split()))
    max_h=max(a)
    min_h=min(a)
    max_p=a.index(max_h)
    min_p=t-1-a[::-1].index(min_h)
    ans=max_p+(t-1-min_p)
    if max_p>min_p:
        ans-=1
    print(ans)
 
if __name__ == "__main__":
    main()