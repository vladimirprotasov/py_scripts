def find_difference(a: list, b: list):
    """Find the difference between two lists. Complexity is O(n)."""
    idx_a, idx_b = 0, 0
    diff_list = []

    while idx_a < len(a) and idx_b < len(b):
        if a[idx_a] < b[idx_b]:
            diff_list.append(a[idx_a])
            idx_a += 1
        elif a[idx_a] > b[idx_b]:
            diff_list.append(b[idx_b])
            idx_b += 1
        else:
            # Skip the common elements
            idx_a += 1
            idx_b += 1

    diff_list.extend(a[idx_a:])
    diff_list.extend(b[idx_b:])

    return diff_list

# Example usage
list_1 = [1, 2, 3, 4, 20, 21, 22]
list_2 = [3, 4, 5, 8, 19, 20, 24]
# print(find_difference(list_1, list_2))


def find_difference_2(a: list, b: list):
    diff_a = set(a).difference(set(b))
    diff_b = set(b).difference(set(a))

    diff_list = sorted(diff_a.union(diff_b))

    return diff_list


print(find_difference_2(list_1, list_2))