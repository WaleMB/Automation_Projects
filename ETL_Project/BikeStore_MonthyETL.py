import pyodbc
import pandas as pd
from datetime import datetime

# DB config
server = 'localhost\\SQLEXPRESS'
database = 'BikeStores'

# Connect
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
    "Connection Timeout=30;"
)
conn = pyodbc.connect(conn_str)

# SQL with JOINs
sql_query = """select o.order_id, concat(c.first_name,'',c.last_name) as name, c.city, c.state, o.order_date,
sum(oi.quantity) as total_units,
sum(oi.quantity * oi.list_price) as revenue,
pd.product_name,
ct.category_name,
st.store_name,
concat(stf.first_name,'',stf.last_name) as sales_rep
from sales.orders o
join sales.customers c
on o.customer_id = c.customer_id
join sales.order_items oi
on o.order_id= oi.order_id
join production.products pd
on oi.product_id=pd.product_id
join production.categories ct
on pd.category_id=ct.category_id
join sales.stores st
on o.store_id=st.store_id
join sales.staffs stf
on o.staff_id=stf.staff_id
group by o.order_id, concat(c.first_name,'',c.last_name), c.city, c.state,
o.order_date, pd.product_name, ct.category_name, st.store_name, concat(stf.first_name,'',stf.last_name)
"""
# Run and transform
df = pd.read_sql(sql_query, conn)
df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

# Save with timestamped filename
filename = f"monthly_report_{datetime.now().strftime('%Y_%m')}.csv"
df.to_csv(filename, index=False)
print(f"Exported: {filename}")
