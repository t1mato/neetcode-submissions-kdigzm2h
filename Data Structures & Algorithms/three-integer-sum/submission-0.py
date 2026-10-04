class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:          # smallest value positive -> no solution possible
                break
            if i > 0 and nums[i] == nums[i - 1]:   # skip duplicate anchors
                continue

            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:   # skip duplicate j
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:   # skip duplicate k
                        k -= 1
        return res