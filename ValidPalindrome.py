class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = (re.sub(r'\W+', '', s)).lower()
        i = 0
        s1= ''.join(s1.split("_"))
        print(s1,len(s1))
        j = len(s1)-1
        print(j)

        if (s1 == ""):
            return True

        for i in range(0,len(s1)):
            if(s1[i] != s1[j]):
                return False
            i+=1
            j-=1
            print("Hello")
            print(i,j)
            if(i >= j):
                return True