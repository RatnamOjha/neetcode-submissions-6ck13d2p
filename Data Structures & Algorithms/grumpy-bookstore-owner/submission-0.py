class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:        
        l = 0
        n = len(customers)

        base = sum(customers[i] for i in range(n) if grumpy[i] == 0)
        current_gain = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)

        max_gain = current_gain

        for i in range(minutes, n):
            # Add new customer on the right
            if grumpy[i] == 1:
                current_gain += customers[i]
            # Remove customer on the left
            if grumpy[i - minutes] == 1:
                current_gain -= customers[i - minutes]
            
            max_gain = max(max_gain, current_gain)
        
        return base + max_gain
        


