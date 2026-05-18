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
                    return False
        return stack == []


        # Takes in a string
        # iterates through the string, into a stack
        # stack adds open parentheses into stack

        # Case 1
        # iteration has a closed brackets, goes to top of...
        # ...stack and key pair does not match
        # returns False

        # Case 2
        # iteration is complete and the stack is NOT empty
        # returns False

        # Case 3
        # iteration has a closed bracket, goes to top of...
        # ...stack and key pair DOES match
        # removes the open bracket from the top of the stack

        # Case 4
        # iteration is complete, and check confirms that...
        # ...stack is empty
        # return True