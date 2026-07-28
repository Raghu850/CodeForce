import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
    ans=0
    for _ in range(t):
        a=input().strip()
        if a=="Tetrahedron":
            ans+=4
        elif a=="Cube":
            ans+=6
        elif a=="Octahedron":
            ans+=8
        elif a=="Dodecahedron":
            ans+=12
        else:
            ans+=20
    print(ans)
 
if __name__ == "__main__":
    main()