#Reverssing an Array
arr = []
n=int(input("Enter the size of array: "))
for i in range(n):
   element=int(input("Enter the next element: "))
   arr.append(element)
print("Array before reversing: ")
print(arr)
print("After reversing the array: ")
for i in range(n//2):
    temp=arr[i]
    arr[i]=arr[n-1-i]
    arr[n-1-i]=temp
print(arr)