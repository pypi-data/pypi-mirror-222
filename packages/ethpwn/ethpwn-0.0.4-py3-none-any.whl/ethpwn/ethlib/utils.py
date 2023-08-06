import functools
from hexbytes import HexBytes
from web3 import Web3

@functools.lru_cache(maxsize=1024)
def normalize_contract_address(address) -> str:
    """Normalize a contract address. This ensures all addresses are checksummed and have the 0x prefix."""
    if not address:
        return None

    if type(address) == str:
        address = "0x" + address.replace("0x", '').zfill(40)

    if Web3.is_checksum_address(address):
        return address

    if type(address) == int:
        address = HexBytes(address.to_bytes(20, 'big'))

    return Web3.to_checksum_address(address)


def get_shared_prefix_len(a, b):
    '''
    Get the length of the shared prefix of two strings.
    '''
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return i
    return min(len(a), len(b))


def to_snake_case(s: str) -> str:
    '''
    Convert a string to snake case.
    '''
    s = s.replace('-', '_')
    return ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_')


def show_diff(a, b, show_old_new=False):
    '''
    Show a nice `rich` table of the diff between two objects using `deepdiff`.
    '''
    from deepdiff import DeepDiff

    from rich import print
    from rich.table import Table

    """Show a diff between two objects"""
    diff = DeepDiff(a, b, ignore_order=True)
    table = Table(title="Diff")
    table.add_column("Type")
    table.add_column("Path")
    table.add_column("Diff")

    if show_old_new:
        table.add_column("Left")
        table.add_column("Right")

    for diff_type, diff_paths in diff.items():
        for diff_path, diff_value in diff_paths.items():
            table.add_row(diff_type, diff_path, diff_value['diff'])
    print(table)


# Enum for the different types of chain
# that are supported by the tool
class ChainName:
    MAINNET = 1
    SEPOLIA = 11155111
    AVALANCHE = 43114


def get_chainid(chain_name):
    '''
    Get the chain id for a given chain name.
    '''
    if chain_name == "mainnet":
        return 1
    elif chain_name == "sepolia":
        return 11155111
    elif chain_name == "avalanche":
        return 43114
    else:
        raise Exception(f"Unknown chain name {chain_name}")


def get_chain_name(id):
    '''
    Get the chain name for a given chain id.
    '''
    if id == 1:
        return "mainnet"
    elif id == 11155111:
        return "sepolia"
    elif id == 43114:
        return "avalanche"
    else:
        raise Exception("Unknown chain id")
