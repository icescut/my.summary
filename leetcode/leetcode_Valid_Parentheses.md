# Valid Parentheses
## 题目
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

## 解一
1. 准备一个栈`q  = []`
2. 从左往右遍历字符串，如果是一对括号的左边，则入栈；否则与栈顶元素比较看是否一对，如果是一对则出栈，如果不是，返回`False `。
3. 遍历完后，判断栈中是否还有元素，如有返回`False`
4. 另外在一开始判断字符串长度是否为奇数，如是返回`False`。
```python
class Solution:
    left = ('(', '[', '{')
    m = {')': '(', ']': '[', '}': '{'}
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 0 or l % 2 != 0:
            return False
        q = []
        for c in s:
            if c in Solution.left:
                q.append(c)
            else:
                if len(q) > 0:
                    if q.pop()!= Solution.m[c]:
                        return False
                else:
                    return False
        if len(q) != 0:
            return False
        return True
```