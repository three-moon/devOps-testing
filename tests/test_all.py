import pytest
from src.main import hello, negative


@pytest.fixture
def test_hello():
    assert hello() == "Hello world!"


@pytest.mark.parametrize(
    ('n', 'result'), [
        (1, -1),
        (-5, 5),
        (0, 0),
    ]
)
def test_negative(n, result):
    assert negative(n) == result
