from unittest import mock

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


@mock.patch("builtins.input", return_value="yes")
def test_reset_transaction_yes(mock_input):
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.reset_transaction()
    assert len(t.item_list) == 0


@mock.patch("builtins.input", return_value="no")
def test_reset_transaction_no(mock_input):
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    t.reset_transaction()
    assert len(t.item_list) == 1


def test_check_order_valid(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 10000)
    # KNOWN QUIRK: __str__ initializes derived attributes used by validation.
    str(t)
    t.check_order()
    captured = capsys.readouterr()
    assert "Order is correct" in captured.out


def test_check_order_invalid_qty(capsys):
    t = Transaction()
    t.add_item("Apple", "two", 10000)
    # KNOWN QUIRK: __str__ initializes derived attributes used by validation.
    str(t)
    t.check_order()
    captured = capsys.readouterr()
    assert "There is a data input error" in captured.out


def test_check_order_invalid_price(capsys):
    t = Transaction()
    t.add_item("Apple", 2, "ten thousand")
    # KNOWN QUIRK: __str__ initializes derived attributes used by validation.
    str(t)
    t.check_order()
    captured = capsys.readouterr()
    assert "There is a data input error" in captured.out


def test_total_price_no_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 50000)  # Total: 100,000
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    assert "Total : 100000" in captured.out
    assert "The total amount to be paid is: Rp 100000" in captured.out


def test_total_price_200k_boundary_no_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 100000)  # Total: 200,000
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    assert "Total : 200000" in captured.out
    assert "The total amount to be paid is: Rp 200000" in captured.out


def test_total_price_5_percent_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 125000)  # Total: 250,000
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    assert "Total : 250000" in captured.out
    assert "Discount : 5%" in captured.out
    assert "The total amount to be paid is: Rp 237500.0" in captured.out


def test_total_price_300k_boundary_uses_5_percent(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 150000)  # Total: 300,000
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    assert "Total : 300000" in captured.out
    assert "Discount : 5%" in captured.out
    assert "The total amount to be paid is: Rp 285000.0" in captured.out


def test_total_price_8_percent_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 4, 100000)  # Total: 400,000
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    assert "Total : 400000" in captured.out
    assert "Discount : 8%" in captured.out
    assert "The total amount to be paid is: Rp 368000.0" in captured.out


def test_total_price_500k_boundary_uses_8_percent(capsys):
    t = Transaction()
    t.add_item("Apple", 5, 100000)  # Total: 500,000
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    assert "Total : 500000" in captured.out
    assert "Discount : 8%" in captured.out
    assert "The total amount to be paid is: Rp 460000.0" in captured.out


def test_total_price_10_percent_discount(capsys):
    t = Transaction()
    t.add_item("Apple", 2, 300000)  # Total: 600,000
    str(t)
    t.total_price()
    captured = capsys.readouterr()
    assert "Total : 600000" in captured.out
    assert "Discount : 10%" in captured.out
    assert "The total amount to be paid is: Rp 540000.0" in captured.out
