class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize the res array with 0
        res = [0] * len(temperatures)
        # stack to store monotonic decreasing stack
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res


