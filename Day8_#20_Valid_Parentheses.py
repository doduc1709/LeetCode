class Solution:
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in pairs:
                # char là ngoặc đóng
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                # char là ngoặc mở
                stack.append(char)
        
        return not stack # điền nốt điều kiện cuối