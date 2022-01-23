from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

# DECIMALS = 18
# STARTING_PRICE = 2000

DECIMALS = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

ETH_USD = "0x9326BFA02ADD2366b30bacB125260Af641031331"  # (in Kovan)


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"Active network is: {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
        price_feed_address = MockV3Aggregator[-1].address
    print("Mocks Deployed!")


# To test on local ganache UI, add ganache-local network:
# brownie networks add Ethereum ganache-local host=http://127.0.0.1:7545 chainid=5777
# brownie run scripts/deploy.py --network ganache-local
# see: https://ethereum.stackexchange.com/questions/110979/deploying-smartcontract-to-ganache-desktop-instead-of-ganache-cli-with-brownie
