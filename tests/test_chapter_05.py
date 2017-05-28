import string

import pytest

from epi import chapter_05


@pytest.mark.parametrize('x, expected_parity', [
    (1, 1),
    (2, 1),
    (3, 0),
    (800, 1),
    (801, 0),
])
def test_get_parity(x, expected_parity):
    assert chapter_05.get_parity(x) == expected_parity


@pytest.mark.parametrize('x, i, j, expected_x', [
    # same bit
    (2, 1, 1, 2),
    (2, 0, 1, 1),
    (3, 1, 2, 5),
])
def test_swap_bits(x, i, j, expected_x):
    assert chapter_05.swap_bits(x, i, j) == expected_x


@pytest.mark.parametrize('x, expected_x', [
    (2 ** 64 - 1, 2 ** 64 - 1),
    (2 ** 63, 1),
])
def test_reverse_bits(x, expected_x):
    assert chapter_05.reverse_bits(x) == expected_x


@pytest.mark.parametrize('x, y', [
    (1, 2),
    (47, 55),
])
def test_get_closest(x, y):
    assert chapter_05.get_closest(x) == y


@pytest.mark.parametrize('s, expected_x', [
    ('3', 3),
    ('32', 32),
    ('-32', -32),
    ('0', 0),
])
def test_string_to_int(s, expected_x):
    assert chapter_05.string_to_int(s) == expected_x


@pytest.mark.parametrize('s', [
    'abc',
    '--2',
    '32abc',
    '',
])
def test_string_to_int_failure(s):
    with pytest.raises(ValueError):
        chapter_05.string_to_int(s)


@pytest.mark.parametrize('x, expected_s', [
    (3, '3'),
    (32, '32'),
    (-32, '-32'),
    (0, '0'),
    (100, '100'),
])
def test_int_to_string(x, expected_s):
    assert chapter_05.int_to_string(x) == expected_s


@pytest.mark.parametrize('s,b1,b2,expected_s', [
    ('3', 10, 2, '11'),
    ('-3', 10, 2, '-11'),
    ('17', 10, 16, '11'),
    ('26', 10, 16, '1a'),
    ('ff', 16, 10, '255'),
])
def test_base_conversion(s, b1, b2, expected_s):
    assert chapter_05.base_conversion(s, b1, b2) == expected_s


@pytest.mark.parametrize('s, b1, b2', [
    ('3', 3, 10),
    ('2', 2, 10),
    ('a', 2, 10),
    ('g', 16, 10),
])
def test_base_conversion_failure(s, b1, b2):
    with pytest.raises(ValueError):
        chapter_05.base_conversion(s, b1, b2)


@pytest.mark.parametrize('s, alphabet, expected_column', [
    ('AA', string.ascii_uppercase, 27),
    ('AB', string.ascii_uppercase, 28),
    ('Z', string.ascii_uppercase, 26),
    ('ACB', 'ABC', 20),
])
def test_spreadsheet_column(s, alphabet, expected_column):
    assert chapter_05.spreadsheet_column(s, alphabet) == expected_column
