class Solution:
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]   # trả về chỉ số dạng 1-based
            elif current_sum < target:
                left += 1  # dịch pointer nào?
            else:
                right -= 1   # dịch pointer nào?