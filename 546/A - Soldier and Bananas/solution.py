import sys
 
input = sys.stdin.readline
 
def main():
    k,n,w = map(int,input().split())
    ans=k*(w*(w+1)//2)-n
    print(ans if ans>0 else 0)
 
if __name__ == "__main__":
    main()