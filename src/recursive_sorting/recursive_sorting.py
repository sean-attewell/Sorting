# TO-DO: complete the helper function below to merge 2 sorted arrays
# handles merging sorted pieces back together
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = 0 # add one to counter each time a value is placed from this arr
    b = 0 # these act as index to keep track of where you are instead of pop()
    # also a or b are equal to their respective array length, then that arr is done 

    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # element in arrA smaler
            merged_arr[i] = arrA[a]
            a += 1          
        else: # element in arrB smaler
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# elements = 6
# merged_arr = [0] * elements
# print(merged_arr) <-- [0, 0, 0, 0, 0, 0]


# TO-DO: implement the Merge Sort function below USING RECURSION
# handles dividing the array (or subarray) in half
def merge_sort( arr ):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        # print("left" + str(left))
        right = merge_sort(arr[mid:])
        # print("right" + str(right))
        arr = merge(left, right)
        # print(arr)

    return arr

arr = [1, 23, 3, 4, 4, 48, 7]
arr2 = merge_sort(arr)
print(arr2)
# arr = [1, 2, 3, 4, 5, 6, 7]
# mid = len(arr) // 2
# left = arr[:mid]
# right = arr[mid:]
# print(mid) <-- 3
# print(left) <-- [1, 2, 3]
# print(right) <-- [4, 5, 6, 7]

# print(mid) 
# print(left) 
# print(right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

# http://www.pythontutor.com/visualize.html#mode=edit