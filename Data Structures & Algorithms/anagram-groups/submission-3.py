class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """

        The approach is pretty simple:
1. We iterate over all our strings.
2. For each string, we calculate a representation of its characters, so the counts of each character that it has. Since it's lowercase, this can be a lot simpler.
3. We simply use this as a key and then add the word as a value.
4. We get all of our keys in our map and append all the lists to an output list.

        """

        wordMap = defaultdict(list)

        for word in strs:

            countMap = [0] * 26

            for c in word:
                index = ord(c) - ord('a')
                countMap[index] += 1

            wordMap[tuple(countMap)].append(word)

        output = []

        for k, v in wordMap.items():
            output.append(v)

        return output
        