from typing import List
import string

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['hit']


def most_common_word(line: str, banList: List[str]) -> str:
    word_dict = {}
    rev_dict = {}
    for word in paragraph.split():
        word = word.strip(string.punctuation).lower()
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    for banword in banList:
        if banword in word_dict:
            del (word_dict[banword])

    for k, v in word_dict.items():
        rev_dict[v] = k
    ans_list = list(rev_dict.items())
    ans_list.sort(key=lambda x: -x[0])
    return ans_list[0][1]


print(most_common_word(paragraph, banned))
