#To Find The Maximum in a array
import array 
arr = []
n = int(input("Enter the size of array: "))
if  n == 0:
    print("It is an Empty array ")
else:
    for i in range(n):
        element = int(input("Enter the element: "))
        arr.append(element)
    print(arr)
    if n == 1:
        print("The maximum value is: ",arr[10])
    else:
        max = arr[0]
        # for i in range(n):
        for num in arr:
            if max < num:
                max = num
        print("The maximum value in array is :",max)