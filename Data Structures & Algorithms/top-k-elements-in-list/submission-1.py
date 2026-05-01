class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         dictionary = {}
         for i in nums:
            if i not in dictionary:
                dictionary[i]=1
            else:
                dictionary[i]+=1
         bucket=[]
         for i in range(len(nums)+1):
            bucket.append([])
         for num,count in dictionary.items():
            bucket[count].append(num)
         result=[]
         for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                   return result 
            
        
         
        
        

