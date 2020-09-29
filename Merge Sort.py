def merge_sort(l): 
  if len(l)>1: 
        m = len(l)//2
        left = l[:m] 
        right = l[m:] 
        left = merge_sort(left) 
        right = merge_sort(right) 
        l =[]
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                l.append(left[0]) 
                left.pop(0) 
            else: 
                l.append(right[0]) 
                right.pop(0) 
        for i in left: 
            l.append(i) 
        for i in right: 
            l.append(i) 
  return l

a = eval(input("Enter the list:")) 
print("Given list is") 
print(a)
a = merge_sort(a)  
print("Sorted list is : ") 
print(a)
