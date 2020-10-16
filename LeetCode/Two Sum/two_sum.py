class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i,current_value in enumerate(nums):
            diff = target - current_value
            second_index= values.get(diff)
            if   second_index is not None:
                return second_index,i
            else:
                values[current_value] =i    
