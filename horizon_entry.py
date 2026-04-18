"""Horizon deployment entrypoint."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from alpaca_mcp_server.server import build_server

mcp = build_server()

__all__ = ["mcp"]
