def reorder_space(text: str) -> str:
    spaces = text.count(" ")
    words = text.split()
    words_len = len(words)
    if words_len == 1:
        return words[0] + " " * spaces
    gap, extra = divmod(spaces, words_len - 1)
    return (" " * gap).join(words) + " " * extra


print(reorder_space(text="  this   is  a sentence "))
"""
Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
"""
