from BasicAlgorithm.kmp import kmp_search
from BasicAlgorithm.bm import boyer_moore
from BasicAlgorithm.suffix_tries import SuffixTree
from BasicAlgorithm.Naive_algorithm import naive_search
from BasicAlgorithm.RabinKarp import rabin_karp_search
#第一种生成文本字符串的方法
import nltk
import time
import random

if __name__ == '__main__':
    # # 生成10个长度为5的随机字符串
    # dataset = [generate_random_string(5) for _ in range(10)]
    # print(dataset)

    # 获取reuters语料库的英文文本数据
    nltk.download('reuters')
    corpus = nltk.corpus.reuters
    raw_text = corpus.raw()[0:100000]
    # print(raw_text)
    # 获取前10个文件的文本内容
    # dataset = [corpus.raw(fileid) for fileid in corpus.fileids()[:10]]

    #随机生成模式匹配字符串

    # 生成随机长度的pattern
    min_length = 1  # 最小长度
    max_length = 10  # 最大长度
    pattern_length = random.randint(min_length, max_length)  # 随机生成长度

    # 从raw_text中随机截取pattern_length长度的子字符串作为pattern
    start_index = random.randint(0, len(raw_text) - pattern_length)  # 随机生成起始索引
    pattern = raw_text[start_index: start_index + pattern_length]  # 截取子字符串

    print("Random pattern:", pattern)

    # Naïve Algorithm
    start_time_naive = time.time()
    indices_naive = naive_search(raw_text, pattern)
    end_time_naive = time.time()
    execution_time_naive = end_time_naive - start_time_naive

    print("Naïve Algorithm:")
    if indices_naive:
        print("Pattern found at indices:", indices_naive)
    else:
        print("Pattern not found")
    print("Execution time: {:.6f} seconds".format(execution_time_naive))
    print("————————————————————————")

    # KMP Algorithm
    start_time_kmp = time.time()
    index_kmp = kmp_search(raw_text, pattern)
    end_time_kmp = time.time()
    execution_time_kmp = end_time_kmp - start_time_kmp

    print("KMP Algorithm:")
    if index_kmp != -1:
        print("Pattern found at index:", index_kmp)
    else:
        print("Pattern not found")
    print("Execution time: {:.6f} seconds".format(execution_time_kmp))
    print("————————————————————————")

    # Rabin-Karp Algorithm
    start_time_rk = time.time()
    indices_rk = rabin_karp_search(raw_text, pattern)
    end_time_rk = time.time()
    execution_time_rk = end_time_rk - start_time_rk

    print("Rabin-Karp Algorithm:")
    if indices_rk:
        print("Pattern found at indices:", indices_rk)
    else:
        print("Pattern not found")
    print("Execution time: {:.6f} seconds".format(execution_time_rk))
    print("————————————————————————")

    # Boyer-Moore Algorithm
    start_time_bm = time.time()
    index_bm = boyer_moore(raw_text, pattern)
    end_time_bm = time.time()
    execution_time_bm = end_time_bm - start_time_bm

    print("Boyer-Moore Algorithm:")
    if index_bm != -1:
        print("Pattern found at index:", index_bm)
    else:
        print("Pattern not found")
    print("Execution time: {:.6f} seconds".format(execution_time_bm))
    print("————————————————————————")

    # # Suffix Tree Algorithm
    # start_time_suffix_tree = time.time()
    # suffix_tree = SuffixTree()
    # suffix_tree.build_tree(raw_text)
    # indices_suffix_tree = suffix_tree.search_text(pattern)
    # end_time_suffix_tree = time.time()
    # execution_time_suffix_tree = end_time_suffix_tree - start_time_suffix_tree
    #
    # print("Suffix Tree Algorithm:")
    # if indices_suffix_tree:
    #     print("Pattern found at indices:", indices_suffix_tree)
    # else:
    #     print("Pattern not found")
    # print("Execution time: {:.6f} seconds".format(execution_time_suffix_tree))
    # print("————————————————————————")

