class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26   # 26 lowercase letters

            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)   # lists can't be dict keys, so convert to tuple
            groups[key].append(s)

        return list(groups.values())
        
        