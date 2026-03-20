from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict

from modules.checker import check_username
from modules.formatter import print_banner, print_results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check public profile presence for a username across selected websites."
    )
    parser.add_argument("username", help="Username to check")
    parser.add_argument("--timeout", type=int, default=6, help="Request timeout in seconds")
    parser.add_argument("--json", dest="json_output", action="store_true", help="Print JSON output")
    args = parser.parse_args()

    print_banner()
    results = check_username(args.username, timeout=args.timeout)

    if args.json_output:
        print(json.dumps([asdict(r) for r in results], indent=2))
    else:
        print_results(args.username, results)

    return 0


if __name__ == "__main__":
    sys.exit(main())