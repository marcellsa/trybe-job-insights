import pytest
from src.pre_built.counter import count_ocurrences


@pytest.fixture
def jobs_stock():
    return "data/jobs.csv"


def test_counter(jobs_stock):
    report = count_ocurrences(jobs_stock, "Python")
    assert report == 1639
