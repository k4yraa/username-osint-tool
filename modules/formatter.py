from __future__ import annotations

from typing import List

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from modules.checker import SiteResult

console = Console()


def print_banner() -> None:
    console.print(
        Panel.fit(
            "[bold]Username OSINT Tool[/bold]\nPublic profile presence checker",
            border_style="cyan",
        )
    )


def print_results(username: str, results: List[SiteResult]) -> None:
    table = Table(title=f"Results for: {username}")
    table.add_column("Site", style="cyan", no_wrap=True)
    table.add_column("Found", style="white")
    table.add_column("Status", style="white")
    table.add_column("URL", style="white")

    for item in results:
        table.add_row(
            item.site,
            "Yes" if item.found else "No",
            str(item.status_code) if item.status_code is not None else "Error",
            item.url,
        )

    console.print(table)