class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join([char for char in s if char.isalnum()])
        pal = pal.lower()

        left = 0
        right = len(pal) - 1

        if len(pal) == 1:
            return True
            
        while right > left:
            if pal[left] == pal[right]:
                left += 1
                right -= 1
                continue
            elif pal[left] != pal[right]:
                return False
        return True

