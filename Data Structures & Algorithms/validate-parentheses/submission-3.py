class Solution:
    def isValid(self, s: str) -> bool:
        seen = []

        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                seen.append(bracket)
            elif bracket == ')':
                if seen and seen[-1] == '(':
                    seen.pop()
                else:
                    return False
            elif bracket == '}':
                if seen and seen[-1] == '{':
                    seen.pop()
                else:
                    return False
            elif bracket == ']':
                if seen and seen[-1] == '[':
                    seen.pop()
                else:
                    return False
        return len(seen) == 0
