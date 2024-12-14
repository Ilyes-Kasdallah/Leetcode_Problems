class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mnl=min(len(word1),len(word2))
        res=""
        for i in range(mnl):
            res+=word1[i]
            res+=word2[i]
        if len(word1)==mnl:
            res+=word2[mnl:]
        else:
            res+=word1[mnl:]

        return res