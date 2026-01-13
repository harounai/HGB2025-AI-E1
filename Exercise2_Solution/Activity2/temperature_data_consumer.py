import time
from datetime import datetime, timedelta

import psycopg

DB_NAME = "mydb"
DB_USER = "postgres"
DB_PASSWORD = "postgrespw"
DB_HOST = "localhost"
DB_PORT = 4343

def fetch_avg_temp():
    ten_minutes_ago = datetime.now() - timedelta(minutes=10)

    with psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT AVG(temperature)
                FROM temperature_readings
                WHERE recorded_at >= %s
            """, (ten_minutes_ago,))
            return cur.fetchone()[0]

try:
    print("Starting the temperature consumer...")
    while True:
        avg_temp = fetch_avg_temp()
        if avg_temp is not None:
            print(f"{datetime.now()} - Average temperature last 10 minutes: {avg_temp:.2f} °C")
        else:
            print(f"{datetime.now()} - No data in last 10 minutes.")
        time.sleep(600)
except KeyboardInterrupt:
    print("Stopped consuming data.")
