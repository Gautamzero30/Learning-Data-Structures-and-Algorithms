
def shellsort(a,n):
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = a[i]
            j = i
            while( j>= gap and a[j - gap] > temp):
               a[j]=a[j-gap]
               j = j- gap
            a[j]=temp
        gap //=2  


a=[]
n = int(input("enter the numbers of elements to be sorted "))
for i in range(n):
    p = int(input(f"enter the {i + 1} element : "))
    a.append(p)       
shellsort(a,n) 
print(f"the sorted list  is " ,a)   
          