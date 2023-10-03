from src.scripts import *
import datetime

filename = "src/operations.json"
extracted_file = extract_operations_list(filename)
filtered_file = filter_executed(extracted_file)
sorted_file = sort_for_date(filtered_file)
maked_card_number = make_card_number(filtered_file[0]["from"])


def test_extract_operations_list():
    assert extract_operations_list(filename)[0]["id"] == 441945886

def test_filter_executed():
    assert filter_executed(extracted_file)[12]["id"] == 147815167

def test_sort_for_date():
    assert sorted_file[1]["date"] > sorted_file[2]["date"]

def test_make_card_number():
    assert maked_card_number[-6:-4] == "* "



def test_make_date():
    assert make_date(sorted_file[0]["date"]) == "08.12.2019"


def test_comb_text():
    assert comb_text(sorted_file[0]) == """08.12.2019 Открытие вклада\n -> Счет ****************5907\n41096.24 USD"""