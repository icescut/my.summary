# Implement strStr()

## 题目
Implement strStr().
Return the index of the first occurrence of needle in haystack, or **-1** if needle is not part of haystack.

**Example 1:**

> Input: haystack = "hello", needle = "ll"
> Output: 2

**Example 2:**

> Input: haystack = "aaaaa", needle = "bba"
>Output: -1

**Clarification:**

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

## 解一

1. 从左往右扫描haystack，看分片是否等于needle，如果有，返回开始的索引，如果扫描完都没有，返回-1。
2. 如果needle长度为0，返回0。
3. 如果haystack长度小于needle长度，返回-1。
4. 在haystack长度等于needle长度情况下。如果两者相等，返回0，否则返回-1。

```python
class Solution:
    def strStr(self, haystack, needle):
        lh = len(haystack)
        ln = len(needle)
        if ln == 0:
            return 0
        if lh < ln:
            return -1
        if lh == ln:
            if haystack == needle:
                return 0
            else:
                return -1
       
        for i in range(lh - ln + 1):
            if haystack[i:i + ln] == needle:
                return i
        return -1
```