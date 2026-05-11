from seasons import print_minutes
from datetime import date


def test_default_date_print_minutes():
    assert print_minutes("1970-01-01",) == "Twenty-nine million, four hundred eighty-two thousand, five hundred sixty minutes"
    assert print_minutes("1999-01-01",) == "Fourteen million, two hundred thirty thousand eighty minutes"
    assert print_minutes("1998-06-20",) == "Fourteen million, five hundred ten thousand, eight hundred eighty minutes"


def test_today_date_print_minutes():
    assert print_minutes("2022-04-21") == "One million, nine hundred seventy-four thousand, two hundred forty minutes"
    assert print_minutes("2023-4-01") == "One million, four hundred seventy-seven thousand, four hundred forty minutes"