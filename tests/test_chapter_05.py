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
