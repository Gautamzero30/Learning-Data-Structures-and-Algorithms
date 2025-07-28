
def quickshort(a,l,r):
    if (l<r):
        p = partition(a,l,r)
        quickshort(a,l,p-1)
        quickshort(a,p+1,r)

def partition(a,l,r):
    x=l 
    y=r       
    pivot = a[l]
    while(x<y):
        while (a[x]<= pivot and x <= r):
            x+=1
        while( a[y] > pivot):
            y-=1
        if (x<y):
            a[x],a[y]=a[y],a[x]

        else:
            break
    a[l],a[y]=a[y],a[l]    
    return y

a= []
n = int(input("enter the no. of elements you want to sort"))
for i in range(n):
    p=int(input(f"enter the {i+1 } element") )
    a.append(p)

quickshort(a,0,n-1)
print("the sorted list is", a)



          
