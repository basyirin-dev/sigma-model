#!/usr/bin/env python3
"""Backward-compatible thin wrapper — delegates to sigma.monitoring.pub."""

from sigma.monitoring.pub import main

if __name__ == "__main__":
    main()
