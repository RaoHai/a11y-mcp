# #!/usr/bin/env python3

import logging
import os

import click
# Import tools from the tools package
from .tools import mcp

def configure_logging(log_file: str = "a11ymcp.log") -> None:
  from .config import get_logger_path, get_logger_verbosity
  log_dir = get_logger_path()
  os.makedirs(log_dir, exist_ok=True)
  log_path = os.path.join(log_dir, log_file)

  # Get log level from config, with environment variable override
  log_level_str = os.environ.get("DESKAID_DEBUG_LEVEL") or get_logger_verbosity()
  # Map string log level to logging constants
  log_level_map = {
      "DEBUG": logging.DEBUG,
      "INFO": logging.INFO,
      "WARNING": logging.WARNING,
      "ERROR": logging.ERROR,
      "CRITICAL": logging.CRITICAL,
  }
  # Convert string to logging level, default to INFO if invalid
  log_level = log_level_map.get(log_level_str.upper(), logging.INFO)

  # Force DEBUG level if DESKAID_DEBUG is set (for backward compatibility)
  debug_mode = False
  if os.environ.get("DESKAID_DEBUG"):
      log_level = logging.DEBUG
      debug_mode = True

  # Create a root logger
  root_logger = logging.getLogger()
  root_logger.setLevel(log_level)

  # Clear any existing handlers
  if root_logger.hasHandlers():
      root_logger.handlers.clear()

  # Create file handler
  file_handler = logging.FileHandler(log_path)
  file_handler.setLevel(log_level)

  # Create console handler
  console_handler = logging.StreamHandler()
  console_handler.setLevel(log_level)

  # Create formatter and add it to the handlers
  formatter = logging.Formatter(
      "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
  )
  file_handler.setFormatter(formatter)
  console_handler.setFormatter(formatter)

  # Set up filter to exclude logs from 'mcp' module unless in debug mode
  class ModuleFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
      # Allow all logs in debug mode, otherwise filter 'mcp' module
      if debug_mode or not record.name.startswith("mcp"):
          return True
      return False

  module_filter = ModuleFilter()
  file_handler.addFilter(module_filter)
  console_handler.addFilter(module_filter)

  # Add the handlers to the root logger
  root_logger.addHandler(file_handler)
  root_logger.addHandler(console_handler)

  logging.info(f"Logging configured. Log file: {log_path}")
  logging.info(f"Log level set to: {logging.getLevelName(log_level)}")
  if not debug_mode:
      logging.info("Logs from 'mcp' module are being filtered")

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """CodeMCP: Command-line interface for MCP server and project management."""
    # If no subcommand is provided, run the MCP server (for backwards compatibility)
    if ctx.invoked_subcommand is None:
        run()

def run() -> None:
    """Run the MCP server."""
    configure_logging()
    mcp.run()