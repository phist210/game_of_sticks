from stick_ai import choice_error


def test_choice():
    assert choice_error(2) is True


def test_choice_error():
    assert choice_error(6) is not True
