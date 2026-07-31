import sys
 
input = sys.stdin.readline
 
def main():
    k = int(input())
    a=input().strip()
    freq={}
    for i in a:
        freq[i]=freq.get(i,0)+1
    for i in freq.values():
        if i%k!=0:
            print(-1)
            return
    base=""
    for ch,count in freq.items():
        base+=ch*(count//k)
    print(base*k)
 
if __name__ == "__main__":
    main()