#496.Next Greater Element 1
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        stack = []
        d = {}
        for i in range(len(nums2)-1,-1,-1):
            cur = nums2[i]
            while stack and stack[-1] <= cur:
                stack.pop()
            if stack:
                d[cur] = stack[-1]
            else:
                d[cur] = -1
            stack.append(cur)
        res = []
        for ele in nums1:
            res.append(d[ele])
        return res

