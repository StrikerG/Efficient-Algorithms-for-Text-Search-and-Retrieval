import string
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
import psutil
import os


if __name__ == '__main__':
    # 定义模式长度
    pattern_length = 10

    # 定义数据集大小范围
    min_dataset_size = 100
    max_dataset_size = 500
    step_size = 100



    pattern_lengths = []
    execution_times_naive = []
    execution_times_kmp = []
    execution_times_rk = []
    execution_times_bm = []
    execution_times_suffix_tries = []
    execution_times_suffix_tree = []

    memory_usages_naive = []
    cpu_usages_naive = []
    memory_usages_kmp = []
    cpu_usages_kmp = []
    memory_usages_rk = []
    cpu_usages_rk = []
    memory_usages_bm = []
    cpu_usages_bm = []
    memory_usages_suffix_tries = []
    cpu_usages_suffix_tries = []
    memory_usages_suffix_tree = []
    cpu_usages_suffix_tree = []
    node_counts_tries = []
    node_counts_tree = []

    process = psutil.Process(os.getpid())

    for dataset_size in range(min_dataset_size, max_dataset_size + 1, step_size):
        pattern_lengths.append(dataset_size)
        # 获取reuters语料库的英文文本数据
        nltk.download('reuters')
        corpus = nltk.corpus.reuters
        raw_text = corpus.raw()[:dataset_size]
        start_pos = random.randint(0, len(raw_text) - pattern_length)
        pattern = raw_text[start_pos: start_pos + pattern_length]

        # 在每个循环开始时获取内存和CPU使用情况
        memory_usage_before = process.memory_info().rss
        cpu_usage_before = process.cpu_percent(interval=None)

        # Naïve Algorithm
        start_time_naive = time.time()
        indices_naive = naive_search(raw_text, pattern)
        end_time_naive = time.time()
        execution_time_naive = end_time_naive - start_time_naive
        execution_times_naive.append(execution_time_naive)

        # 在每个循环结束时获取内存和CPU使用情况，并计算差值
        memory_usage_after = process.memory_info().rss
        cpu_usage_after = process.cpu_percent(interval=None)

        memory_usages_naive.append(memory_usage_after - memory_usage_before)
        cpu_usages_naive.append(cpu_usage_after - cpu_usage_before)

        # KMP Algorithm
        memory_usage_before = process.memory_info().rss
        cpu_usage_before = process.cpu_percent(interval=None)

        start_time_kmp = time.time()
        index_kmp = kmp_search(raw_text, pattern)
        end_time_kmp = time.time()
        execution_time_kmp = end_time_kmp - start_time_kmp
        execution_times_kmp.append(execution_time_kmp)

        memory_usage_after = process.memory_info().rss
        cpu_usage_after = process.cpu_percent(interval=None)

        memory_usages_kmp.append(memory_usage_after - memory_usage_before)
        cpu_usages_kmp.append(cpu_usage_after - cpu_usage_before)

        # Rabin-Karp Algorithm
        memory_usage_before = process.memory_info().rss
        cpu_usage_before = process.cpu_percent(interval=None)

        start_time_rk = time.time()
        indices_rk = rabin_karp_search(raw_text, pattern)
        end_time_rk = time.time()
        execution_time_rk = end_time_rk - start_time_rk
        execution_times_rk.append(execution_time_rk)

        memory_usage_after = process.memory_info().rss
        cpu_usage_after = process.cpu_percent(interval=None)

        memory_usages_rk.append(memory_usage_after - memory_usage_before)
        cpu_usages_rk.append(cpu_usage_after - cpu_usage_before)

        # Boyer-Moore Algorithm
        memory_usage_before = process.memory_info().rss
        cpu_usage_before = process.cpu_percent(interval=None)

        start_time_bm = time.time()
        index_bm = boyer_moore(raw_text, pattern)
        end_time_bm = time.time()
        execution_time_bm = end_time_bm - start_time_bm
        execution_times_bm.append(execution_time_bm)

        memory_usage_after = process.memory_info().rss
        cpu_usage_after = process.cpu_percent(interval=None)

        memory_usages_bm.append(memory_usage_after - memory_usage_before)
        cpu_usages_bm.append(cpu_usage_after - cpu_usage_before)

        # Suffix Tries Algorithm
        suffix_tries = SuffixTries()
        suffix_tries.build_tree(raw_text)
        start_time_suffix_tries = time.time()
        indices_suffix_tries = suffix_tries.search_text(pattern)
        end_time_suffix_tries = time.time()
        execution_time_suffix_tries = end_time_suffix_tries - start_time_suffix_tries
        execution_times_suffix_tries.append(execution_time_suffix_tries)

        memory_usage_after = process.memory_info().rss
        cpu_usage_after = process.cpu_percent(interval=None)

        memory_usages_suffix_tries.append(memory_usage_after - memory_usage_before)
        cpu_usages_suffix_tries.append(cpu_usage_after - cpu_usage_before)

        # Suffix Tree Algorithm
        suffix_tree = SuffixTree(raw_text + '$')  # 使用SuffixTree类
        start_time_suffix_tree = time.time()
        indices_suffix_tree = suffix_tree.search_all(pattern)
        end_time_suffix_tree = time.time()
        execution_time_suffix_tree = end_time_suffix_tree - start_time_suffix_tree
        execution_times_suffix_tree.append(execution_time_suffix_tree)

        memory_usage_after = process.memory_info().rss
        cpu_usage_after = process.cpu_percent(interval=None)

        memory_usages_suffix_tree.append(memory_usage_after - memory_usage_before)
        cpu_usages_suffix_tree.append(cpu_usage_after - cpu_usage_before)

        # 获取节点数量
        node_counts_tries.append(suffix_tries.count_nodes())
        node_counts_tree.append(suffix_tree.count_nodes())

    # 在图表中添加内存使用情况
    plt.figure(figsize=(10, 5))  # 创建新的图表
    plt.title('Memory Usage')  # 设置图表标题
    plt.plot(pattern_lengths, memory_usages_naive, label="Memory Usage (Naïve)")
    plt.plot(pattern_lengths, memory_usages_kmp, label="Memory Usage (KMP)")
    plt.plot(pattern_lengths, memory_usages_rk, label="Memory Usage (Rabin-Karp)")
    plt.plot(pattern_lengths, memory_usages_bm, label="Memory Usage (Boyer-Moore)")
    plt.plot(pattern_lengths, memory_usages_suffix_tries, label="Memory Usage (Suffix Tries)")
    plt.plot(pattern_lengths, memory_usages_suffix_tree, label="Memory Usage (Suffix Tree)")
    plt.legend()
    plt.show()

    # 在图表中添加CPU使用情况
    plt.figure(figsize=(10, 5))  # 创建新的图表
    plt.title('CPU Usage')  # 设置图表标题
    plt.plot(pattern_lengths, cpu_usages_naive, label="CPU Usage (Naïve)")
    plt.plot(pattern_lengths, cpu_usages_kmp, label="CPU Usage (KMP)")
    plt.plot(pattern_lengths, cpu_usages_rk, label="CPU Usage (Rabin-Karp)")
    plt.plot(pattern_lengths, cpu_usages_bm, label="CPU Usage (Boyer-Moore)")
    plt.plot(pattern_lengths, cpu_usages_suffix_tries, label="CPU Usage (Suffix Tries)")
    plt.plot(pattern_lengths, cpu_usages_suffix_tree, label="CPU Usage (Suffix Tree)")
    plt.legend()
    plt.show()

    # 在图表中添加节点数量
    plt.figure(figsize=(10, 5))  # 创建新的图表
    plt.title('Node Count')  # 设置图表标题
    plt.plot(pattern_lengths, node_counts_tries, label="Node Count (Suffix Tries)")
    plt.plot(pattern_lengths, node_counts_tree, label="Node Count (Suffix Tree)")
    plt.legend()
    plt.show()

    # 打印节点数量
    print("Node Count (Suffix Tries):", node_counts_tries)
    print("Node Count (Suffix Tree):", node_counts_tree)


