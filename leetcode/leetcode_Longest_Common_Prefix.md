
# Longest Common Prefix

## 题目
Write a function to find the longest common prefix string amongst an array of strings.

## 解一

1. 如果字符串列表没有元素，返回空字符串。
2. 如果字符串列表只有一个元素，返回改元素。
3. 获取字符串列表中最短的元素的长度minl，如果为零返回空字符串。
4. 从左到右比较字符串列表中所有元素相同位置的字符是否相等，如果不相等，返回已比较的相等的字符串。

```python
class Solution:
    def longestCommonPrefix(self, strs):
        la = len(strs)
        if la == 0:
            return ''
        if la == 1:
            return strs[0]
        
        minl = len(strs[0])
        if minl != 0:
            for s in strs:
                if len(s) < minl:
                    minl = len(s)
                    if minl == 0:
                        break
        else:
            return ''
        if minl == 0:
            return ''
        for i in range(minl):
            c = strs[0][i]
            for s in strs:
                if c != s[i]:
                    return s[0:i]
        return strs[0][0:minl]
```