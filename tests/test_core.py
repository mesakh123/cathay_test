import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目:
# 1. 之後存款1000元, 確認帳戶總金額為1100元
# 2. 接續提款500元, 確認帳戶總金額為600元
# 3. 之後提款700元, 會出現 RuntimeError
#
##########################################################################################
    customer = Customer("Test User","100-1100")
    #init
    def test_zero(self):
        assert self.customer.balance == 0
        self.customer.balance = Decimal(INIT_MONEY)
        assert self.customer.balance == INIT_MONEY

    #1. 之後存款1000元, 確認帳戶總金額為1100元
    def test_one(self):
        self.customer.deposit(1000)
        assert self.customer.balance == 1100

    #2. 接續提款500元, 確認帳戶總金額為600元
    def test_two(self):
        self.customer.withdraw(500)
        assert self.customer.balance == 600


    #3. 之後提款700元, 會出現 RuntimeError
    def test_three(self):
        self.customer.withdraw(700)
        assert self.customer.balance=='balance not enough'
