import random

from mcp.server.fastmcp import FastMCP
from starlette.responses import JSONResponse

mcp = FastMCP(host="0.0.0.0", stateless_http=True)

@mcp.tool()
def decide_path() -> str:
    """Decide what the player finds in the path"""
    options = ["nothing", "a treasure chest", "demonic entities"]
    return random.choice(options)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
