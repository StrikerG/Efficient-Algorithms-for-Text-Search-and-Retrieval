#第一种生成文本字符串的方法
from BasicAlgorithm.kmp import kmp_search
from BasicAlgorithm.bm import boyer_moore
import time
# from generate_suffix_tree import  build_suffix_tree,search_text
import os

def algorithm_correction_text():
    folder_path = 'text_source_data'
    file_names = os.listdir(folder_path)
    # print(file_names)
    raw_text = ""

    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r') as file:
            raw_text += file.read()
    # 打印合并后的文本内容
    # print(raw_data)
    pattern = "are"

    #kmp part
    start_time_kmp = time.time()
    index = kmp_search(raw_text, pattern)
    if index != -1:
        print("Pattern found at index", index)
    else:
        print("Pattern not found")
    end_time_kmp = time.time()
    execution_time_kmp = end_time_kmp - start_time_kmp
    print("Execution kmp time:", execution_time_kmp, "seconds")
    # #计算kmp平均用时
    # calculate_average_time_cost_kmp(len(corpus.fileids()))

    #bm part
    start_time_bm = time.time()
    result = boyer_moore(raw_text, pattern)
    if result == -1:
        print("Pattern not found in the text.")
    else:
        print("Pattern found at index", result)
    end_time_bm = time.time()
    execution_bm = end_time_bm - start_time_bm
    print("Execution bm time:", execution_bm, "seconds")
    # #计算bm平均用时
    # calculate_average_time_cost_bm(len(corpus.fileids()))


    # #suffix tree
    # start_time_suffix_tree = time.time()
    # root = build_suffix_tree(raw_text)
    # result = search_text(root, pattern)
    # if result == -1:
    #     print("Pattern not found in the text.")
    # else:
    #     print("Pattern found at index", result)
    # end_time_suffix_tree = time.time()
    # execution_suffix_tree = end_time_suffix_tree - start_time_suffix_tree
    # print("Execution suffix tree time:", execution_suffix_tree, "seconds")
algorithm_correction_text()