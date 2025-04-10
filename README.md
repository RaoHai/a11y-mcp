# accessibility-helper-mcp
 Accessibility Helper Assistant MCP for Claude Desktop, Cursor and Other MCP-Supported Code Agent.

### Bootstrap


#### 创建虚拟环境
```bash
python -m venv .venv
source .venv/bin/activate
```

#### 安装依赖 
```bash
uv pip install -e .  # 安装主要依赖
uv pip install -e ".[dev]"  # 安装开发依赖
```

#### 开发时，如果需要在 cursor 中运行，需要在 mcp 中加入以下配置
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