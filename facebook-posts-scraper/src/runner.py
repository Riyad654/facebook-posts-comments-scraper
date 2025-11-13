import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List

# Resolve project paths
CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[1]
SRC_ROOT = PROJECT_ROOT / "src"

# Ensure src/ is on sys.path so we can import internal packages
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from extractors.facebook_parser import FacebookPostScraper  # type: ignore  # noqa: E402
from outputs.exporters import JsonLinesExporter, StdoutExporter  # type: ignore  # noqa: E402

def load_config() -> Dict[str, Any]:
    """Load configuration from settings.example.json with safe defaults."""
    config_path = SRC_ROOT / "config" / "settings.example.json"
    if not config_path.is_file():
        raise FileNotFoundError(f"Config file not found at {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        user_cfg = json.load(f)

    defaults: Dict[str, Any] = {
        "mode": "sample",  # "sample" or "live"
        "sample_file": "data/sample.json",
        "output_path": "data/output.jsonl",
        "max_comments": 100,
        "log_level": "INFO",
        "request_timeout": 15,
        "user_agent": "facebook-posts-scraper/1.0",
    }

    cfg = {**defaults, **(user_cfg or {})}
    return cfg

def load_inputs(input_file: Path) -> List[str]:
    """Load Facebook post URLs from a simple text file."""
    if not input_file.is_file():
        raise FileNotFoundError(f"Input file not found at {input_file}")

    urls: List[str] = []
    with input_file.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            urls.append(line)
    return urls

def setup_logging(level_name: str) -> None:
    """Configure root logger."""
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

def main() -> None:
    config = load_config()
    setup_logging(config.get("log_level", "INFO"))
    logger = logging.getLogger("runner")

    input_file = PROJECT_ROOT / "data" / "inputs.sample.txt"
    urls = load_inputs(input_file)

    if not urls:
        logger.warning("No URLs found in %s", input_file)
        return

    output_path = PROJECT_ROOT / config.get("output_path", "data/output.jsonl")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    scraper = FacebookPostScraper(
        sample_mode=(config.get("mode", "sample") == "sample"),
        sample_file=PROJECT_ROOT / str(config.get("sample_file", "data/sample.json")),
        max_comments=int(config.get("max_comments", 100)),
        request_timeout=int(config.get("request_timeout", 15)),
        user_agent=str(config.get("user_agent", "facebook-posts-scraper/1.0")),
    )

    exporters = [
        JsonLinesExporter(output_path),
        StdoutExporter(),
    ]

    logger.info("Starting scrape for %d URL(s)", len(urls))
    success_count = 0

    for url in urls:
        try:
            logger.info("Scraping %s", url)
            record = scraper.scrape(url)
            for exporter in exporters:
                exporter.export(record)
            success_count += 1
        except Exception as exc:  # noqa: BLE001
            logger.exception("Failed to scrape %s: %s", url, exc)

    logger.info(
        "Finished. Successfully scraped %d/%d URL(s).",
        success_count,
        len(urls),
    )

if __name__ == "__main__":
    main()