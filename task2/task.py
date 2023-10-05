import json as js

import anytree.search
from anytree import Node, RenderTree


def json_to_tree_core(json_obj, parent=None):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            node = Node(key, parent=parent)
            json_to_tree_core(value, parent=node)
    else:
        Node(str(json_obj), parent=parent)


def json_to_tree(json_obj):
    root = list(json_obj.keys())[0]
    parent = Node(root)
    for key, value in json_obj[root].items():
        node = Node(key, parent=parent)
        json_to_tree_core(value, parent=node)

    return parent


def group_by_classes(json: str):
    json_obj = js.loads(json)

    tree = json_to_tree(json_obj)

    def filter_g1(n: Node):
        return len(n.children) > 0

    g1 = anytree.search.findall(tree, filter_g1)

    print(g1)






if __name__ == '__main__':
    json_str = '''
    {
      "ROOT": {
        "CHILD1" : {
            "CHILD1_1": "VAULE",
            "CHILD1_2": "VAULE2"
        },
        "CHILD2" : {
            "CHILD2_1": "VAULE3",
            "CHILD2_2": "VAULE4"
        }
      }
    }
    '''
    group_by_classes(json_str)







