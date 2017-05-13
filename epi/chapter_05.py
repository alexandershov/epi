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


def get_closest(x):
    for i in range(0, 64):
        b = get_bit(x, i)
        if not b:
            continue
        res = try_swap(x, i, i - 1)
        if res is not None:
            return res
        res = try_swap(x, i, i + 1)
        if res is not None:
            return res


def try_swap(x, i, j):
    if j < 0:
        return None
    if j >= 64:
        return None
    if get_bit(x, j):
        return None
    return swap_bits(x, i, j)


def print_powerset(items):
    items = list(items)
    for i in range(0, 2 ** len(items)):
        print_subset(items, i)


def print_subset(items, i):
    b = 0
    while i:
        if i == 1:
            end = ''
        else:
            end = ','
        if i & 1:
            print(items[b], end=end)
        i >>= 1
        b += 1
    print()


def main():
    print('powerset of {1, 2, 3}')
    print_powerset({1, 2, 3})
    print('powerset of {}')
    print_powerset(set())


if __name__ == '__main__':
    main()
