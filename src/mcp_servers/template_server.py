"""
MCP Server Template
This is a starter template for creating custom MCP servers.
Copy this file and modify it to create your own MCP server.
"""

from mcp.server import FastMCP
from typing import Dict, List, Any, Optional

# Step 1: Create your MCP server instance with a descriptive name
mcp = FastMCP("My Custom Server")

# Step 2: Define your tools using the @mcp.tool decorator
# Each tool should have:
# - A clear description
# - Type hints for all parameters
# - A docstring explaining what it does
# - Proper error handling

@mcp.tool(description="Example tool that greets a user")
def greet(name: str, formal: bool = False) -> str:
    """
    Greet a user by name.
    
    Args:
        name: The name of the person to greet
        formal: Whether to use formal greeting (default: False)
    
    Returns:
        A greeting message
    """
    if formal:
        return f"Good day, {name}. How may I assist you?"
    else:
        return f"Hello, {name}! Nice to meet you!"

@mcp.tool(description="Example tool that performs a calculation")
def calculate_discount(price: float, discount_percentage: float) -> Dict[str, float]:
    """
    Calculate the discounted price and savings.
    
    Args:
        price: Original price
        discount_percentage: Discount percentage (0-100)
    
    Returns:
        Dictionary with original price, discount amount, and final price
    """
    if price < 0:
        raise ValueError("Price cannot be negative")
    
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    
    return {
        "original_price": price,
        "discount_percentage": discount_percentage,
        "discount_amount": round(discount_amount, 2),
        "final_price": round(final_price, 2)
    }

# Step 3: Add any initialization code here
# This could include:
# - Database connections
# - Loading configuration
# - Setting up external services

def initialize():
    """Initialize any resources your server needs."""
    # Example: Load configuration, connect to database, etc.
    print("Initializing server...")
    # Add your initialization code here
    pass

# Step 4: Add cleanup code if needed
def cleanup():
    """Clean up any resources before shutting down."""
    # Example: Close database connections, save state, etc.
    print("Cleaning up...")
    # Add your cleanup code here
    pass

if __name__ == "__main__":
    # Initialize resources
    initialize()
    
    try:
        # Run the server
        # You can change the transport type:
        # - "stdio" for command-line tools
        # - "sse" for Server-Sent Events
        # - "http" for HTTP transport
        mcp.run(transport="stdio")
    finally:
        # Clean up resources
        cleanup()
