class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}   # {giá_trị: chỉ_số_gần_nhất}
        
        for i in range(len(nums)):
            if nums[i] in seen:
                # đã gặp giá trị này trước đó rồi
                if i - seen[nums[i]] <= k :   # điều kiện khoảng cách <= k
                    return True
            seen[nums[i]] = i   # cập nhật vị trí gần nhất của giá trị này
        return False