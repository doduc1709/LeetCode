def max_sum_subarray(nums, k):
    # Bước 1: tính tổng của cửa sổ đầu tiên (k phần tử đầu tiên)
    window_sum = sum(nums[0:k])
    max_sum = window_sum
    
    # Bước 2: trượt cửa sổ từ vị trí k đến hết mảng
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]   # trừ phần tử ra, cộng phần tử vào
        max_sum = max(max_sum, window_sum)
    
    return max_sum

print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))

#Bài tập áp dụng 
#643: Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[0:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        return max_sum / k 