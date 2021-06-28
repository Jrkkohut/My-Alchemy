import json 
import os 
import psycopg2
import psycopg2.extras

with open("data.json", "r", encoding='utf-8') as f:
    data = json.load(f)

conn = psycopg2.connect(
        host = os.getenv("FRINX_HOST", "localhost"),
        database = os.getenv("FRINX_DATABASE", "postgres"),
        user= os.getenv("FRINX_USER", "postgres"),
        password=os.getenv("FRINX_PASSWORD", "tutorial")
    )
cursor=conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS frinx (id serial PRIMARY KEY,connection INTEGER,name VARCHAR(255),type VARCHAR(50),port_chanel_id INTEGER,max_frame_size INTEGER) "
)
