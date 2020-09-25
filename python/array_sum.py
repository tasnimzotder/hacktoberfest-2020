# Sum of the elements of an array

def sum_arr(arr):
    sum=0
    for x in arr:
        sum+=x
    
    return sum 
        


arr = [1, 9, 2, 0]
print('Sum of the array: {}'.format(sum_arr(arr)))
