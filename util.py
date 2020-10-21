from pprint import pprint
from copy import deepcopy


def find_combos(arr):
    combos = []
    for i in range(len(arr) - 1, 0, -1):
        data = []
        combination_util(combos, arr, len(arr), i, 0, deepcopy(data), 0)
    return combos


def combination_util(combos, arr, n, r, index, data, i):
    if index == r:
        combos.append(data)
        return
    if i >= n:
        return
    try:
        data[index] = arr[i]
    except IndexError:
        data.append(arr[i])

    combination_util(combos, arr, n, r, index + 1, deepcopy(data), i + 1)

    combination_util(combos, arr, n, r, index, deepcopy(data), i + 1)


def pairs_contains_pair(pairs, new_pair):
    new_pair_origin = [sorted(new_pair[0]), sorted(new_pair[1])]
    new_pair_reverse = [sorted(new_pair[1]), sorted(new_pair[0])]
    for pair in pairs:
        pair_sorted = [sorted(pair[0]), sorted(pair[1])]
        if pair_sorted == new_pair_origin or pair_sorted == new_pair_reverse:
            return True
    return False


def is_sub_list(origin, sublist):
    l = sorted(origin)
    subl = sorted(sublist)
    if len(l) < len(subl):
        return False
    if l == subl:
        return True
    i = 0
    j = 0
    while i < len(l) and j < len(subl):
        if l[i] == subl[j]:
            i += 1
            j += 1
            if j == len(subl):
                return True
        else:
            i += 1
    return False


def find_pairs(combos, arr):
    pairs = []
    for l1 in combos:
        for l2 in combos:
            if(sum(l1) != sum(l2)):
                continue
            if is_sub_list(arr, l1 + l2):
                new_pair = [l1, l2]
                if not pairs_contains_pair(pairs, new_pair):
                    pairs.append(new_pair)
    return pairs




if __name__ == '__main__':
    arr = [6, 9, 13, 7, 11, 13, 6, 5, 3, 11]
    combos = find_combos(arr)
    pairs = find_pairs(combos, arr)
    pprint(pairs)