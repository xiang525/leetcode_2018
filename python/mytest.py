class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dic = {}
        for index, value in enumerate(words):
            if value not in dic:
                dic[value] = [index]
            else:
                dic[value] += index,

        print(dic)
        return min(set(abs(x-y) for x in dic[word1] for y in dic[word2]) - set([0]))




a = Solution()
word = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"
a.shortestWordDistance(word, word1, word2)

