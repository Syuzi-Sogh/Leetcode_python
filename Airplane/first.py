from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        key = tuple(sorted(s))
        anagram_map[key].append(s)

    return list(anagram_map.values())

str = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(str))