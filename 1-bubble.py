# function for bubble sort
def bubble(ar):
    n = len(ar)

    # run loop till length of list
    for i in range(n):

        # traverse the array from in range of n-i-1 
        for j in range(n-i-1):

            # if condition is true swap values
            if ar[j]>ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j] 
    

# declaring a list
ar = [1,5,3,4,8,7]

# print list elemnts before soarting
print("Unsorted elemnts:",ar)

# call the bubble sort function 
bubble(ar)

# print sorted list elements
print("Sorted Elements:")
for i in range(len(ar)):
    print(ar[i],end=' ')