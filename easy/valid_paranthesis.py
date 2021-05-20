'''

https://leetcode.com/problems/valid-parentheses/

'''


class Solution:

    ## 1. Python clear and fast Python Python Python beat 100%
    def isValid1(self, s: str) -> bool:
        dic = {'(': 1, ')': 2, '[': 3, ']': 6, '{': 5, '}': 10}
        res = []
        for one in s:
            temp = dic[one]
            if (temp % 2):
                res.append(temp)
            else:
                if (len(res) and res[-1] == temp // 2):
                    del res[-1]
                else:
                    return False
        return res == []


## 2. Python Stack Hash
    def isValid2(self, s: str) -> bool:
        stack = []
        left = set('([{')
        right = set(')]}')
        check = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in left:
                stack.append(i)
            if i in right:
                if not stack:
                    return False
                elif stack.pop() != check[i]:
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False

    ## Python solution. Pythonic and fast.

    def isValid3(self, s):
        stack = []
        match = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif not stack or match[stack.pop()] != c:
                return False
        return not stack


obj = Solution()
print(obj.isValid1('({[]})'))
