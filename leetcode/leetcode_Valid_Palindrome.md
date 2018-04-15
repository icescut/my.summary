
# Valid Palindrome

## 题目
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.  
**For example,**

"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

**Note:**

Have you consider that the string might be empty? This is a good question to ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.

## 解一

1. 设置left指向字符串最左边元素，right指向最右边元素。

2. 循环直到left和right相遇

    * 如果left指向的元素非字母数字则右移一位，如果right指向的元素非字母数字则左移一位。  
    * 如果left和right指向的元素转换为小写字母后不相的，返回False。  
    * left右移一位，right左移一位。  

3. 如果循环结束都没发现不同，返回True。

4. 如果字符串长度为0或1，返回True。

```python
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 0 or l == 1:
            return True
        
        left = 0
        right = l - 1
        while left < right:
            x = s[left]
            y = s[right]
            if not x.isalnum():
                left += 1
                if not y.isalnum():
                    right -= 1
                continue
            elif not y.isalnum():
                right -= 1
                if not x.isalnum():
                    left += 1
                continue
            elif x.lower() != y.lower():
                return False
            else:
                left += 1
                right -= 1
        return True
```