class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions and speeds, and sort by position in descending order
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []  # To store times of fleets
        
        for pos, spd in cars:
            time_to_reach = (target - pos) / spd
            # If the stack is empty or the current car cannot catch the last fleet
            if not stack or time_to_reach > stack[-1]:
                stack.append(time_to_reach)  # Start a new fleet
        
        return len(stack)