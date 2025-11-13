from __future__ import annotations

import datetime as _dt
from typing import Union

def unix_to_iso(timestamp: Union[int, float]) -> str:
    """Convert a UNIX timestamp (seconds) to an ISO 8601 UTC string."""
    dt = _dt.datetime.utcfromtimestamp(float(timestamp)).replace(
        tzinfo=_dt.timezone.utc
    )
    return dt.isoformat()

def iso_to_unix(iso_str: str) -> int:
    """Convert an ISO 8601 string to a UNIX timestamp (seconds)."""
    # Accept both "Z" and explicit offset forms
    if iso_str.endswith("Z"):
        iso_str = iso_str[:-1] + "+00:00"
    dt = _dt.datetime.fromisoformat(iso_str)
    return int(dt.timestamp())

def current_utc_iso() -> str:
    """Return current time in ISO 8601 UTC format."""
    return _dt.datetime.now(tz=_dt.timezone.utc).isoformat()