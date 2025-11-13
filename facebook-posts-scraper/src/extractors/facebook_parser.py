from __future__ import annotations

import hashlib
import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from bs4 import BeautifulSoup

from extractors.utils_time import current_utc_iso, unix_to_iso

logger = logging.getLogger("facebook_parser")

class FacebookPostScraper:
    """
    Scraper for Facebook post-level + comment-level data.

    Two operating modes:

    - sample mode: loads deterministic data from a local JSON file.
    - live mode:   fetches the page via HTTP and extracts basic metadata
                   (title, description, image) as a fallback when there is
                   no local sample record.
    """

    def __init__(
        self,
        sample_mode: bool = False,
        sample_file: Optional[Path] = None,
        max_comments: int = 100,
        request_timeout: int = 15,
        user_agent: str = "facebook-posts-scraper/1.0",
    ) -> None:
        self.sample_mode = sample_mode
        self.sample_file = sample_file
        self.max_comments = max_comments
        self.request_timeout = request_timeout
        self.user_agent = user_agent

        self._sample_cache: Optional[List[Dict[str, Any]]] = None
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": self.user_agent})

    # --------------------------------------------------------------------- #
    # Public API
    # --------------------------------------------------------------------- #
    def scrape(self, url: str) -> Dict[str, Any]:
        """
        Scrape a single Facebook post URL.

        In sample mode we return a record from the local sample file.
        In live mode we fetch HTML and build a structured record from
        OpenGraph tags and minimal fallback data.
        """
        if self.sample_mode and self.sample_file is not None:
            logger.debug("Using sample data from %s", self.sample_file)
            return self._from_sample(url)

        logger.debug("Using live HTTP scraping for %s", url)
        return self._from_live(url)

    # --------------------------------------------------------------------- #
    # Sample-mode helpers
    # --------------------------------------------------------------------- #
    def _load_sample_cache(self) -> List[Dict[str, Any]]:
        if self._sample_cache is not None:
            return self._sample_cache

        if self.sample_file is None or not self.sample_file.is_file():
            raise FileNotFoundError(f"Sample file not found: {self.sample_file}")

        with self.sample_file.open("r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Sample JSON must contain a list of records")

        self._sample_cache = data
        return self._sample_cache

    def _from_sample(self, url: str) -> Dict[str, Any]:
        records = self._load_sample_cache()
        for record in records:
            if record.get("input") == url:
                enriched = self._enrich_record(record)
                logger.info("Loaded sample record for %s", url)
                return enriched

        raise ValueError(f"No sample record found for URL: {url}")

    # --------------------------------------------------------------------- #
    # Live-mode helpers
    # --------------------------------------------------------------------- #
    def _from_live(self, url: str) -> Dict[str, Any]:
        try:
            resp = self._session.get(url, timeout=self.request_timeout)
            resp.raise_for_status()
        except Exception as exc:  # noqa: BLE001
            logger.error("HTTP error while fetching %s: %s", url, exc)
            return self._build_error_record(url, str(exc))

        soup = BeautifulSoup(resp.text, "html.parser")

        title = None
        title_meta = soup.find("meta", property="og:title")
        if title_meta is not None:
            title = title_meta.get("content")

        if not title and soup.title:
            title = soup.title.string or None

        desc = None
        desc_meta = soup.find("meta", property="og:description")
        if desc_meta is not None:
            desc = desc_meta.get("content")

        image_url = None
        image_meta = soup.find("meta", property="og:image")
        if image_meta is not None:
            image_url = image_meta.get("content")

        now_ts = int(time.time())
        digest = hashlib.md5(url.encode("utf-8")).hexdigest()

        record: Dict[str, Any] = {
            "input": url,
            "author": None,
            "post_id": digest[:12],
            "action_id": digest,
            "text": desc or title or "",
            "create_time": now_ts,
            "create_time_iso": unix_to_iso(now_ts),
            "post_url": url,
            "like_count": 0,
            "comment_count": 0,
            "share_count": 0,
            "view_count": 0,
            "play_count": 0,
            "image_list": [image_url] if image_url else [],
            "video_list": [],
            "author_username": None,
            "author_user_id": None,
            "comments": [],
            "scraped_at": current_utc_iso(),
            "source": "live",
        }

        logger.info("Scraped basic metadata for %s", url)
        return record

    # --------------------------------------------------------------------- #
    # Utilities
    # --------------------------------------------------------------------- #
    def _enrich_record(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Ensure a sample record has all helper fields and is trimmed."""
        enriched = dict(record)  # shallow copy

        ct = enriched.get("create_time")
        if isinstance(ct, (int, float)):
            enriched.setdefault("create_time_iso", unix_to_iso(ct))

        enriched.setdefault("scraped_at", current_utc_iso())
        enriched.setdefault("source", "sample")

        comments = enriched.get("comments")
        if isinstance(comments, list) and self.max_comments is not None:
            enriched["comments"] = comments[: self.max_comments]

        return enriched

    def _build_error_record(self, url: str, error_message: str) -> Dict[str, Any]:
        """Return a structured error record so callers can handle failures."""
        now_ts = int(time.time())
        return {
            "input": url,
            "author": None,
            "post_id": None,
            "action_id": None,
            "text": "",
            "create_time": now_ts,
            "create_time_iso": unix_to_iso(now_ts),
            "post_url": url,
            "like_count": 0,
            "comment_count": 0,
            "share_count": 0,
            "view_count": 0,
            "play_count": 0,
            "image_list": [],
            "video_list": [],
            "author_username": None,
            "author_user_id": None,
            "comments": [],
            "scraped_at": current_utc_iso(),
            "source": "error",
            "error": error_message,
        }