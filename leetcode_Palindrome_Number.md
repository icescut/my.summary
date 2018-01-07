# Leetcode Palindrome Number
## 题目
Determine whether an integer is a palindrome. Do this without extra space.

## 解一
将x和y(一开始为空列表)想象为一个列表：  
1. 从x的右边移出一个数字
2. 将该数字移到y的最右边
3. 重得这个过程，直到`y >= x`。
4. 如果`x == y`或者x等于y的前len(x)位则为回文。

奇数：
> x = 12321 y = 0  
> x = 1232 y = 1  
> x = 123 y = 12  
> x = 12 y = 123  

偶数：
> x = 1221 y = 0    
> x = 122 y = 1  
> x = 12 y = 12  

```python
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x = int(x / 10)

        return x == y or x == int(y / 10)
```
