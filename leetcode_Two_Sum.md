# Leetcode Two Sum
## 题目
Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

You may assume that each input would have **exactly** one solution, and you may not use the same element twice.

**Example:**
>Given nums = [2, 7, 11, 15], target = 9,
>
>Because nums[0] + nums[1] = 2 + 7 = 9,
>return [0, 1].

## 解一
最直觉的想法是，从左往右，先取第一个元素，然后在剩余的元素中找是否有另一个元素使得两者之和等于`target`。如果没有，取再取第二个元素，重复前面的步骤，直到找到。可是效率为O(n<sup>2</sup>)。
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in nums:
            b = target - a
            ix_a = nums.index(a)
            if b in nums[ix_a + 1:]:
                return [ix_a, nums.index(b, ix_a + 1)]
```

## 解二
1. 假设读取的列表中的元素值为`a`，并且有一个`b`使得`a + b = target`。
2. 准备一个字典，当读取一个列表中的元素`a`，则以`b`作为key，索引作为value放入字典中。
3. 每读取一个元素`a`，则判断其是否在字典中，如果在，则返回字典的值及当前索引；如果不在，执行第二步。  

这个解法的关键在于字典是用`hash`实现的，想找字典仅需O(1)，所以整个方法的效率为O(n)。

```python
class Solution:
    def twoSum(self, nums, target):
        num_ix = {}
        for i, a in enumerate(nums):
            if a in num_ix:
                return [num_ix[a], i]
            else:
                num_ix[target - a] = i
```

优化：经实践不使用`enumerate`将会有些许效率提升。
```python
class Solution:
    def twoSum(self, nums, target):
        num_ix = {}
        for i in range(len(nums)):
            if nums[i] in num_ix:
                return [num_ix[nums[i]], i]
            else:
                num_ix[target - nums[i]] = i
```
