import random
import nltk
from BasicAlgorithm.kmp import kmp_search
import time
from BasicAlgorithm.bm import boyer_moore

nltk.download('reuters')
corpus = nltk.corpus.reuters
raw_text = corpus.raw()

def calculate_average_time_cost_kmp(length):

    start_time_kmp = time.time()
    for i in range(10):
       index = kmp_search(raw_text, corpus.fileids()[random.randint(1, length)])
    end_time_kmp = time.time()
    execution_time_kmp = end_time_kmp - start_time_kmp
    print("KMP execution average kmp time:", execution_time_kmp/10, "seconds")

def calculate_average_time_cost_bm(length):

    start_time_bm = time.time()
    for i in range(10):
       index = boyer_moore(raw_text, corpus.fileids()[random.randint(1, length)])
    end_time_bm = time.time()
    execution_time_bm = end_time_bm - start_time_bm
    print("BM execution average kmp time:", execution_time_bm/10, "seconds")


