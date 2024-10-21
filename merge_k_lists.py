import heapq


def merge_k_lists(lists):
    if not lists:
        return []

    heap = []
    for i, list in enumerate(lists):
        if list:
            heapq.heappush(heap, (list[0], i, 0))

    result = []
    while heap:
        value, list_index, element_index = heapq.heappop(heap)
        result.append(value)
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1],
                          list_index, element_index + 1)
            heapq.heappush(heap, next_tuple)

    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)

print("Відсортований список:", merged_list)
