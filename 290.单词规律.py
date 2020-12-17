class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        list = s.split(' ')

        if len(list) != len(pattern):
            return False
        else:
            for i in range(len(pattern)):
                pivot = pattern[i]
                for j in range(i, len(pattern)):
                    if pivot == pattern[j]:
                        if list[i] != list[j]: return False
                    else:
                        if list[i] == list[j]: return False

            return True