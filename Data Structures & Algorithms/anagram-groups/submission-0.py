class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            # Use the sorted characters as a canonical identifier
            key = "".join(sorted(word))
            groups[key].append(word)

        # All grouped anagrams can be retrieved via .values()
        result = list(groups.values())
        return result