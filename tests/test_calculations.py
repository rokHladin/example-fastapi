import pytest

from app.calculations import BankAccount, InsufficientFunds, add, divide, multiply, subtract

# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
# pylint: disable=missing-function-docstring


@pytest.fixture
def zero_bank_account():
    return BankAccount(0)


@pytest.fixture
def bank_account():
    return BankAccount(100)


@pytest.mark.parametrize(
    "num1, num2, expected", [(3, 5, 8), (4, 3, 7), (2, 2, 4), (5, 5, 10)]
)
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected


def test_subtract():
    print("testing subtract function")
    assert subtract(9, 4) == 5


def test_multiply():
    print("testing multiply function")
    assert multiply(4, 3) == 12


def test_divide():
    print("testing divide function")
    assert divide(10, 2) == 5


def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 100


def test_bank_default_initial_amount(zero_bank_account):
    assert zero_bank_account.balance == 0


def test_withdraw(bank_account):
    bank_account.withdraw(50)
    assert bank_account.balance == 50


def test_deposit(bank_account):
    bank_account.deposit(50)
    assert bank_account.balance == 150


def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 110


@pytest.mark.parametrize(
    "deposited, withdrew, expected",
    [(200, 50, 150), (100, 50, 50), (0, 0, 0), (100, 100, 0)],
)
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(150)
