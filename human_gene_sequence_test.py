from BasicAlgorithm.kmp import kmp_search
from BasicAlgorithm.bm import boyer_moore
# from BasicAlgorithm.suffix_tries import SuffixTree
from BasicAlgorithm.Naive_algorithm import naive_search
from BasicAlgorithm.RabinKarp import rabin_karp_search
import time
import random

if __name__ == '__main__':
    with open('text_source_data/human_gene_sequence.txt', 'r') as file:
        raw_text = file.read()

    min_length = 1
    max_length = 10
    pattern_length = random.randint(min_length, max_length)

    start_index = random.randint(0, len(raw_text) - pattern_length)
    pattern = raw_text[start_index: start_index + pattern_length]

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
