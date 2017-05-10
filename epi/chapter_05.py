def get_parity(x):
    parity = 0
    while x:
        last_byte = x & 255
        parity += BYTE_PARITY[last_byte]
        x = x >> 8
    return parity % 2


def make_lookup_table(size):
    result = []
    for i in range(size):
        x = i
        num_bits = 0
        while x:
            num_bits += (x & 1)
            x = x >> 1
        result.append(num_bits)
    return result


BYTE_PARITY = make_lookup_table(256)


def swap_bits(x, i, j):
    i_b = get_bit(x, i)
    j_b = get_bit(x, j)
    if i_b == j_b:
        return x
    x = toggle_bit(x, i)
    return toggle_bit(x, j)


def get_bit(x, i):
    return (x >> i) & 1


def toggle_bit(x, i):
    return x ^ (1 << i)


def reverse_bits(x):
    result = 0
    for i in range(8):
        result <<= 8
        result = result | reverse_byte(x & 255)
        x >>= 8
    return result


def reverse_byte(b):
    return REVERSED_BYTES[b]


def make_reversed_bytes():
    result = []
    for i in range(256):
        x = 0
        n = i
        for _ in range(8):
            x <<= 1
            x = x | (n & 1)
            n >>= 1
        result.append(x)
    return result


REVERSED_BYTES = make_reversed_bytes()
