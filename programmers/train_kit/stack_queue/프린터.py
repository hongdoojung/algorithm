def solution(priorities, location):
    indexes = [i for i in range(len(priorities))]
    index = 0
    while priorities != sorted(priorities, reverse=True):
        if priorities[index] < max(priorities[index+1:]):
            indexes.append(indexes.pop(index))
            priorities.append(priorities.pop(index))
        else:
            index += 1

    return indexes.index(location) + 1