import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    a=list(map(int,input().split()))
    for i in range(t):
        if a[i]:
            print("HARD")
            break
    else:
        print("EASY")
if __name__ == "__main__":
    main()