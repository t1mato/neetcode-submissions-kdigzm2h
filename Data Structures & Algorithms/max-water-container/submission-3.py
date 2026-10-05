class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 2:
            return min(heights[0], heights[1])
        
        # formula to find amount of water is min(heights[l], heights[r]) * (r - l)
        # if heights[l] < heights[l + 1], l += 1
        # if heights[r] < heights[r - 1], r-= 1

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            res = max(res, min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res