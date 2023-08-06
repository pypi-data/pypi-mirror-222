"""
Methods to work with tron addresses.
https://stackoverflow.com/questions/57200685/how-to-convert-tron-address-to-different-format
"""
import logging
from typing import Optional

import base58
from rich.console import Console
from rich.text import Text

from trongrid_extractoor.helpers.dict_helper import get_dict_key_by_value
from trongrid_extractoor.helpers.rich_helpers import console

TOKEN_ADDRESSES = {
    'TFczxzPhnThNSqr5by8tvxsdCFRRz6cPNq': 'APENFT',
    'TN3W4H6rK2ce4vX9YnFQHwKENnHjoxb3m9': 'BTCT',   # BTC on Tron (?!)
    'TAFjULxiVgT4qWk6UZwjqwZXTSaGaqnVp4': 'BTT',
    'TMz2SWatiAtZVVcH2ebpsbVtYwUPT9EdjH': 'BUSD',
    'THbVQp8kMjStKNnf2iCY6NEzThKMK5aBHg': 'DOGET',  # DOGEcoin on Tron (?!)
    'TDyvndWuvX5xTBwHPYJi7J3Yq8pq8yh62h': 'HT',     # Huobi Token
    'TNSBA6KvSvMoTqQcEgpVK7VhHT3z7wifxy': 'jUSDC',
    'TCFLL5dx5ZJdKnWuesXxi1VPwjLVmWZZy9': 'JST',
    'TVh1PF9xr4zC5uAqRcCbxF1By6ucp95G4i': 'stUSDT',
    'TSSMHYeV2uE9qYH95DqyoCuNCzEL1NvU3S': 'SUN',
    'TBqsNXUtqaLptVK8AYvdPPctpqd8oBYWUC': 'TCNH',
    'TUpMhErZL2fhh4sVNULAbNKLokS4GjC1F4': 'TUSD',
    'TEkxiTehnzSmSe2XqrBj4w32RUN966rdz8': 'USDC',
    'TPYmHEhy5n8TCEfYGqW2rPxsghSfzghPDn': 'USDD',
    'TMwFHYXLJaRUPeW6421aqXL4ZEzPRFGkGT': 'USDJ',
    'TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t': 'USDT',
    'TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7': 'WIN',
    'TGkxzkDKyMeq2T7edKnyjZoFypyzjkkssq': 'wstUSDT',
    'TNUC9Qb1rRpS5CbWLmNMxXBjyFoydXjWFR': 'WTRX',
}


def symbol_for_address(address: str) -> Optional[str]:
    return TOKEN_ADDRESSES.get(address)


def hex_to_tron(address: str) -> str:
    """Convert a hex address to the more commonly used Txxxxxxxxx base58 style."""
    if address.startswith('0x'):
        address = '41' + address[2:]

    if len(address) % 2 == 1:
        address = '0' + address

    return base58.b58encode_check(bytes.fromhex(address)).decode()


def tron_to_hex(address: str) -> str:
    """Convert a Tron base58 address to a hexadecimal string."""
    return base58.b58decode_check(address).hex()


def is_contract_address(address: str) -> bool:
    """Returns true if it looks like a Tron contract address."""
    if not isinstance(address, str):
        return False

    return address[0] == 'T' and len(address) == 34


def address_of_symbol(symbol: str) -> Optional[str]:
    try:
        return get_dict_key_by_value(TOKEN_ADDRESSES, symbol)
    except ValueError:
        logging.warning(f"No address found for '{symbol}'!")


def print_symbol_addresses() -> None:
    for symbol, address in TOKEN_ADDRESSES.items():
        txt = Text('').append(symbol, style='cyan').append('    ').append(address, style='magenta')
        console.print(txt)
