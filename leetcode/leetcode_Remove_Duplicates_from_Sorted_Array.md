# Remove Duplicates from Sorted Array
## 题目
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by ** modifying the input array in-place ** with O(1) extra memory.
** Example: **
> Given nums = [1,1,2],
> 
> Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
> It doesn't matter what you leave beyond the new length.

## 解一
1. 第一个元素占据第一个位置
2. 从左往右遍历字符串，直到找到第一个与前一个元素不同，放到第二个位置；然后依次设置第三/第四个位置，如此类推
3. 遍历完后，清空后面没重新放置元素的位置，返回长度。

```python
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0 or l == 1:
            return l
        offset = 1
        curr = nums[0]
        for n in nums:
            if n != curr:
                nums[offset] = n
                offset += 1
                curr = n
        nums[offset:] = []
        return offset
```