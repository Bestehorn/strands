"""
E-commerce Database MCP Server
This server provides database operations for an e-commerce system using SQLite.
"""

from mcp.server import FastMCP
import sqlite3
import json
from typing import List, Dict, Any, Optional
from datetime import datetime

# Create the MCP server instance
mcp = FastMCP("E-commerce Database Server")

# Global connection (will be initialized when server starts)
conn = None

def initialize_database():
    """Initialize the in-memory database with e-commerce schema and sample data."""
    global conn
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row  # Enable column access by name
    
    # Create tables
    conn.executescript('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            stock INTEGER DEFAULT 0,
            category TEXT NOT NULL
        );
        
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date TEXT DEFAULT CURRENT_TIMESTAMP,
            total_amount REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        );
        
        CREATE TABLE order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders (id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        );
    ''')
    
    # Insert sample products
    products = [
        ('Laptop Pro 15"', 'High-performance laptop with 16GB RAM', 1299.99, 10, 'Electronics'),
        ('Wireless Mouse', 'Ergonomic wireless mouse with USB receiver', 29.99, 50, 'Electronics'),
        ('Mechanical Keyboard', 'RGB mechanical keyboard with blue switches', 89.99, 25, 'Electronics'),
        ('USB-C Hub', '7-in-1 USB-C hub with HDMI and card reader', 49.99, 30, 'Electronics'),
        ('Standing Desk', 'Electric height-adjustable standing desk', 399.99, 5, 'Furniture'),
        ('Ergonomic Chair', 'Mesh back office chair with lumbar support', 299.99, 8, 'Furniture'),
        ('Notebook Set', 'Pack of 3 premium notebooks', 19.99, 100, 'Stationery'),
        ('Premium Coffee Beans', 'Single-origin arabica coffee beans 1kg', 24.99, 40, 'Food & Drink'),
        ('Thermal Mug', 'Insulated stainless steel travel mug', 19.99, 60, 'Food & Drink'),
        ('Desk Lamp', 'LED desk lamp with adjustable brightness', 39.99, 20, 'Furniture')
    ]
    
    conn.executemany('INSERT INTO products (name, description, price, stock, category) VALUES (?, ?, ?, ?, ?)', products)
    
    # Insert sample customers
    customers = [
        ('Alice Johnson', 'alice@example.com'),
        ('Bob Smith', 'bob@example.com'),
        ('Charlie Brown', 'charlie@example.com'),
        ('Diana Prince', 'diana@example.com')
    ]
    
    conn.executemany('INSERT INTO customers (name, email) VALUES (?, ?)', customers)
    
    # Insert sample orders
    conn.execute('INSERT INTO orders (customer_id, total_amount, status) VALUES (1, 1329.98, "completed")')
    conn.execute('INSERT INTO orders (customer_id, total_amount, status) VALUES (2, 119.98, "completed")')
    conn.execute('INSERT INTO orders (customer_id, total_amount, status) VALUES (3, 39.98, "pending")')
    
    # Insert sample order items
    order_items = [
        (1, 1, 1, 1299.99),  # Order 1: 1 Laptop
        (1, 2, 1, 29.99),    # Order 1: 1 Mouse
        (2, 3, 1, 89.99),    # Order 2: 1 Keyboard
        (2, 2, 1, 29.99),    # Order 2: 1 Mouse
        (3, 7, 2, 19.99)     # Order 3: 2 Notebook Sets
    ]
    
    conn.executemany('INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)', order_items)
    conn.commit()

# Tool definitions

@mcp.tool(description="Search for products by name or category")
def search_products(query: str = "", category: Optional[str] = None) -> List[Dict[str, Any]]:
    """Search products by name or filter by category."""
    if not conn:
        initialize_database()
    
    if category:
        cursor = conn.execute(
            "SELECT * FROM products WHERE category = ? AND name LIKE ?",
            (category, f"%{query}%")
        )
    else:
        cursor = conn.execute(
            "SELECT * FROM products WHERE name LIKE ? OR description LIKE ?",
            (f"%{query}%", f"%{query}%")
        )
    
    return [dict(row) for row in cursor.fetchall()]

@mcp.tool(description="Get product details by ID")
def get_product(product_id: int) -> Optional[Dict[str, Any]]:
    """Get detailed information about a specific product."""
    if not conn:
        initialize_database()
    
    cursor = conn.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    return dict(row) if row else None

@mcp.tool(description="Get customer information by email")
def get_customer(email: str) -> Optional[Dict[str, Any]]:
    """Get customer details by email address."""
    if not conn:
        initialize_database()
    
    cursor = conn.execute("SELECT * FROM customers WHERE email = ?", (email,))
    row = cursor.fetchone()
    return dict(row) if row else None

@mcp.tool(description="Get order history for a customer")
def get_customer_orders(customer_id: int) -> List[Dict[str, Any]]:
    """Get all orders for a specific customer."""
    if not conn:
        initialize_database()
    
    cursor = conn.execute("""
        SELECT o.*, c.name as customer_name, c.email
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        WHERE o.customer_id = ?
        ORDER BY o.order_date DESC
    """, (customer_id,))
    
    return [dict(row) for row in cursor.fetchall()]

@mcp.tool(description="Get order details including items")
def get_order_details(order_id: int) -> Optional[Dict[str, Any]]:
    """Get complete order information including all items."""
    if not conn:
        initialize_database()
    
    # Get order info
    cursor = conn.execute("""
        SELECT o.*, c.name as customer_name, c.email
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        WHERE o.id = ?
    """, (order_id,))
    
    order = cursor.fetchone()
    if not order:
        return None
    
    order_dict = dict(order)
    
    # Get order items
    cursor = conn.execute("""
        SELECT oi.*, p.name as product_name, p.category
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        WHERE oi.order_id = ?
    """, (order_id,))
    
    order_dict['items'] = [dict(row) for row in cursor.fetchall()]
    
    return order_dict

@mcp.tool(description="Get sales statistics by category")
def get_sales_by_category() -> List[Dict[str, Any]]:
    """Get total sales amount and quantity by product category."""
    if not conn:
        initialize_database()
    
    cursor = conn.execute("""
        SELECT 
            p.category,
            COUNT(DISTINCT oi.order_id) as total_orders,
            SUM(oi.quantity) as total_quantity,
            SUM(oi.quantity * oi.price) as total_revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        JOIN orders o ON oi.order_id = o.id
        WHERE o.status = 'completed'
        GROUP BY p.category
        ORDER BY total_revenue DESC
    """)
    
    return [dict(row) for row in cursor.fetchall()]

@mcp.tool(description="Check product availability")
def check_stock(product_id: int) -> Dict[str, Any]:
    """Check if a product is in stock and return availability info."""
    if not conn:
        initialize_database()
    
    cursor = conn.execute(
        "SELECT id, name, stock, price FROM products WHERE id = ?", 
        (product_id,)
    )
    row = cursor.fetchone()
    
    if not row:
        return {"available": False, "error": "Product not found"}
    
    product = dict(row)
    product['available'] = product['stock'] > 0
    return product

@mcp.tool(description="Update product stock level")
def update_stock(product_id: int, quantity_change: int) -> Dict[str, Any]:
    """Update product stock. Use negative values to decrease stock."""
    if not conn:
        initialize_database()
    
    # Get current stock
    cursor = conn.execute("SELECT stock FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    
    if not row:
        return {"success": False, "error": "Product not found"}
    
    current_stock = row[0]
    new_stock = current_stock + quantity_change
    
    if new_stock < 0:
        return {"success": False, "error": "Insufficient stock"}
    
    conn.execute(
        "UPDATE products SET stock = ? WHERE id = ?",
        (new_stock, product_id)
    )
    conn.commit()
    
    return {
        "success": True,
        "product_id": product_id,
        "previous_stock": current_stock,
        "new_stock": new_stock
    }

@mcp.tool(description="Get database statistics")
def get_database_stats() -> Dict[str, Any]:
    """Get overall statistics about the e-commerce database."""
    if not conn:
        initialize_database()
    
    stats = {}
    
    # Count records in each table
    for table in ['products', 'customers', 'orders', 'order_items']:
        cursor = conn.execute(f"SELECT COUNT(*) FROM {table}")
        stats[f'total_{table}'] = cursor.fetchone()[0]
    
    # Get additional stats
    cursor = conn.execute("SELECT COUNT(DISTINCT category) FROM products")
    stats['total_categories'] = cursor.fetchone()[0]
    
    cursor = conn.execute("SELECT SUM(total_amount) FROM orders WHERE status = 'completed'")
    stats['total_revenue'] = cursor.fetchone()[0] or 0.0
    
    return stats

if __name__ == "__main__":
    # Initialize database on startup
    initialize_database()
    # Run the server
    mcp.run(transport="stdio")
