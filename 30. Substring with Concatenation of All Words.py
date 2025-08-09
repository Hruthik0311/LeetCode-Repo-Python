class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        res = []
        for i in range(word_len):
            left = i
            current_count = Counter()
            words_used = 0
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                if word in word_count:
                    current_count[word] += 1
                    words_used += 1
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                    if words_used == num_words:
                        res.append(left)
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        words_used -= 1
                        left += word_len
                else:
                    current_count.clear()
                    words_used = 0
                    left = right + word_len
        return res
