import string


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


def string_to_int(s):
    if not s:
        raise ValueError
    mul = 1
    result = 0
    for i, c in enumerate(s):
        if i == 0 and c == '-':
            mul = -1
            continue
        if c not in string.digits:
            raise ValueError
        result = result * 10 + (ord(c) - ord('0'))
    return result * mul


def int_to_string(x):
    parts = []
    if x < 0:
        neg = True
    else:
        neg = False
    x = abs(x)
    for d in get_digits(x):
        parts.append(str(d))
    if neg:
        parts.append('-')
    return ''.join(reversed(parts))


def get_digits(x):
    x, rem = divmod(x, 10)
    yield rem
    while x:
        x, rem = divmod(x, 10)
        yield rem


def main():
    print('powerset of {1, 2, 3}')
    print_powerset({1, 2, 3})
    print('powerset of {}')
    print_powerset(set())


def base_conversion(s, b1, b2):
    assert s and (2 <= b1 <= 16) and (2 <= b2 <= 16)
    x = bconvert_to_int(s, b1)
    return bconvert_to_string(x, b2)


def bconvert_to_int(s, b):
    mul = 1
    allowed_digits = get_allowed_digits(b)
    result = 0
    for i, c in enumerate(s):
        if i == 0 and c == '-':
            mul = -1
            continue
        if c not in allowed_digits:
            raise ValueError
        result = result * b + allowed_digits[c]
    return result * mul


CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']


def bconvert_to_string(x, b):
    if x < 0:
        neg = True
        x = -x
    else:
        neg = False
    parts = []
    for digit in bget_digits(x, b):
        parts.append(CHARS[digit])
    if neg:
        parts.append('-')
    return ''.join(reversed(parts))


def bget_digits(x, b):
    x, rem = divmod(x, b)
    yield rem
    while x:
        x, rem = divmod(x, b)
        yield rem


def get_allowed_digits(b):
    assert 2 <= b <= 16
    return {
        CHARS[i]: i
        for i in range(0, b)
    }


if __name__ == '__main__':
    main()
