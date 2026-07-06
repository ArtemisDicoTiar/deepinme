#!/usr/bin/env python3
"""Validate every data/**/items*.json against item-bank.schema.json.

Usage:  python3 data/reference/schema/validate.py
Requires: pip install jsonschema
Exit code 0 = all valid, 1 = failures found.
"""
import json, sys, glob, os
try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("Install the validator first:  pip install jsonschema")

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))   # .../data
SCHEMA = json.load(open(os.path.join(HERE, "item-bank.schema.json")))
Draft202012Validator.check_schema(SCHEMA)
validator = Draft202012Validator(SCHEMA)

files = sorted(glob.glob(os.path.join(DATA_ROOT, "**", "items*.json"), recursive=True))
failures = 0
for f in files:
    rel = os.path.relpath(f, DATA_ROOT)
    j = json.load(open(f))
    errs = sorted(validator.iter_errors(j), key=lambda e: list(e.path))
    count_ok = j.get("count") == len(j.get("items", []))
    if errs or not count_ok:
        failures += 1
        print(f"FAIL  {rel}")
        for e in errs[:10]:
            print(f"      - {'/'.join(map(str, e.path)) or '(root)'}: {e.message}")
        if not count_ok:
            print(f"      - count({j.get('count')}) != items.length({len(j.get('items', []))})")
    else:
        print(f"ok    {rel}  ({j.get('count')} items)")

total = sum(json.load(open(f)).get("count", 0) for f in files)
print(f"\n{len(files)} files, {total} items, {failures} failing.")
sys.exit(1 if failures else 0)
