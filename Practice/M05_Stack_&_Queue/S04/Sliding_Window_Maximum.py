# 239. Sliding Window Maximum
def maxSlidingWindow(nums :list[int], k:int) -> list[int]:
    res = []
    for i in range(0,len(nums)-k+1):
        res.append(max(nums[i:i+k]))
    return res
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums,k))