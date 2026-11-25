import langchain_core
from langchain_core.tools import tool
import sqlite3

@tool
def fetch_product_details(prod_id)->dict:
    
    '''This tool is used to fetch product details from a database given a product_id.
    It will return the current stock level, average daily demand, lead time to procure(in days), 
    and whether there is an active promotion happening.'''

    with sqlite3.connect('my_db.db') as conn:
        cursor=conn.cursor()
        cursor.execute('''select product_id, current_stock, daily_demand, lead_time_days, promotion_active 
                from my_table where product_id=?''',(prod_id,))
        result=cursor.fetchone()
        if result is None:
            return {'message':f'Product {prod_id} not found in the table'}
        else: 
            current_stock, daily_demand, lead_time_days,promotion_active =result[1], result[2], result[3], result[4]
            return {'current_stock': current_stock, 
                    'daily_demand': daily_demand,
                    'lead_time': lead_time_days, 
                    'promotion_active': promotion_active}



