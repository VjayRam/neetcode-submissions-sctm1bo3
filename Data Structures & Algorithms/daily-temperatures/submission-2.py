class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize the result array with 0s
        stack = []  # Stack to keep track of indices
        
        for i in range(n):
            # While the current temperature is greater than the temperature at the index stored in the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)  # Push the current index onto the stack
        
        return result