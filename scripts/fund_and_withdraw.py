from brownie import FundMe, accounts
from scripts.helpful_script import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"entrance fee: {entrance_fee}")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    withdraw = fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
