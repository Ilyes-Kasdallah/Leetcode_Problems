class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        mx = 0

        while r > l:
            area = (r - l) * min(height[l], height[r])
            mx = max(mx, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return mx

                
            
        