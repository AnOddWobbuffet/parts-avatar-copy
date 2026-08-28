import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    select email, order_date from Customers
    join Orders on Customers.customer_id=Orders.customer_id
    where Orders.status='Pending'
    """
    
    cursor.execute(query)
    print(cursor.fetchall())

get_pending_customers()
# (1, 'John Doe', 'john@example.com', '2023-01-01'),
# (3, 'Alex Rivard', 'alex@parts.ca', '2024-01-10'),