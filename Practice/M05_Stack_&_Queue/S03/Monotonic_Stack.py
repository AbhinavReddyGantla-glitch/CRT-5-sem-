def next_greater(arr):
    n = len(arr)
    result = [-1]  * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1] < arr[i]]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    return result

arr = [2,1,5,3,4]
print(next_greater(arr))

#496. Next Greater Element I
def next_greater_element(nums1, nums2):
    stack = []
    next_greater_map = {}
    
    