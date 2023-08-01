import random
import string
#第二种生成文本字符串的方法
# 生成包含英文字母的随机字符串
def generate_random_string(length):
    letters = string.ascii_letters
    print(letters)
    return ''.join(random.choice(letters) for _ in range(length))

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# # # 生成10个长度为5的随机字符串
    # # dataset = [generate_random_string(5) for _ in range(10)]
    # # print(dataset)
    #
    # # 获取reuters语料库的英文文本数据
    # nltk.download('reuters')
    # corpus = nltk.corpus.reuters
    # raw_text = corpus.raw()
    # # 获取前10个文件的文本内容
    # dataset = [corpus.raw(fileid) for fileid in corpus.fileids()[:10]]
    # # 计算这个数据包的长度
    # # print(len(corpus.fileids()))
    # # print(corpus.fileids()[:10])
    # # print(dataset)
    # # print(type(raw_text))
    # # print(raw_text)
    # pattern = "hi"