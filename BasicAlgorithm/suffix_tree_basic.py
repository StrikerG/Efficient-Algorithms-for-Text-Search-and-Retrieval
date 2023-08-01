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


class SuffixTreeSplittingAlgorithm(object):
    def __init__(self, string):
        self.string = string
        self.root = MyNode("Root")
        self.build_tree()

    def build_tree(self):
        for i in range(len(self.string)):
            self.add_suffix(i)

    def add_suffix(self, i):
        current_node = self.root
        j = i
        while j < len(self.string):
            if not any(child.name.startswith(self.string[j]) for child in current_node.children):
                new_node = MyNode(self.string[j:] + " [" + str(j) + ":∞]", parent=current_node, start=j, end=len(self.string))
                break
            else:
                next_node = next(child for child in current_node.children if
                                 child.name.startswith(self.string[j]))
                k = 0
                while k < len(next_node.name) and self.string[j] == next_node.name[k]:
                    j += 1
                    k += 1
                if k == len(next_node.name):
                    current_node = next_node
                else:
                    split_node = MyNode(next_node.name[:k] + " [" + str(next_node.start) + ":" + str(next_node.start + k - 1) + "]",
                                        parent=current_node, start=next_node.start, end=next_node.start + k - 1)
                    next_node.name = next_node.name[k:]
                    next_node.start += k
                    next_node.parent = split_node
                    new_node = MyNode(self.string[j:] + " [" + str(j) + ":∞]", parent=split_node, start=j, end=len(self.string))
                    break

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

        pos = nx.shell_layout(G)
        labels = {node.id: node.name for node in self.root.descendants}

        nx.draw_networkx(G, pos, labels=labels, with_labels=True, arrows=True, node_color='skyblue', node_size=500,
                         edge_color='gray')
        plt.show()

    # def search_all(self, pattern):
    #     def dfs(node, path, start_positions):
    #         if pattern in path:
    #             pattern_start = path.index(pattern)
    #             if pattern_start < len(start_positions):
    #                 position = start_positions[pattern_start]
    #                 if position not in matches:  # Check if the position is already in matches
    #                     matches.append(position)
    #                     return  # Stop searching once a match is found
    #         for child in node.children:
    #             new_path = path + child.name
    #             if child.end == float('inf'):  # check if child.end is infinity
    #                 new_start_positions = start_positions + [child.start]
    #             else:
    #                 new_start_positions = start_positions + list(range(child.start, child.end + 1))
    #             dfs(child, new_path, new_start_positions)
    #
    #     matches = []
    #     dfs(self.root, "", [])
    #     print(f"'{pattern}' found at indices: ", matches)
    #     return matches

    def search_all(self, pattern):
        def search_node(node, path, start_positions):
            if pattern in path:
                pattern_start = path.index(pattern)
                if pattern_start < len(start_positions):
                    position = start_positions[pattern_start]
                    if position not in matches:  # Check if the position is already in matches
                        matches.append(position)
                        return True
            for child in node.children:
                new_path = path + child.name
                if child.end == float('inf'):  # check if child.end is infinity
                    new_start_positions = start_positions + [child.start]
                else:
                    new_start_positions = start_positions + list(range(child.start, child.end + 1))
                if search_node(child, new_path, new_start_positions):
                    return True
            return False

        matches = []
        search_node(self.root, "", [])
        print(f"'{pattern}' found at indices: ", matches)
        return matches

    def count_nodes(self):
        def dfs(node):
            count = 1
            for child in node.children:
                count += dfs(child)
            return count

        return dfs(self.root)


if __name__ == "__main__":
    tree = SuffixTreeSplittingAlgorithm("guanxinyu1$")
    print("Suffix Tree: ", tree)
    print("\nTree Structure:")
    tree.draw()

    # tree.draw_matplotlib()

    tree.search_all('u')
    tree.search_all('a')
    tree.search_all('1')
    tree.search_all('gg')
    print("Number of nodes: ", tree.count_nodes())
