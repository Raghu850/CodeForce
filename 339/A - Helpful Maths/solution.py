import sys
 
input = sys.stdin.readline
 
def main():
    t = list(map(int,input().split('+')))
    def quicksort(t,low,high):
        if low<high:
            p=partition(t,low,high)
            quicksort(t,low,p-1)
            quicksort(t,p+1,high)
    def partition(t,low,high):
        pivot=t[low]
        i=low
        j=high
        while i<j:
            while i<=high and t[i]<=pivot:
                i+=1
            while j>low and t[j]>pivot:
                j-=1
            if i<j: t[i],t[j]=t[j],t[i]
        t[low],t[j]=t[j],t[low]
        return j
    quicksort(t,0,len(t)-1)
    print('+'.join(str(i) for i in t))
if __name__ == "__main__":
    main()