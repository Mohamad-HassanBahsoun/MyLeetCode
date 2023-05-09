class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        end = len(str(x))-1
        if(len(str(x)) %2 == 0):
            mid = int((len(str(x))/2))
            for i in range(0,mid):
                if(str(x)[i] != str(x)[end]):
                    return False
                else:
                    end-=1
            return True
        else:
            mid = int((len(str(x))/2) +0.5)
            for i in range(0,mid):
                if(str(x)[i] != str(x)[end]):
                    return False
                else:
                    end-=1
            return True