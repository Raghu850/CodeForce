import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    height=0
    level=1
    while t>=level*(level+1)//2:
        t-=level*(level+1)//2
        height+=1
        level+=1
    print(height)
 
if __name__ == "__main__":
    main()