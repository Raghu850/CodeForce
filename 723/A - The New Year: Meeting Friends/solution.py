import sys
 
input = sys.stdin.readline
 
def main():
    nums=list(map(int,input().split()))
    nums.sort()
    med=nums[1]
    print(abs(nums[0]-med)+abs(nums[2]-med))
if __name__ == "__main__":
    main()