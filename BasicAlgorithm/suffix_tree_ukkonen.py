from anytree import Node, RenderTree
import uuid

class MyNode(Node):
    def __init__(self, name, parent=None, start=None, end=None):
        super().__init__(name, parent)
        self.start = start
        self.end = end
        self.id = uuid.uuid4()
        self.suffix_link = None  # Adding suffix link

class UkkonenSuffixTree:
    def __init__(self, string):
        self.string = string + "$"
        self.root = MyNode("Root")
        self.active_node = self.root
        self.active_edge = -1
        self.active_length = 0
        self.remainder = 0
        self.last_new_node = None
        self.build_tree()

    def build_tree(self):
        for i in range(len(self.string)):
            self.add_suffix(i)

    def add_suffix(self, pos):
        self.remainder += 1
        last_new_node = None

        while self.remainder > 0:
            if self.active_length == 0:
                self.active_edge = pos

            next_node = next((child for child in self.active_node.children if child.name.startswith(self.string[self.active_edge])), None)

            if not next_node:
                new_leaf = MyNode(self.string[pos:], self.active_node, pos, len(self.string) - 1)
                if self.last_new_node:
                    self.last_new_node.suffix_link = self.active_node
                self.last_new_node = None
            else:
                if self.walk_down(next_node, pos):
                    continue

                if self.string[next_node.start + self.active_length] == self.string[pos]:
                    if last_new_node and self.active_node != self.root:
                        last_new_node.suffix_link = self.active_node
                    self.active_length += 1
                    break

                split_end = next_node.start + self.active_length - 1
                split_node = MyNode(self.string[next_node.start:split_end + 1], self.active_node, next_node.start, split_end)
                next_node.parent = split_node
                next_node.start += self.active_length
                next_node.name = self.string[next_node.start:]
                MyNode(self.string[pos:], split_node, pos, len(self.string) - 1)

                if last_new_node:
                    last_new_node.suffix_link = split_node
                last_new_node = split_node

            self.remainder -= 1
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = pos - self.remainder + 1
            elif self.active_node != self.root:
                self.active_node = self.active_node.suffix_link if self.active_node.suffix_link else self.root

    def walk_down(self, node, pos):
        edge_length = node.end - node.start + 1
        if self.active_length >= edge_length:
            self.active_edge += edge_length
            self.active_length -= edge_length
            self.active_node = node
            return True
        return False

    def draw(self):
        for pre, fill, node in RenderTree(self.root):
            print("%s%s [%s:%s]" % (pre, node.name, node.start, node.end if node.end != float('inf') else '∞'))

    def count_nodes(self):
        def dfs(node):
            count = 1
            for child in node.children:
                count += dfs(child)
            return count

        return dfs(self.root)
    def search_all(self, pattern):
        # 一. 第一步搞定这个pattern的匹配点最后匹配在哪个结点,这个是比较关键的.这个步骤分了好几种情况
        # 首先说一下他的匹配过程首先从根节点出发,所有遍历孩子结点, 用pattern[0]去做匹配看是不是这些孩子节点的前缀
        # 1如果是就继续匹配,如果不是就直接返回不存在这个后缀树中
        # 2当继续匹配时,就会有两种情况出现,一个是pattern比这个结点短,另一个情况是比这个结点长,
        # 但是不管如何都要继续匹配pattern[1],pattern[2]
        # 2.1 pattern比这个结点短,那就把pattern全部字符都对比完,看看pattern是不是该结点的前缀,如果是那么直接返回该结点的start,如果不是,那说明整个字符串数据里没有pattern这个字符串
        # 2.2 pattern比这个结点长,首先判断他有没有孩子结点,如果没有就说明没找到这个pattern,如果有孩子,则继续2的过程,直到找到这个匹配结点为止.

        # 二. 第二步根据这个找到的结点,遍历该结点的下面的树,这里分几种情况
        # 1.第一种情况,找到的这个匹配点是叶子结点,直接返回该结点的start

        # 2.第二种情况,如果该匹配点不是叶子结点,那么就通过leaf属性,直接找到该匹配点的所有叶子结点,
        # 并记录所有叶子结点的start下标,还要记录一下叶子结点到root到这个匹配结点中,每个结点的长度
        # 那么计算这个中间的结点有什么意义呢?因为如果你想找到你的pattern匹配下标在哪里,你得用叶子结点的start减去到root的所有节点长度之和
        # 我说这里是长度之和,比如结点a长度2结点b长度3,那他们之和就是5,然后再用这个start减去这个长度之和5就完了.
        # 需要注意的是匹配结点下面的所有叶子结点都得经过上面这个第二种情况的所有步骤来一遍,最后都得出一个值,然后最后汇总到match[]里面就行了

        current_node = self.root
        i = 0
        while i < len(pattern):
            found = False
            for child in current_node.children:
                if child.name.startswith(pattern[i]):
                    overlap_len = min(len(child.name), len(pattern) - i)
                    if pattern[i:i + overlap_len] == child.name[:overlap_len]:
                        i += overlap_len
                        current_node = child
                        found = True
                        break
            if not found:
                return []  # Pattern not found in the tree
        print(current_node.name,'[',current_node.start,',',current_node.end,']',
              current_node.parent.name,current_node.parent.start,current_node.parent.end)

        # Collect all leaf nodes below the current node
        all_leaf_nodes = current_node.leaves
        al_matches = []
        for leaf_node in all_leaf_nodes:
            sum_length = 0
            temp_node = leaf_node
            # print(leaf_node.name)
            # print(temp_node.parent.parent.parent.parent.is_root)
            # print(not leaf_node.parent.is_root)
            while not temp_node.parent.is_root == True:
                temp_node = temp_node.parent
                # print(temp_node.name, temp_node.start, temp_node.end)
                sum_length += temp_node.end - temp_node.start +1
            # print(sum_length)
            al_matches.append(leaf_node.start - sum_length)
        return al_matches
if __name__ == "__main__":
    # Test the revised UkkonenSuffixTree
    ukkonen_tree_revised = UkkonenSuffixTree("mississippi")
    print("\nRevised Ukkonen Suffix Tree Structure:")
    ukkonen_tree_revised.draw()
    search_result = ukkonen_tree_revised.search_all('i')
    print("Search results :", search_result)
    print("Number of nodes in the revised tree: ", ukkonen_tree_revised.count_nodes())
