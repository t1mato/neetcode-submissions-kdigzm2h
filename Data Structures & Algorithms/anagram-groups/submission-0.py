class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            sorted_word = sorted(s)

            res[tuple(sorted_word)].append(s)

        return list(res.values())




        