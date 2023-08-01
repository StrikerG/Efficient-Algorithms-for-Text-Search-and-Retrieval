import random
import nltk
import time
from BasicAlgorithm.kmp import kmp_search
from BasicAlgorithm.bm import boyer_moore
from BasicAlgorithm.Naive_algorithm import naive_search
from BasicAlgorithm.RabinKarp import rabin_karp_search
import matplotlib.pyplot as plt
from BasicAlgorithm.suffix_tries import *
from BasicAlgorithm.suffix_tree_ukkonen import *

if __name__ == '__main__':
    # 定义数据集大小
    dataset_size = 1000

    # 定义模式长度范围
    min_pattern_length = 10
    max_pattern_length = 100
    step_size = 10

    pattern_lengths = []
    execution_times_naive = []
    execution_times_kmp = []
    execution_times_rk = []
    execution_times_bm = []
    execution_times_suffix_tries = []
    execution_times_suffix_tree = []

    # 获取reuters语料库的英文文本数据
    nltk.download('reuters')
    corpus = nltk.corpus.reuters
    raw_text = corpus.raw()[:dataset_size]

    for pattern_length in range(min_pattern_length, max_pattern_length + 1, step_size):
        start_pos = random.randint(0, len(raw_text) - pattern_length)
        pattern = raw_text[start_pos: start_pos + pattern_length]

        # Naïve Algorithm
        start_time_naive = time.time()
        indices_naive = naive_search(raw_text, pattern)
        end_time_naive = time.time()
        execution_time_naive = end_time_naive - start_time_naive
        execution_times_naive.append(execution_time_naive)

        # KMP Algorithm
        start_time_kmp = time.time()
        index_kmp = kmp_search(raw_text, pattern)
        end_time_kmp = time.time()
        execution_time_kmp = end_time_kmp - start_time_kmp
        execution_times_kmp.append(execution_time_kmp)

        # Rabin-Karp Algorithm
        start_time_rk = time.time()
        indices_rk = rabin_karp_search(raw_text, pattern)
        end_time_rk = time.time()
        execution_time_rk = end_time_rk - start_time_rk
        execution_times_rk.append(execution_time_rk)

        # Boyer-Moore Algorithm
        start_time_bm = time.time()
        index_bm = boyer_moore(raw_text, pattern)
        end_time_bm = time.time()
        execution_time_bm = end_time_bm - start_time_bm
        execution_times_bm.append(execution_time_bm)

        # Suffix Tries Algorithm
        suffix_tries = SuffixTries()
        suffix_tries.build_tree(raw_text)
        start_time_suffix_tries = time.time()
        indices_suffix_tries = suffix_tries.search_text(pattern)
        end_time_suffix_tries = time.time()
        execution_time_suffix_tries = end_time_suffix_tries - start_time_suffix_tries
        execution_times_suffix_tries.append(execution_time_suffix_tries)

        # Suffix Tree Algorithm
        suffix_tree = SuffixTree(raw_text+'$')  # 使用SuffixTree类
        start_time_suffix_tree = time.time()
        indices_suffix_tree = suffix_tree.search_all(pattern)
        end_time_suffix_tree = time.time()
        execution_time_suffix_tree = end_time_suffix_tree - start_time_suffix_tree
        execution_times_suffix_tree.append(execution_time_suffix_tree)

        pattern_lengths.append(pattern_length)

    # 绘制图表
    plt.plot(pattern_lengths, execution_times_naive, label="Naïve")
    plt.plot(pattern_lengths, execution_times_kmp, label="KMP")
    plt.plot(pattern_lengths, execution_times_rk, label="Rabin-Karp")
    plt.plot(pattern_lengths, execution_times_bm, label="Boyer-Moore")
    plt.plot(pattern_lengths, execution_times_suffix_tries, label="Suffix Tries")
    plt.plot(pattern_lengths, execution_times_suffix_tree, label="Suffix Tree")
    plt.xlabel("Pattern Length")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.show()
