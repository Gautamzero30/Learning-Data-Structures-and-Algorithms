def mergesort(a,l,r):
    if (l<r):
        m= (l+r) // 2
        mergesort(a,l,m)
        mergesort(a,m+1,r)
        merge(a,l,m,r)
def merge(a,l,m,r):
    b=[]
    i = l 
    j =m +1
    
    while (i<=m and j<= r):
        if a[i] < a[j]:

            b.append(a[i])
            
            i+=1
        else :  
            b.append(a[j])
            j+=1 
    while i <= m:
        b.append(a[i])
        i+=1
    while j<=  r:
        b.append(a[j]) 
        j+=1 
        
    for k in range(len(b)):
        a[l+k]=b[k]
        
a = []
n = int(input("enter the numbers you want to sort : "))
for i in range(n):
    p = int(input(f"enter {i+1} number : "))
    a.append(p)
    l=0
    r= len(a)

mergesort(a,0,len(a)-1) 
  
print("the sorted list is  : ", a )
    

           

