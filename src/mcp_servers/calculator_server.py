"""
Simple Calculator MCP Server
This server provides basic arithmetic operations for demonstration purposes.
"""

from mcp.server import FastMCP

# Create the MCP server instance
mcp = FastMCP("Calculator Server")

@mcp.tool(description="Add two numbers together")
def add(x: float, y: float) -> float:
    """Add two numbers and return the result."""
    return x + y

@mcp.tool(description="Subtract the second number from the first")
def subtract(x: float, y: float) -> float:
    """Subtract y from x and return the result."""
    return x - y

@mcp.tool(description="Multiply two numbers together")
def multiply(x: float, y: float) -> float:
    """Multiply two numbers and return the result."""
    return x * y

@mcp.tool(description="Divide the first number by the second")
def divide(x: float, y: float) -> float:
    """Divide x by y and return the result."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

@mcp.tool(description="Calculate the power of a number")
def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent."""
    return base ** exponent

@mcp.tool(description="Calculate the square root of a number")
def sqrt(x: float) -> float:
    """Calculate the square root of a number."""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return x ** 0.5

if __name__ == "__main__":
    # Run the server
    mcp.run(transport="stdio")
