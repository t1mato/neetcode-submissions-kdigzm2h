class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_msg = ""
        encoded_list = []
        for i in range(len(strs)):
            curr_len = len(strs[i])
            encoded_list.extend([str(curr_len), "#", strs[i]])
        encoded_msg = "".join(encoded_list)
        return encoded_msg

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decoded_str.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return decoded_str