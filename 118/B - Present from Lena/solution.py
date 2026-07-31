import sys
 
input = sys.stdin.readline
 
def main():
    t = int(input())
 
    for i in range(t + 1):
        print(" " * (2 * (t - i)), end="")
 
        j = 0
        while j <= i:
            if j == i and i == 0:
                print(j, end="")
            else:
                print(j, end=" ")
            j += 1
 
        j -= 2
 
        while j >= 0:
            if j == 0:
                print(j, end="")
            else:
                print(j, end=" ")
            j -= 1
 
        print()
 
    for i in range(t - 1, -1, -1):
        print(" " * (2 * (t - i)), end="")
 
        j = 0
        while j <= i:
            if j == i and i == 0:
                print(j, end="")
            else:
                print(j, end=" ")
            j += 1
 
        j -= 2
 
        while j >= 0:
            if j == 0:
                print(j, end="")
            else:
                print(j, end=" ")
            j -= 1
 
        print()
 
if __name__ == "__main__":
    main()