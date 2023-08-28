def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    indices = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            indices.append(i)

    return indices

text = "This is a test text guanxinyu is a good person"
pattern = "i"
naive_indices = naive_search(text, pattern)
print("Naive Search indices:", naive_indices)