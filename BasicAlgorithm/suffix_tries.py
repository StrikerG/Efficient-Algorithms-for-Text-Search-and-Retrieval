# 算法中使用的主要数据结构是SuffixTriesNode类和SuffixTries类。
#
# SuffixTriesNode类表示后缀树的节点。每个节点包含一个字符char、
# 一个子节点字典children和一个索引列表indices。children字典用于存储当前节点的子节点，
# 键是子节点的字符，值是对应的子节点对象。indices列表用于存储当前节点所代表的后缀在原始文本中的起始索引。
class SuffixTriesNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.indices = []


# SuffixTries类是后缀树的主类。它具有一个根节点root，初始时根节点的字符为空字符串''。
# add_suffix方法用于向后缀树中添加一个后缀，它接受后缀和对应的索引作为参数。
# build_tree方法用于构建整个后缀树，它遍历输入文本的每个位置，并将从当前位置到文本末尾的后缀添加到后缀树中。
# search_text方法用于在后缀树中搜索给定的模式，它遍历模式中的每个字符，
# 并按照相应的路径在后缀树中向下移动，直到找到匹配的模式或到达后缀树的叶子节点。
class SuffixTries:
    def __init__(self):
        self.root = SuffixTriesNode('')

    # 当调用add_suffix方法时，将后缀字符串和对应的起始索引作为参数传递给该方法。
    # 方法首先将当前节点设为根节点，然后遍历后缀字符串的每个字符。
    # 对于每个字符，检查是否存在于当前节点的子节点中。如果不存在，就创建一个新的子节点，并将该字符作为其字符值。
    # 然后将当前节点移动到新创建的子节点。最后，将后缀的起始索引添加到当前节点的索引列表中。
    def add_suffix(self, suffix, index):
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTriesNode(char)
            #这里会移动指针
            node = node.children[char]
            node.indices.append(index)


    # 在build_tree方法中，遍历输入的文本字符串，从索引0到字符串末尾的每个位置。
    # 对于每个位置，获取从当前位置到字符串末尾的后缀字符串，并将其作为参数传递给add_suffix方法。
    # 这样，通过反复调用add_suffix方法，将所有后缀字符串添加到后缀树中。
    def build_tree(self, text):
        for i in range(len(text)):
            suffix = text[i:]
            self.add_suffix(suffix, i)
        # print(self.root.children)

    # 在search_text方法中，遍历要搜索的模式字符串的每个字符。
    # 对于每个字符，检查是否存在于当前节点的子节点中。如果不存在，则表示模式不在后缀树中，返回一个空列表。
    # 如果存在，则将当前节点移动到相应的子节点。
    # 完成后，返回当前节点的索引列表作为模式的匹配结果。
    def search_text(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.indices

    def count_nodes(self, node=None):
        if node is None:
            node = self.root
        count = 1  # 计算当前节点
        for child in node.children.values():
            count += self.count_nodes(child)  # 递归计算子节点
        return count

# 示例用法
if __name__ == '__main__':
    suffix_tries = SuffixTries()
    text = "guanxinyu$"
    pattern = "a"
    suffix_tries.build_tree(text)
    result = suffix_tries.search_text(pattern)
    if result:
        print("Pattern found at indices:", result)
    else:
        print("Pattern not found in the text.")
    print("Number of nodes in the suffix tree:", suffix_tries.count_nodes())
