#!/usr/bin/env python3
# add.py
import sys
from decimal import Decimal

def add(a, b):
    return Decimal(a) + Decimal(b)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: add.py <num1> <num2>", file=sys.stderr)
        sys.exit(1)
    try:
        result = add(sys.argv[1], sys.argv[2])
        # Print only the result so callers can capture it easily
        print(result)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)

