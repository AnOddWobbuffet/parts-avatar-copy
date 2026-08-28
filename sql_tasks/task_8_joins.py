import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    SELECT name, SUM(Order_Items.price * Order_Items.quantity) AS total_spend from Customers
    JOIN Orders on Customers.customer_id = Orders.customer_id
    JOIN Order_Items on Order_Items.order_id = Orders.order_id
    GROUP BY name
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    print(results)
    return results

get_customer_spend()