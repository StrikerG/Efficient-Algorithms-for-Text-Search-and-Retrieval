def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    indices = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)

    return indices
