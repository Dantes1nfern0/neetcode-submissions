class Solution:
    def isPalindrome(self, s: str) -> bool:
        first_array = []
        second_array = []

        for x in s:
            if x.isalnum():
                first_array.append(x.lower())
        
        for x in range(len(first_array) - 1, -1, -1):
            second_array.append(first_array[x])

        return first_array == second_array
                
        

        # isalnum()
        # Takes in a string
        # strips it of all non-alphanumeric characters and spaces
        # converts the string to all lower case
        # sorts the string backwards
        # check if the string backwards is equivalent to the...
        # ...original string.
        # If so, return True. Otherwise, return False.