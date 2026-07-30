import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    for _ in range(t):
        s=input().strip()
        i=0
        j=len(s)-1
        while i<j:
            if s[i] == '1' and s[j] == '1':
                break
            if s[i] != '1':
                i += 1
            if s[j] != '1':
                j -= 1
        ans=0
        while i<j:
            if s[i] == '0':
                ans += 1
            i += 1
        print(ans)
 
if __name__ == "__main__":
    main()