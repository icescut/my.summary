# Length Of Last Word

## 题目
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
If the last word does not exist, return 0.

**Note:** A word is defined as a character sequence consists of non-space characters only.

**Example:**

```
Input: "Hello World"
Output: 5
```

## 解一

1. 如果字符串长度为0，返回0。
2. 从后往前找到第一个非空字符串的位置，记为end。如果为是第一个元素，返回1；如果为无非空字符，返回0。
3. 从第一个非空字符的前一位置往前找第一个空字符。如果无空字符，返回end + 1；否则返回end - 该位置。

```python
class Solution:
    def lengthOfLastWord(self, s):
        l = len(s)
        if l == 0:
            return 0
        
        i = l - 1
        while i >= 0:
            if s[i] != ' ':
                break
            i -= 1
        if i == 0:
            return 1
        if i == -1:
            return 0
        end = i
        i -= 1
        while i >= 0:
            if s[i] == ' ':
                break
            i -= 1
        if i == -1:
            return end + 1
        else:
            return end - i
```