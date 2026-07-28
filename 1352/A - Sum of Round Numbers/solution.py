import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        a=int(input())
        ans=[]
        i=0
        while a>0:
           n=a%10
           if n!=0:
                   ans.append(n*(10**i))
           i+=1
           a//=10
        ans.reverse()
        print(len(ans))
        print(*ans)
 
if __name__ == "__main__":
    main()