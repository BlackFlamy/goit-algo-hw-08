"""Тема 8. Злиття k відсортованих списків через мінімальну купу (heapq)."""

import heapq


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    heap = []
    # (значення, індекс списку, індекс елемента) - індекс списку розрулює однакові значення
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    merged = []
    while heap:
        value, list_idx, elem_idx = heapq.heappop(heap)
        merged.append(value)
        next_idx = elem_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(heap, (lists[list_idx][next_idx], list_idx, next_idx))
    return merged


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
