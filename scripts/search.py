#!/usr/bin/env python3
r"""
Compatibility wrapper.

The primary generator entry point has been renamed to generate.py to better
reflect that it orchestrates reasoning plus artifact rendering.
"""

from __future__ import annotations

from generate import main


if __name__ == "__main__":
    raise SystemExit(main())
