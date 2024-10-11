# tests/test_widget.py
import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("input_data, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected

@pytest.mark.parametrize("input_date, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected
