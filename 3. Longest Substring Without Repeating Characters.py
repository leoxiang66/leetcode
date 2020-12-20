'''
Given a string s, find the length of the longest substring without repeating characters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)  ==0:  return  0
        result = 1
        length = len(s)
        for i in range(length):
            diff_count = 1

            for j in range(i+1,length):
                if s[j] not  in  s[i:j]:
                    diff_count +=1
                    if diff_count > result: result = diff_count
                    #print(s[j],s[i:j])
                else:
                    if diff_count > result: result  =diff_count
                    break


        return result

#Solution().lengthOfLongestSubstring("pwwkew")