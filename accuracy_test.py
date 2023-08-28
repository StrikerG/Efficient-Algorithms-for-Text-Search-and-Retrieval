import string
import random
import nltk
import time
from BasicAlgorithm.kmp import kmp_search
from BasicAlgorithm.bm import boyer_moore
from BasicAlgorithm.Naive_algorithm import naive_search
from BasicAlgorithm.RabinKarp import rabin_karp_search
from BasicAlgorithm.suffix_tree_basic import SuffixTreeSplittingAlgorithm

def calculate_accuracy(reference_indices, test_indices):
    # Calculate the accuracy of the test_indices by comparing with reference_indices
    correct_count = sum(1 for idx in test_indices if idx in reference_indices)
    if len(test_indices) == 0:
        return 0
    return (correct_count / len(test_indices)) * 100

if __name__ == '__main__':
    # Define pattern length
    pattern_length = 5

    # Download the reuters corpus
    nltk.download('reuters')
    corpus = nltk.corpus.reuters
    raw_text = corpus.raw()

    # Split the raw_text into groups of 1000 words each, and take 5 groups
    words = raw_text.split()
    group_size = 1000
    num_groups = 5

    for group_num in range(num_groups):
        start_idx = group_num * group_size
        end_idx = start_idx + group_size
        group_words = words[start_idx:end_idx]
        group_text = ' '.join(group_words)

        print(f"Processing Group {group_num + 1} ...")

        # Generate a random pattern from the text
        start_pos = random.randint(0, len(group_text) - pattern_length)
        pattern = group_text[start_pos: start_pos + pattern_length]

        # Use Boyer-Moore as the reference algorithm
        reference_indices = boyer_moore(group_text, pattern)

        # Naïve Algorithm
        indices_naive = naive_search(group_text, pattern)
        naive_accuracy = calculate_accuracy(reference_indices, indices_naive)

        # KMP Algorithm
        indices_kmp = kmp_search(group_text, pattern)
        kmp_accuracy = calculate_accuracy(reference_indices, indices_kmp)

        # Rabin-Karp Algorithm
        indices_rk = rabin_karp_search(group_text, pattern)
        rk_accuracy = calculate_accuracy(reference_indices, indices_rk)

        # Suffix Tree Algorithm with splitting algorithm
        suffix_tree = SuffixTreeSplittingAlgorithm(group_text + '$')
        indices_suffix_tree_splitting = (suffix_tree.search_all(pattern))
        suffix_tree_accuracy = calculate_accuracy(reference_indices, indices_suffix_tree_splitting)

        print(f"Naïve Accuracy: {naive_accuracy:.2f}%")
        print(f"KMP Accuracy: {kmp_accuracy:.2f}%")
        print(f"Rabin-Karp Accuracy: {rk_accuracy:.2f}%")
        print(f"Suffix Tree Splitting Accuracy: {suffix_tree_accuracy:.2f}%")
        print("\n" + "="*40 + "\n")
