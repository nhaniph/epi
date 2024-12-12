from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0

def h_index_slow(citations: List[int]) -> int:
    count = 1
    while count <= len(citations) + 1:
        papers_with_citations = len(list(filter(lambda x: x >= count, citations)))
        if papers_with_citations < count:
            return count - 1
        count += 1
    return count - 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index_slow))
