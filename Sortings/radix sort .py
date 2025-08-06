

def radix(a):    
    max_num= max(a)
    val =1
    while max_num//val >0:
        radix_sort(a,val,n)
        print(f"the sorted elements are : " ,a)
        val = val *10
  
def radix_sort(a,val,n):
    output = [0]*n
    count = [0]*10
    for i in range(n):
        index = (a[i]//val)%10
        count[index]+=1 

    for i in range(1,10):
        count[i] = count[i] + count[i-1]

    i = n-1
    while i >=0:
        index = (a[i]//val)%10
        output[count[index]-1] = a[i]
        count[index]-=1
        i-=1
    for i in range(n):
        a[i] = output[i]


    

a=[]
n=int(input("enter the no of elements to be sorted : "))
for i in range(n):
    p = int(input(f"enter the {i + 1} element : "))
    a.append(p)
radix(a)

