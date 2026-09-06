nums = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        seen = {}  # dict lưu {giá_trị: chỉ_số} đã duyệt qua

        for i in range(len(nums)):
            complement = target - nums[i]   # số còn thiếu cần tìm
            
            if complement in seen:
                return [seen[complement], i]   # trả về chỉ số của complement và chỉ số i
            
            seen[nums[i]] = i   # lưu giá trị hiện tại vào dict

print(Solution().twoSum(nums, target))