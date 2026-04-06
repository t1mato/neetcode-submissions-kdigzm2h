class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)

        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1

        sorted_values = sorted(res.items(), key=lambda item: item[1], reverse=True)

        top_two_items = sorted_values[:k]

        top_two_values = [item[0] for item in top_two_items]

        return top_two_values