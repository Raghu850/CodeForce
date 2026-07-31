import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    a=list(map(int,input().split()))
    m=sum(a)
    t %= m
    if t == 0:
        t=m
    for i in range(len(a)):
        t -= a[i]
        if t <= 0:
            print(i+1)
            break
 
if __name__ == "__main__":
    main()