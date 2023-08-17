class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        hashmap = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in hashmap and len(stack) and stack[-1] == hashmap[ch]:
                stack.pop()
                continue

            stack.append(ch)
        
        if len(stack):
            return False
        
        return True
        
        
