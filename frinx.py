import json 
import os 
import psycopg2
import psycopg2.extras


import json
import psycopg2

conn = psycopg2.connect(
        host = os.getenv("FRINX_HOST", "localhost"),
        database = os.getenv("FRINX_DATABASE", "postgres"),
        user= os.getenv("FRINX_USER", "postgres"),
        password=os.getenv("FRINX_PASSWORD", "tutorial")
    )
cursor=conn.cursor
data = []
with open('data.json') as f:
    for line in f:
        data.append(json.loads(line))

fields = [
    "id" #SERIAL PRIMARY KEY,
    "connection" #INTEGER,
    "name" #VARCHAR(255) NOT NULL,
    "description" #VARCHAR(255),
    "config" #json,
    "type" #VARCHAR(50),
    "infra_type" #VARCHAR(50),
    "port_channel_id" #INTEGER,
    "max_frame_size" #INTEGER

]
for item in data:
    my_data = [item[field] for field in fields]
    for i, v in enumerate(my_data):
        if isinstance(v, dict):
            my_data[i] = json.dumps(v)
    insert_query = "INSERT INTO crm VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, tuple(my_data))
conn.close
cursor.close