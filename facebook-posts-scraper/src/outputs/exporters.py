from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, Protocol

logger = logging.getLogger("exporters")

class Exporter(Protocol):
    def export(self, item: Dict[str, Any]) -> None:  # pragma: no cover - interface
        ...

class JsonLinesExporter:
    """Append each record as a JSON line to the given file."""

    def __init__(self, output_path: Path) -> None:
        self.output_path = output_path

    def export(self, item: Dict[str, Any]) -> None:
        try:
            with self.output_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
            logger.debug("Wrote record to %s", self.output_path)
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to write JSON line to %s: %s", self.output_path, exc)

class StdoutExporter:
    """Pretty-print each record to stdout (useful for demos and debugging)."""

    def export(self, item: Dict[str, Any]) -> None:
        try:
            pretty = json.dumps(item, ensure_ascii=False, indent=2)
            print(pretty)
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to print record: %s", exc)