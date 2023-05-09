class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        opened = ['(','{','[']
        closed = [')','}',']']

        stack = []

        for i in s:
            if i in opened:
                stack.append(i)
            else:
                if(len(stack) >0):
                    if(stack[-1] == opened[closed.index(i)]):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if(len(stack) >0):
            return False
        else:
            return True