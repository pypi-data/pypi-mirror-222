import csv
import re
from dataclasses import dataclass, field, asdict, fields
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pendulum

from trongrid_extractoor.config import log
from trongrid_extractoor.helpers.address_helpers import *
from trongrid_extractoor.trc20_txn import Trc20Txn

WRITTEN = 'written'
WRITTEN_AT_REGEX = re.compile(WRITTEN + "_(\\d{4}-\\d{2}-\\d{2}T\\d{2}[.:]\\d{2}[.:]\\d{2})\\.csv")


def write_rows(file_path: Union[str, Path], rows: List[Trc20Txn], _klass = Trc20Txn) -> None:
    log.info(f"Writing {len(rows)} rows...")
    _fields = [fld.name for fld in fields(_klass)]

    if Path(file_path).exists():
        file_mode = 'a'
    else:
        file_mode = 'w'

    with open(file_path, file_mode) as f:
        csv_writer = csv.DictWriter(f, _fields)

        if file_mode == 'w':
            csv_writer.writeheader()

        # Put this after the header is written so there is always an output file
        if len(rows) == 0:
            log.warning(f"No rows to write!")
            return

        csv_writer.writerows([asdict(row) for row in rows])


def output_csv_path(address: str, dir: Optional[Path] = None, suffix: Optional[str] = None) -> Path:
    """Build a filename that contains the address and (if available) the symbol."""
    dir = dir or Path('')
    filename = csv_prefix(address)

    if suffix:
        filename += f"{suffix}_"

    filename += csv_suffix()
    return dir.joinpath(filename.replace(':', '.').replace('/', '.'))


def load_csv(csv_path: Union[str, Path]) -> List[Dict[str, Any]]:
    with open(Path(csv_path), mode='r') as csvfile:
        return [
            row
            for row in csv.DictReader(csvfile, delimiter=',')
        ]


def csvs_with_prefix_in_dir(dir: Union[str, Path], prefix: str) -> List[str]:
    return [f.name for f in Path(dir).glob(f"{prefix}*.csv")]


def csv_prefix(address: str) -> str:
    filename = 'events_'

    if is_contract_address(address):
        symbol = symbol_for_address(address)
    else:
        symbol = address
        address = address_of_symbol(address)

        if not address:
            raise ValueError(f"No address found for {symbol}!")

    if symbol:
        filename += f"{symbol}_"

    filename += f"{address}_"
    return filename


def csv_suffix() -> str:
    """String showing the time the file was created."""
    return f"{WRITTEN}_{datetime.now().strftime('%Y-%m-%dT%H.%M.%S')}.csv"


def parse_written_at_from_filename(csv_path: Union[str, Path]) -> pendulum.DateTime:
    """Extract the written timestmap (output of csv_suffix()) to a timestamp."""
    match = WRITTEN_AT_REGEX.search(str(csv_path))

    if match is None:
        raise ValueError(f"'{csv_path}' does not seem to have an embedded written_at timestamp!")

    return pendulum.parse(match.group(1).replace('.', ':'))
