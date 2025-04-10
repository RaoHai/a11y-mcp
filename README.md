# Accessibility Helper MCP

A powerful accessibility testing and improvement assistant for Claude Desktop, Cursor, and other MCP-supported code agents. This tool helps developers ensure their applications meet accessibility standards and best practices.

## Features

- Automated accessibility testing
- Real-time accessibility analysis
- Smart accessibility improvements
- Integration with popular IDEs and development tools
- Support for multiple accessibility standards (WCAG, etc.)

## Acknowledgments

This project is inspired by and references the excellent work of [codemcp](https://github.com/ezyang/codemcp) by Edward Z. Yang. We would like to express our gratitude for the inspiration and technical insights provided by the codemcp project.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/accessibility-helper-mcp.git
cd accessibility-helper-mcp
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
uv pip install -e .  # Install main dependencies
uv pip install -e ".[dev]"  # Install development dependencies
```

### Configuration

#### For Cursor Integration

Add the following configuration to your MCP settings:
```json
{
  "mcpServers": {
    "a11ymcp": {
      "command": "uvx",
      "args": [
        "--from",
        ".",
        "a11ymcp"
      ]
    }
  }
}
```

## Usage

[Usage instructions and examples will be added here]

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.