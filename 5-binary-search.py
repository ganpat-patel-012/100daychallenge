def binary(ar, x): 

    l = 0
    r = len(ar)-1

    if r >= l: 
  
        mid = l + (r - l) // 2
  
        if ar[mid] == x: 
            return mid 
          
        elif ar[mid] > x: 
            return binary(ar, l, mid-1, x) 
  
        else: 
            return binary(ar, mid + 1, r, x) 
  
    else: 
        return -1
  
ar = [1,4,2,7,9]
x = 2
  
result = binary(ar, x) 
  
if result != -1: 
    print ("Element is at index :", result) 
else: 
    print ("Element is not there in the list.") 