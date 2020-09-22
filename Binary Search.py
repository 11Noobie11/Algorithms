#Binary Search

def binary_search(l,item,beg,end):
     if end<beg:
          return
     else:
          mid=(beg+end)//2
          if l[mid]>item:
               return binary_search(l,item,beg,mid-1)
          elif l[mid]<item:
               return binary_search(l,item,mid+1,end)
          elif l[mid]==item:
               print("Found")
          else:
               print("Not Found")

l=eval(input("Enter the list:"))
l.sort()
item=int(input("Enter the item:"))
beg=0
end=len(l)
print(binary_search(l,item,beg,end))
