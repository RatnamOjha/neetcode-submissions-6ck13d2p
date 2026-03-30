class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        validSub = 0
        Sum = sum(arr[:k])
        
        if Sum/k >= threshold:
            validSub += 1
        
        for r in range(k,len(arr)):
            Sum = Sum - arr[r-k] + arr[r]
            if Sum/k >= threshold:
                validSub += 1
        return validSub
