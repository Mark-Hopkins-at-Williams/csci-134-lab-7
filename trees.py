def tree_node(l, lbl, r):
    return [l, lbl, r]


def leaf(lbl):
    return tree_node(None, lbl, None)


def label(node):
    return node[1]


def left(node):
    return node[0]


def right(node):
    return node[2]


def set_label(node, label):
    node[1] = label


def set_left(node, left_node):
    node[0] = left_node


def set_right(node, right_node):
    node[2] = right_node


def has_left(node):
    return left(node) != None


def has_right(node):
    return right(node) != None


def is_leaf(node):
    return not has_left(node) and not has_right(node)


def viz(node, stringify_label=str):
    def viz_helper(node, indent):
        result = ""
        if node == None:
            return result
        result = result + stringify_label(label(node)) + "\n"
        if left(node) != None:
            left_str = viz_helper(left(node), indent+2)
            result = result + (" " * indent) + "--L--> " + left_str
        if right(node) != None:
            right_str = viz_helper(right(node), indent+2)
            result = result + (" " * indent) + "--R--> " + right_str
        return result
    print(viz_helper(node, 0).strip())





