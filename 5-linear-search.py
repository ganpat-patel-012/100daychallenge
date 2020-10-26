def linear(ar, x):
    n = len(ar)
    for i in range(0, n):
        if (ar[i] == x):
            return i
    return -1

ar = [1,4,2,7,9]
x = 2

result = linear(ar, x)
if(result == -1):
    print("Element is not there in the list.")
else:
    print("Element is at index :", result)