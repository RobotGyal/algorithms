def random_ints(count=20, min=1, max=50):
    import random
    return [random.randint(min, max) for _ in range(count)]

def is_sorted(items):
    for i in range(len(items) - 1):
      if items[i] > items[i + 1]:
        return False
    return True



# Merge Algorithm
def merge(start, end):
  mid = (start + end) //2
  merge(start, mid) #split into first half
  merge(mid+1, end) # split into second half
  merge_sort(A) #merge together after reach base case


# Does comparisons and sorts
def merge_sort(A):
  if len(A) > 1:
    mid = len(A) //2

    #Split
    L = A[:mid] # create array of left half elements
    R = A[mid:] # create an array of right half elements

    #Sort
    merge_sort(L)
    merge_sort(R)

    #Traverse
    i= j= k = 0

    #Compare
    while i < len(L) and j < len(R): #move through 2 arrays
      if L[i] < R[j]:    #if left element smaller
        A[k] = L[i]    #add left to array
        i+=1    #move one index on left array
      else:
        A[k] = R[j]   #add right to array
        j+=1    #move one index in right array
      k+=1

    # Extra elements in left array
    while i < len(L):
      A[k] = L[i]
      i+=1
      k+=1
    
    # Extra elements in right array
    while j < len(R):
      A[k] = R[j]
      j+=1
      k+=1


def partition(items, low, high):
  pivot = items[high] #last element pivot
  i = low -1
  #move items to left if smaller and right if bigger
  for j in range(low, high):
    if items[j] <= pivot:
      i+=1
      items[i], items[j] = items[j], items[i] # swap

  items[i+1], items[high] = items[high], items[i+1] #swap second to last with the end
  return i+1


def quick_sort(items, low=None, high=None):
  if low < high:
    part = partition(items, low, high) #move all low items to the left

    quick_sort(items, low, part - 1) #perform on left side
    quick_sort(items, part + 1, high) #perform on right side 