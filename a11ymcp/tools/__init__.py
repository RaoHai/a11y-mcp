"""Tools for accessibility testing and improvements."""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("a11ymcp")

# Import and re-export all tools
from .check import check_accessibility
from .fix import fix_accessibility
from .analyze import analyze_accessibility

# Define what should be exported
__all__ = ['mcp', 'check_accessibility', 'fix_accessibility', 'analyze_accessibility'] 