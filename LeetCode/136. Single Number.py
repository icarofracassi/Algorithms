from typing import List

#At first i thought the list must be ordered to the logic i was in mind to work, 
#but it doesn't made sense to an easy problem to have to sort and do some logic afterwards, 
#so i brainstormed another ideas and came out with the XOR approach and came to this

#Developed at 23:59 26th July 2024
#Using 1 hint from leetcode.
#took around 30min trying multiple ideas and debugging them before trying the XOR method
#first time i ran into a class and understood how leetcode handles inputs and outputs (as a function and return, and not printing on screen as seen on code marathons)
#thanks :)

#by iff

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            
        resultado = 0

        for i in nums:
            resultado ^= i
            
        return resultado


solution = Solution()
nums = [2,2,1]
print(nums)
print(solution.singleNumber(nums))  # Output: [1]

nums = [4,1,2,1,2]
print(nums)
print(solution.singleNumber(nums))  # Output: [4]

nums = [1]
print(nums)
print(solution.singleNumber(nums))  # Output: [1]


