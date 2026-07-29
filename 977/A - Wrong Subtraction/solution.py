import sys
 
input = sys.stdin.readline
 
def main():
    s,t = map(int,input().split())
    for _ in range(t):
        a=s%10
        if a:
            s-=1
        else:
            s//=10
    print(s)
 
if __name__ == "__main__":
    main()