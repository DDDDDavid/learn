# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 00:46:33 2021

@author: David
"""
#1、两数之和
##暴力法
class Solution:
    def twoSum(self, nums: list[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]       
        return []

##哈希表    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []


#2、两数相加
#用原来的链表
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       if not l1:
            return l2
        if l2:
            l1.val=(l1.val+l2.val)
        if l1.val>=10:
            l1.val=l1.val%10
            if l1.next !=None:
                l1.next.val+=1
            else :
                l1.next=ListNode(1)
        if l2:
            l1.next=self.addTwoNumbers(l1.next,l2.next)
        else:
            l1.next=self.addTwoNumbers(l1.next,l2)
        return l1
    
#新增一个链表    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        count = 0
        ret = ListNode()
        tmp = ret
        while l1 or l2 or count:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if count:
                num += count
                count -= 1
            count, num = divmod(num, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return ret.next
    
#3、无重复字符的最长子串
#哈希map遍历
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k, res, c_dict =  -1, 0, {}
        for i ,c in enumerate(s):
            if c in c_dict and c_dict[c] > k:
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i-k)
        return res
                    

        
        

