#!/usr/bin/env python3
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("a11ymcp_multi")

@mcp.tool()
async def a11ymcp() -> None:
  print("Hello, world!")

def main():
  print("hello world")

if __name__ == "__main__":
  main()
