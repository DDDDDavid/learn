# leetcode刷题记录
## 6. Z 字形变换
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
```
P   A   H   N
A P L S I I G
Y   I   R
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

`string convert(string s, int numRows);`

```python
#按行读取字母，上边和下边则换方向
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)
```
## 7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
```python
class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        INTMAX10 = 214748364
        INTMIN10 = -214748364
        while x:
            pop = x % 10 if x > 0 else x % -10
            x = x // 10 if x >0 else int(x/10)
            if ans > INTMAX10 or (ans == INTMAX10 and pop > 7):
                return 0
            if ans < INTMIN10 or (ans == INTMIN10 and pop < -8):
                return 0
            temp = ans * 10 + pop
            ans = temp
        return ans
```