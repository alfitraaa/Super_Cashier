import pytest
from unittest import mock
import sys
import io
from super_cashier import Transaction

def test_add_item():
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    assert t.item_list == {"Apple": [2, 10000]}

def test_update_item_name():
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.update_item_name("Apple", "Banana")
    assert "Apple" not in t.item_list
    assert t.item_list["Banana"] == [2, 10000]

def test_update_item_qty():
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.update_item_qty("Apple", 5)
    assert t.item_list["Apple"][0] == 5

def test_update_item_price():
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.update_item_price("Apple", 15000)
    assert t.item_list["Apple"][1] == 15000

def test_delete_item():
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.add_item("Banana", 3, 5000)
    t.delete_item("Apple")
    assert "Apple" not in t.item_list
    assert "Banana" in t.item_list

@mock.patch('builtins.input', return_value='yes')
def test_reset_transaction_yes(mock_input):
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.reset_transaction()
    assert len(t.item_list) == 0

@mock.patch('builtins.input', return_value='no')
def test_reset_transaction_no(mock_input):
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.reset_transaction()
    assert len(t.item_list) == 1

def test_check_order_valid(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    # KNOWN QUIRK: Must call __str__ to initialize derived attributes
    str(t)
    t.check_order()
    captured = capsys.readouterr()
    assert "Order is correct" in captured.out

def test_check_order_invalid_qty(capsys):
    t = Transaction()
    t.add_item("Apple", "two", 10000)
    # KNOWN QUIRK: Must call __str__ to initialize derived attributes
    str(t)
    t.check_order()
    captured = capsys.readouterr()
    assert "There is a data input error" in captured.out

def test_check_order_invalid_price(capsys):
    t = Transaction()
    t.add_item("Apple", 2, "ten thousand")
    # KNOWN QUIRK: Must call __str__ to initialize derived attributes
    str(t)
    t.check_order()
    captured = capsys.readouterr()
    assert "There is a data input error" in captured.out

@pytest.mark.xfail(strict=True, reason="Defect: UnboundLocalError raised during elif check for 10% discount when grand_total_price > 500k since it evaluates 500k > 300k using local grand_total_price")
def test_total_price_no_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 50000) # Total: 100,000
    # KNOWN QUIRK: Must call __str__ to initialize derived attributes
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    # Fails because grand_total_price local variable is referenced in the 8% condition check,
    # causing an UnboundLocalError and triggering the except block, hiding the correct behavior
    assert "Total : 100000" in captured.out
    assert "The total amount to be paid is: Rp 100000" in captured.out

def test_total_price_5_percent_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 125000) # Total: 250,000
    # KNOWN QUIRK: Must call __str__ to initialize derived attributes
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    # Passes because the 5% condition is met FIRST, so it doesn't evaluate the 8% condition where the bug is
    assert "Total : 250000" in captured.out
    assert "Discount : 5%" in captured.out
    assert "The total amount to be paid is: Rp 237500.0" in captured.out

@pytest.mark.xfail(strict=True, reason="Defect: UnboundLocalError raised during elif check since it evaluates 8% branch using local grand_total_price before reaching 10% branch")
def test_total_price_10_percent_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 300000) # Total: 600,000
    # KNOWN QUIRK: Must call __str__ to initialize derived attributes
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    # Fails because it hits the 8% check before the 10% check, and crashes due to the UnboundLocalError
    assert "Total : 600000" in captured.out
    assert "Discount : 10%" in captured.out
    assert "The total amount to be paid is: Rp 540000.0" in captured.out

@pytest.mark.xfail(strict=True, reason="Defect: UnboundLocalError in 8% discount branch due to referencing local grand_total_price instead of self.grand_total_price")
def test_total_price_8_percent_discount_defect(capsys):
    t = Transaction()
    t.add_item("Apple", 4, 100000) # Total: 400,000
    # KNOWN QUIRK: Must call __str__ to initialize derived attributes
    str(t)

    # In the original source code, the 8% discount logic catches ANY exception inside the try block
    # and prints "There is a data input error", effectively swallowing the UnboundLocalError.
    # Therefore, the function will not crash, but it will output the error message instead of calculating the total.
    t.total_price()
    captured = capsys.readouterr()

    # If the bug is fixed, we would expect "Discount : 8%" and "The total amount to be paid is: Rp 368000.0"
    # To fail strictly while the bug exists, we assert the fixed behavior, which will fail.
    assert "Discount : 8%" in captured.out
