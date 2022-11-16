def check_sorted_by_recursion(arr):
    if len(arr) == 1:
        return True
    return arr[0] <= arr[1] and check_sorted_by_recursion(arr[1:])


print(check_sorted_by_recursion([1,2,3,4,5,6,7,8]))
print(check_sorted_by_recursion([1,4,2,5,3,2,5,3]))