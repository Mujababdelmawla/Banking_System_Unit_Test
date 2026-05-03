
from user import BankAccount
import pytest
def test_deposit():
    # ARRANGE
    account = BankAccount(owner="mujab", balance=1000000)

    # ACT
    result = account.deposit(2000000)

    # ASSERT
    assert result == 3000000


def test_withdraw():
    # ARRANGE
    account = BankAccount(owner="mujab", balance=1000000)
    
    # ACT
    result = account.withdraw(20000)
    
    # ASSERT
    assert result == 980000


def test_get_balance():
    # ARRANGE 
    account = BankAccount(owner="mujab", balance=1000000)
    # ACT 
    result = account.get_balance()
    # ASSERT
    assert result == 1000000



def test_insufficient_funds():
    # ARRANGE
    account = BankAccount(owner="mujab", balance=500)
    
    # ACT & ASSERT
    with pytest.raises(ValueError):
        account.withdraw(700)  


def test_initial_balance():
    # ARRANGE
    account = BankAccount(owner="mujab", balance=1000000)
    # ACT
    result = account.get_balance()
    # ASSERT
    assert result == 1000000