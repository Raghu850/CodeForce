import sys
 
input = sys.stdin.readline
 
def main():
    n,m = map(int,input().split())
    if m%n!=0:
        print(-1)
        return 
    x=m//n
    mov=0
    while x%2==0:
        x//=2
        mov+=1
    while x%3==0:
        x//=3
        mov+=1
    if x==1:
        print(mov)
    else:
        print(-1)
 
if __name__ == "__main__":
    main()