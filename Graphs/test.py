class Solution:
    def bsearch(self, nums, l, r, target):
        if l>r:
             return -1
             
        mid = (l+r)//2
        if nums[mid] == target:
             return mid
        elif nums[mid] > target:
            if nums[l] < target:
                r = mid-1
                return self.bsearch(nums, l, r, target)
            elif nums[l] > target:
                 l = mid+1
                 return self.bsearch(nums, l, r, target)
            else:
                 return l
        else:
            if nums[r] > target:
                l = mid + 1
                return self.bsearch(nums, l, r, target)

    def search(self, nums: list[int], target: int) -> int:
            if len(nums) == 1:
                return 0 if nums[0] == target else -1
            else:
                l, r = 0, len(nums)-1
                return self.bsearch(nums, l, r, target)


obj = Solution()
nums = [4,5,6,7,0,1,2]
target = 3

print(obj.search(nums, target))