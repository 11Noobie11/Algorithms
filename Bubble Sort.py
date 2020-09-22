#Bubble sort

def bubblesort(lst):
    n=len(lst)
    for i in range(n-1):
        for j in range(n-1):
            if lst[j+1]<lst[j]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    print(lst)

lst=eval(input("Enter the list:"))
bubblesort(lst)
