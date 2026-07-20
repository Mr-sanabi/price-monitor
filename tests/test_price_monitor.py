import json

import pytest

from src.price_checker import compare_previous_price
from src.price_cleaner import clean_price
from src.storage import load_previous_price, save_json


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("$1,299.50", 1299.5),
        ("€1.299,50", 1299.5),
        ("$1,299", 1299.0),
        ("€1.299", 1299.0),
        ("£51.77", 51.77),
    ],
)
def test_clean_price_formats(raw, expected):
    assert clean_price(raw) == expected


def test_compare_previous_price():
    assert compare_previous_price(90, 100) == (-10, "decreased")


def test_state_round_trip(tmp_path):
    path = tmp_path / "nested" / "current.json"
    save_json(path, {"current_price": 42.5})
    assert load_previous_price(path) == 42.5
    assert not (tmp_path / "nested" / "current.json.tmp").exists()
