class Solution(object):
    def isValid(self,s):
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if (top=='(' and i!=')') or (top=='{' and i!='}') or (top=='[' and i!=']'):
                    return False
        return not stack