#!/usr/bin/env python3
"""RPF v2.0 manifest schema validator.

Usage: python scripts/validate_manifest_schema.py <path/to/manifest.yaml>
Prints PASS or FAIL with field-level errors to stdout.
Exit code 0 on PASS, 1 on FAIL.
"""

import argparse
import re
import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "schema_version", "run_id", "phase", "config", "seed",
    "hardware", "environment", "data", "tracking", "status",
    "compute", "numerical_sanity",
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an RPF v2.0 manifest.yaml")
    parser.add_argument("manifest", help="Path to the manifest.yaml to validate")
    args = parser.parse_args()

    path = Path(args.manifest)
    if not path.is_file():
        print(f"FAIL: {args.manifest} does not exist or is not a file.")
        return 1

    try:
        import yaml
    except ImportError:
        print("FAIL: PyYAML is required (pip install pyyaml).")
        return 1

    raw_lines = path.read_text(encoding="utf-8").splitlines()

    try:
        with path.open(encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except yaml.YAMLError as exc:
        print(f"FAIL: {args.manifest} is not valid YAML.")
        for line in str(exc).splitlines():
            print(f"  {line}")
        return 1

    if not isinstance(data, dict):
        print("FAIL: manifest root must be a YAML mapping.")
        return 1

    missing = [
        field for field in REQUIRED_FIELDS
        if not any(re.match(rf"^{re.escape(field)}\s*:", line) for line in raw_lines)
    ]

    if missing:
        print(f"FAIL: manifest is missing {len(missing)} mandatory field(s):")
        for field in missing:
            print(f"  - {field}")
        print("Expected: " + ", ".join(REQUIRED_FIELDS))
        return 1

    print(f"PASS: {args.manifest} satisfies the RPF v2.0 manifest schema "
          f"({len(REQUIRED_FIELDS)} mandatory fields present).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
