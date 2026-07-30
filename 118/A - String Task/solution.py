import sys
 
input = sys.stdin.readline
 
def main():
    t = input().strip().lower()
    a=set("aoyeui")
    ans=""
    for i in t:
       if i not in a:
           ans+="."+i
    print(ans)
if __name__ == "__main__":
    main()