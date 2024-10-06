from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    try:
        get_mask_card_number("12345")
    except ValueError as e:
        assert str(e) == "Card number must be 16 digits long."


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("123456") == "**3456"
    try:
        get_mask_account("123")
    except ValueError as e:
        assert str(e) == "Account number must have at least 4 digits."
