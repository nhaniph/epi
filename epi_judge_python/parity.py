from test_framework import generic_test


def parity(x: int) -> int:
    """
    The parity of a binary word is 1 if the number of 1's in the word is odd;
    Otherwise, it is 0. 
    
    For example, the parity of 1011 is 1 and the parity of 10001000 is 0.
    
    How would you compute the parity of a very large number of 64-bit words?
    """
    bit_count = 0
    while (x):
        bit_count += x & 1
        
        x >>= 1
    
    return bit_count % 2 != 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
