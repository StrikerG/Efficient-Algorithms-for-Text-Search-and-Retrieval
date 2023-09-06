def build_bad_character_table(pattern):
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table


def build_good_suffix_table(pattern):
    table = [-1] * len(pattern)
    length = len(pattern)
    suffix = length - 1

    for i in range(length - 2, -1, -1):
        if i > suffix and table[i + length - 1 - suffix] < i - suffix:
            table[i] = table[i + length - 1 - suffix]
        else:
            if i < suffix:
                suffix = i
            j = suffix
            while j >= 0 and pattern[j] == pattern[j + length - 1 - suffix]:
                j -= 1
            table[i] = suffix - j
    return table


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    indices = []

    if m > n:
        return indices

    bad_character_table = build_bad_character_table(pattern)
    good_suffix_table = build_good_suffix_table(pattern)

    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j == -1:
            # 找到了匹配的模式串，将其起始位置添加到索引列表中
            indices.append(i)
            # 继续寻找下一个匹配的模式串
            i += 1
        else:
            bad_character_shift = bad_character_table.get(text[i + j], m)
            good_suffix_shift = good_suffix_table[j]

            i += max(bad_character_shift, good_suffix_shift)

    return indices


# 示例用法
text = "This is a test text guanxinyu is a good person"
pattern = "i"
bm_indices = boyer_moore(text, pattern)
print("Boyer-Moore indices:", bm_indices)