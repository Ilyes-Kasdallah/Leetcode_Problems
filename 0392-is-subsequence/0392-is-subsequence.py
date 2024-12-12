class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sm=0
        i=0
        if len(s)==0:
                return True
        for j in range(len(t)):
            if t[j]==s[i]:
                i+=1
            if i >= len(s):
                return True
        return False    
            
        