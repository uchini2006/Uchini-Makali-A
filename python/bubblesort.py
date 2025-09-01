def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(1,n-i):
            if arr[j]<arr[j-1]:
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
arr=[12,60,35,10,5]
bubble_sort(arr)
print(arr)

    