class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def checks(x):
            n=x
            for a in range(len(n)):
                for b in range(len(n)):
                    if n[a]+n[b]==target :
                        if a==b:
                            continue
                        else:
                            return [a,b]
        c=checks(nums)
        return c
