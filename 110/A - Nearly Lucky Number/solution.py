import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    count=0
    while t>0:
        a=t%10
        if a==4 or a==7:
            count+=1
        t//=10
    real=count
    while count>0:
        a=count%10
        if a!=4 and a!=7:
            print("NO")
            break
        count//=10
    else:
        if real==0:
            print("NO")
        else:
            print("YES")
 
if __name__ == "__main__":
    main()