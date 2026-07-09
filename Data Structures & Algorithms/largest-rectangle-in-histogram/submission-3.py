class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Monotonic stack to store indices
        max_area = 0  # Initialize max area
        
        # Add a sentinel at the end to ensure all bars are processed
        heights.append(0)
        
        for i, h in enumerate(heights):
            # Process bars until the current bar is taller than the bar at the top of the stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]  # Get the height of the popped bar
                width = i if not stack else i - stack[-1] - 1  # Calculate width
                max_area = max(max_area, height * width)  # Update max area
            stack.append(i)  # Push current bar index onto the stack
        
        return max_area