import sys


def main():
    N = int(sys.stdin.readline())
    nodes = list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())

    child_dict = {}
    parent_dict = {}
    for i, node in enumerate(nodes):
        parent_dict[i] = node
        if child_dict.get(node):
            child_dict[node].append(i)
        else:
            child_dict[node] = [i]

    targets = [target]
    # print(targets, parent_dict, child_dict)
    while targets:
        new_targets = []
        for target in targets:
            if child_dict.get(target):
                # print("catch", target)
                new_targets.extend(child_dict.pop(target))
            parent = parent_dict.pop(target)
            if child_dict.get(parent):
                child_dict[parent].remove(target)
                if child_dict[parent] == []:
                    child_dict.pop(parent)
        # print(new_targets, parent_dict, child_dict)
        targets = new_targets
    # print(child_dict)
    # print(len(parent_dict) - len(child_dict))
    print(
        len(set(parent_dict.keys()).difference(set(child_dict.keys())))
    )


if __name__ == '__main__':
    main()


"""
9
-1 0 0 5 2 4 4 6 6
4
2

2
-1 0
1
1
"""
