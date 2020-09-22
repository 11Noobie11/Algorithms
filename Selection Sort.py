#Selection Sort

def selectionsort(lst):
    n=len(lst)
    for i in range(n-1):
        min=i
        for j in range(i,n):
            if lst[j]<lst[min]:
                min=j
        temp=lst[i]
        lst[i]=lst[min]
        lst[min]=temp
    print(lst)

lst=eval(input("Enter the list:"))
selectionsort(lst)
