import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        print(2)
        if n==2:
            print(1,2)
            continue
        print(n,n-2)
        curr=n-1
        print(curr,curr)
        for x in range(n-3,0,-1):
            print(curr,x)
            curr=(curr+x+1)//2
 
 
if __name__ == "__main__":
    main()