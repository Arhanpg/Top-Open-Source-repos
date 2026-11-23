#!/usr/bin/env python3
"""Load the compressed, tested public repository catalogue auditor."""
from __future__ import annotations
import base64
import gzip
from pathlib import Path

payload_path = Path(__file__).with_name("catalogue_audit.py.gz.b64")
source = gzip.decompress(base64.b64decode(payload_path.read_text(encoding="ascii").strip())).decode("utf-8")
exec(compile(source, "catalogue_audit_implementation.py", "exec"), globals(), globals())
