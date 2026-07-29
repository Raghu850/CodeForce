import sys
 
input = sys.stdin.readline
 
def main():
    t=set(input().strip())
    print("CHAT WITH HER!" if len(t)%2==0 else "IGNORE HIM!")
 
if __name__ == "__main__":
    main()