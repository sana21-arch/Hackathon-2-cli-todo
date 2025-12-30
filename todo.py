#!/usr/bin/env python3
"""Entry point script for the CLI Todo application.

This script can be run directly: python todo.py <command> [args]
"""

import sys
from src.cli.main import main

if __name__ == "__main__":
    sys.exit(main())
