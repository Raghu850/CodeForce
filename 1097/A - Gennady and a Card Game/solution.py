import sys
 
input = sys.stdin.readline
 
def main():
    t = input()
    a=list(input().split())
    for i in range(len(a)):
        if a[i][0]==t[0] or a[i][1]==t[1]:
            print("YES")
            break
    else:
        print("NO")
 
if __name__ == "__main__":
    main()