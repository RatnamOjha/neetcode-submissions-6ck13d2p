class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefx = 0
        count = 0
        hashmap = {}

        for n in nums:
            prefx += n

            if prefx == k:
                count += 1
            if prefx - k in hashmap:
                count += hashmap[prefx - k]
            hashmap[prefx] = hashmap.get(prefx,0) + 1

        return count