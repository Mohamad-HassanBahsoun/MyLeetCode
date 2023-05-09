class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        holder = ""
        s = min(strs,key=len)
        index = 0
        
        if(s == ""):
            return ""
        elif(len(strs) == 1):
            return strs[0]
        elif(len(s) == 1 and len(strs) == 1):
            return s

        for i in s:
            letter = i
            for word in strs:
                print(word[index],"========")
                if(word[index] != letter):
                    if(len(holder) >0):
                        return holder
                    else:
                        return ""
            index +=1
            holder += letter
        return holder