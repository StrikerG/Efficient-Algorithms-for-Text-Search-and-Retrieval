from anytree import Node, RenderTree
import matplotlib.pyplot as plt
import networkx as nx
import uuid


class MyNode(Node):
    def __init__(self, name, parent=None, start=None, end=None):
        super().__init__(name, parent)
        self.start = start
        self.end = end
        self.id = uuid.uuid4()


class SuffixTree(object):
    def __init__(self, string):
        self.string = string
        self.root = MyNode("Root")
        self.active_node = self.root
        self.active_edge = None
        self.active_length = 0
        self.remainder = 0
        self.end = -1
        self.build_tree()

    def build_tree(self):
        for i in range(len(self.string)):
            self.add_char(i)

    def add_char(self, i):
        self.remainder += 1
        self.end = i
        while self.remainder > 0:
            if self.active_length == 0:
                self.active_edge = i
            if not any(child.name.startswith(self.string[self.active_edge]) for child in self.active_node.children):
                new_node = MyNode(self.string[i:] + " [" + str(i) + ":∞]", parent=self.active_node, start=i, end=self.end)
                self.remainder -= 1
            else:
                next_node = next(child for child in self.active_node.children if
                                 child.name.startswith(self.string[self.active_edge]))
                if self.active_length >= len(next_node.name):
                    self.active_edge += len(next_node.name)
                    self.active_length -= len(next_node.name)
                    self.active_node = next_node
                    continue
                if self.string[self.active_length] == self.string[i]:
                    self.active_length += 1
                    break
                split_node = MyNode(next_node.name[:self.active_length], parent=self.active_node, start=next_node.start, end=next_node.start + self.active_length - 1)
                next_node.parent = split_node
                next_node.name = next_node.name[self.active_length:]
                new_leaf = MyNode(self.string[i:] + " [" + str(i) + ":∞]", parent=split_node, start=i, end=self.end)
                self.remainder -= 1
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = i - self.remainder + 1
            elif self.active_node != self.root:
                self.active_node = self.root

    def draw(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s" % (pre, node.name))

    def draw_matplotlib(self):
        def add_edges(node):
            for child in node.children:
                G.add_edge(node.id, child.id)
                add_edges(child)

        G = nx.DiGraph()
        add_edges(self.root)

        # 使用shell_layout替代spring_layout
        pos = nx.shell_layout(G)
        labels = {node.id: node.name for node in self.root.descendants}

        # 调整node_size参数的值来改变节点的大小
        nx.draw_networkx(G, pos, labels=labels, with_labels=True, arrows=True, node_color='skyblue', node_size=500,
                         edge_color='gray')
        plt.show()

    def search_all(self, pattern):
        def dfs(node, path):
            # 如果当前路径匹配模式字符串，将开始位置添加到结果中
            if path.startswith(pattern):
                if len(path) >= len(pattern):
                    matches.append(node.start)
            # 遍历所有子节点
            for child in node.children:
                dfs(child, path + child.name)

        matches = []
        dfs(self.root, "")  # 在这里开始新的搜索，路径被重置为""
        result = matches if matches else "fail"  # 如果没有找到匹配，返回"fail"
        print(f"'{pattern}' found at indices: {result}")  # 打印搜索结果
        return result

    # def search_all(self, pattern):
    #     matches = []
    #     stack = [(self.root, "")]  # 初始时，栈中只有根节点
    #     while stack:
    #         node, path = stack.pop()  # 弹出栈顶的节点
    #         if path.startswith(pattern):
    #             if len(path) >= len(pattern):  # 添加这个条件语句
    #                 matches.append(node.start)
    #         for child in node.children:
    #             stack.append((child, path + child.name))  # 将子节点和对应的路径压入栈中
    #     result = matches if matches else "fail"  # 如果没有找到匹配，返回"fail"
    #     print(f"'{pattern}' found at indices: {result}")  # 打印搜索结果
    #     return result
    def count_nodes(self):
        def dfs(node):
            count = 1  # count this node
            for child in node.children:
                count += dfs(child)  # add the count of child nodes
            return count

        return dfs(self.root)  # start from the root


if __name__ == "__main__":
    tree = SuffixTree("guanxinyu")
    print("Suffix Tree: ", tree)
    print("\nTree Structure:")
    tree.draw()

    tree.draw_matplotlib()
    tree.search_all('u')
    tree.search_all('a')
    tree.search_all('xiny')
    tree.search_all('gg')
    print("Number of nodes: ", tree.count_nodes())



