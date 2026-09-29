class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '*', '-', '/']
        nums = []
        for token in tokens:
            if token in operators:
                val1, val2 = nums.pop(), nums.pop()
                match token:
                    case '+':
                        nums.append(val2 + val1)
                    case '*':
                        nums.append(val2 * val1)
                    case '-':
                        nums.append(val2 - val1)
                    case '/':
                        nums.append(int(val2 / val1))
            else:
                nums.append(int(token))
        return nums[0]