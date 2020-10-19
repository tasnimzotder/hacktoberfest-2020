#Python program for implementation of Heap Sort
#A max heap is formed when all the parent node are greater than corresponding child nodes.

def heapify(arr, n, i):
   largest = i # largest value
   l = 2 * i + 1 # left child
   r = 2 * i + 2 # right child
   # if left child is greater than parent node
   if l < n and arr[i] < arr[l]:
      largest = l
   # if right child is greater than parent node
   if r < n and arr[largest] < arr[r]:
      largest = r

   if largest != i:
      arr[i],arr[largest] = arr[largest],arr[i] # swap the largest elemt with parent node
      heapify(arr, n, largest)

# heap sort function  
def heapSort(arr):
   n = len(arr)
   # maxheap
   for i in range(n, -1, -1):
      heapify(arr, n, i)
   # element extraction
   for i in range(n-1, 0, -1):
      arr[i], arr[0] = arr[0], arr[i] # swap
      heapify(arr, i, 0)

# Array to be sorted
arr = [18,8,15,30,25,12,22,11]

heapSort(arr)
n = len(arr)

print ("Sorted array is")
for i in range(n):
   print (arr[i],end=" ")