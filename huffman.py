from numpy import int32


class Node(object):
    
    def __init__(self, left=None, right=None, string = ''):
        self.left = left
        self.right = right
        self.string = string

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


## huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    ##print('type',type(node), print(node))
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency

def cal_freq(string):
    freq = {}
    for c in string:
        if c in freq:
            freq[c] += freq.get(c,1) + 1
        else:
            freq[c] = 1

    nodes = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    ##print(nodes)

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]

        nodes = nodes[:-2]

        ## Add p
        node = Node(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes

def encode(string):
    nodes = cal_freq(string) 
    print(nodes[0][0])
    print(type(nodes[0][0]))
    huffmanCode = huffman_code_tree(nodes[0][0])
    return huffmanCode

if __name__== "__main__":
    string = 'ABBBBCCCTTTTT'
    print(encode(string))