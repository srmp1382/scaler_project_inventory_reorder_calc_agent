import sqlite3
import pandas as pd
connection=sqlite3.connect('my_db.db')
cursor=connection.cursor()
df=pd.read_csv(r"C:\Users\ASUS\Downloads\inventory_demand_stockout_risk.csv")
df=df[['product_id','current_stock','daily_demand','lead_time_days','promotion_active']]
df.to_sql('my_table', connection, if_exists='replace', index=False)
cursor.execute('select * from my_table where daily_demand>100')
temp_l=[]
for i in cursor.fetchall():
    d={'product_id':i[0],'current_stock':i[1],'daily_demand':i[2], 'lead_time_days':i[3],'promotion_active':i[4]}
    temp_l.append(d)
    

print(temp_l)