a = []
n= int(input("enter the number of nmber you want to enter : "))
for i in range(n): 
    p = int(input(f"enter the {i+1} elements : "))
    a.append(p)
for i in range(0,n):
    temp = a[i]
    j = i-1
    while j >= 0 and temp < a[j]:
        a[j+1]= a[j]
        j=j-1
    a[j+1] = temp
print("the sorted list is ",a)        
