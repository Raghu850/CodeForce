import sys
 
input = sys.stdin.readline
 
def main():
    l,b = map(int,input().split())
    years=0
    while l<=b:
        l=l*3
        b=b*2
        years+=1
    print(years)
if __name__ == "__main__":
    main()