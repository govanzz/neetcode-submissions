class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        output=[]
        for n in nums:
            if n not in dictionary:
                dictionary[n]=1
            else:
                dictionary[n]+=1
        bucket =[]
        for i in range(len(nums)+1):
            bucket.append([])
        for key,value in dictionary.items():
            bucket[value].append(key)
        for i in range(len(nums),0,-1):
            for n in bucket[i]:
                output.append(n)
                if (len(output)==k):
                    return output
        return output
                
        
        