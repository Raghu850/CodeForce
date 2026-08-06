import sys
 
input = sys.stdin.readline
 
def main():
    s = input().strip()
    
    upper = sum(c.isupper() for c in s)
    
    if upper == len(s) or (s[0].islower() and upper == len(s) - 1):
        print(s.swapcase())
    else:
        print(s)
if __name__ == "__main__":
    main()