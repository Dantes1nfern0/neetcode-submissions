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
                print(stack)
            else:
                if stack == []:
                    return False
                elif stack[-1] == p_dictionary[x]:
                    stack.pop()
                    print(stack)
                else:
                    print(stack)
                    return False
        return stack == []