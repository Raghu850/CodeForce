import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    c=0
    m=0
    for i in range(t):
       exit,enter=map(int,input().split())
       c-=exit
       c+=enter
       m=max(m,c)
    print(m) 
 
if __name__ == "__main__":
    main()