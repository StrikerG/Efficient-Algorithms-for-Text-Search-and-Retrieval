def build_lps(pattern):
    """
    构建最长前缀后缀匹配表（Longest Prefix Suffix table）
    """
    m = len(pattern)
    lps = [0] * m
    length = 0  # 已匹配的最长前缀后缀长度
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    """
    使用KMP算法在文本串中查找模式串，返回所有匹配模式的索引位置
    """
    n = len(text)
    m = len(pattern)
    lps = build_lps(pattern)
    indices = []

    i = j = 0  # i用于遍历text，j用于遍历pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == m:
                # 找到了匹配的模式串，将其起始位置添加到索引列表中
                indices.append(i - j)
                # 继续寻找下一个匹配的模式串
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

# text = "This is a test text"
# pattern = "t"
# kmp_indices = kmp_search(text, pattern)
# print("KMP indices:", kmp_indices)