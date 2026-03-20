from __future__ import annotations

from dataclasses import dataclass
from typing import List
import requests

from modules.sites import SITES


@dataclass
class SiteResult:
    site: str
    url: str
    found: bool
    status_code: int | None


def check_username(username: str, timeout: int = 6) -> List[SiteResult]:
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "UsernameOSINTTool/1.0",
        }
    )

    results: List[SiteResult] = []

    for site, pattern in SITES.items():
        url = pattern.format(username=username)

        try:
            response = session.get(url, timeout=timeout, allow_redirects=True)

            text = response.text.lower()

            if response.status_code == 200:
                if "not found" in text or "page not found" in text:
                    found = False
                else:
                    found = True
            else:
                found = False

            results.append(
                SiteResult(
                    site=site,
                    url=url,
                    found=found,
                    status_code=response.status_code,
                )
            )

        except requests.RequestException:
            results.append(
                SiteResult(
                    site=site,
                    url=url,
                    found=False,
                    status_code=None,
                )
            )

    return results