# Plus One

## 题目
Given a **non-empty** array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:**

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example 2:**

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

## 解一

1. 原地处理输入得到输出。
2. 先将最右元素加一，如果结果小于10，将结果赋最右元素，返回digits；否则，最右元素赋0，进位为1，处理其左边元素。
3. 倒数第二元素加上进位，如果结果小于10，将结果赋最右元素，返回digits；否则，最右元素赋0，进位为1，处理其左边元素。如此类推。
4. 直到break或处理完第一个元素。如果处理完第一个元素未结束，在列表前插入一个1。返回digits。

```python
class Solution:
    def plusOne(self, digits):
        i = len(digits) - 1
        
        u = 0
        digits[i] += 1
        
        while i >= 0:
            n = digits[i] + u
            if n < 10:
                digits[i] = n
                break
            else:
                u = 1
                digits[i] = 0
            i -= 1
        if i == -1:
            digits.insert(0, 1)
        return digits
```