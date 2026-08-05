import sys
import math
 
input = sys.stdin.readline
 
def main():
    n,m = map(int,input().split())
    t=math.ceil(n/2)
    for i in range(t,n+1):
        if i%m==0:
            print(i)
            return
    print(-1)
if __name__ == "__main__":
    main()