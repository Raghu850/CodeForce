import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    a=input().strip()
    i=1
    j=0
    ans=""
    while j<t:
        ans+=a[j]
        j+=i
        i+=1
    print(ans)
 
if __name__ == "__main__":
    main()