from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    assert count_ocurrences("data/jobs.csv", "Python") == 1639
    assert count_ocurrences("data/jobs.csv", "Javascript") == 122
    with pytest.raises(TypeError):
        count_ocurrences()

    with pytest.raises(TypeError):
        count_ocurrences("word")
