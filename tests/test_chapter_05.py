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
