import sqlite3

def get_popular_skus():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Return SKUs where the SUM of quantity across all orders is > 1.
    query = """
    SELECT sku from Order_Items
    WHERE quantity > 1
    """
    
    cursor.execute(query)
    print(cursor.fetchall())
    return cursor.fetchall()

get_popular_skus()