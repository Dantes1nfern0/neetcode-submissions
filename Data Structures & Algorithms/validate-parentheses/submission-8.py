class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        p_dictionary = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for x in s:
            if x == '(' or x == '[' or x == '{': 
                stack.append(x)
            else:
                if stack == []:
                    return False
                elif stack[-1] == p_dictionary[x]:
                    stack.pop()
                else:
                    return False
        return stack == []