#!/usr/bin/env python3
"""Compatibility entry point; the canonical collector is catalogue_audit.py."""
from catalogue_audit import main

if __name__ == "__main__":
    raise SystemExit(main())
