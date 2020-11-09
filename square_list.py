# Name: Jamar Hill
# Date: 11/8/2020
# Description: Assignment 7a

"""Define square_list and it's contents as "nums." """
def square_list(nums):
    """Each item in the contents (nums) of square_list will be represented by variable "x" """
    for x in range(len(nums)):
        """Provide formula to square each variable"""
        nums[x] = nums[x] * nums[x]

""" Testing for lines of code"""
nums = [7, -3, 12, 9]
square_list(nums)
print(nums)
