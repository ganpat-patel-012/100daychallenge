#function for selection sort
def selection(ar):
    n = len(ar)
    for i in range(len(ar)):
        min= i
        for j in range(i+1, len(ar)):
            if ar[min] > ar[j]:
                min = j
        #swap
        ar[i], ar[min] = ar[min], ar[i]



ar = [1,5,3,4,8,7,6]

# print list elemnts before soarting
print("Unsorted elemnts:",ar)

# call the bubble sort function 
selection(ar)

for i in range(len(ar)):
    print(ar[i], end=" ")