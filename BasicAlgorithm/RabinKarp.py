def rabin_karp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    indices = []

    # 计算模式字符串的哈希值
    pattern_hash = hash(pattern)

    # 计算文本中第一个窗口的初始哈希值
    window_hash = hash(text[:m])

    for i in range(n - m + 1):
        # 检查哈希值是否匹配并且子串与模式字符串完全匹配
        if pattern_hash == window_hash and text[i:i + m] == pattern:
            indices.append(i)

        # 更新下一个窗口的哈希值
        if i < n - m:
            window_hash = hash(text[i + 1:i + m + 1])

    return indices
