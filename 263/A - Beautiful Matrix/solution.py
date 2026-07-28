import sys
 
input = sys.stdin.readline
 
def main():
    mat=[]
    for _ in range(5):
        mat.append(list(map(int,input().split())))
    for i in range(5):
        for j in range(5):
            if mat[i][j]==1:
                print(abs(i-2)+abs(j-2))
if __name__ == "__main__":
    main()