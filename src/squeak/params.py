import bitcoin


class MainParams(bitcoin.MainParams):
    MESSAGE_START = b'\xb4n\x83\xfe'
    DEFAULT_PORT = 8555
    RPC_PORT = 8554
    DNS_SEEDS = ()


class TestNetParams(bitcoin.TestNetParams):
    MESSAGE_START = b'\x9b\xe50\x89'
    DEFAULT_PORT = 18555
    RPC_PORT = 18554
    DNS_SEEDS = ()


class RegTestParams(bitcoin.RegTestParams):
    MESSAGE_START = b'X\x85\xf4\xcb'
    DEFAULT_PORT = 18666
    RPC_PORT = 18665
    DNS_SEEDS = ()


"""Master global setting for what chain params we're using.
However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.params correctly too.
"""
params = MainParams()


def SelectParams(name):
    """Select the chain parameters to use
    name is one of 'mainnet', 'testnet', or 'regtest'
    Default chain is 'mainnet'
    """
    global params
    bitcoin.SelectParams(name)
    if name == 'mainnet':
        params = bitcoin.params = MainParams()
    elif name == 'testnet':
        params = bitcoin.params = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.params = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
