import psycopg2
import csv
from dotenv import load_dotenv
import os
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def insert_data_to_db(file_path):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        # Read the CSV file
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cursor.execute(
                    """
                    INSERT INTO products (name, category, price, city)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (row["Product Name"], row["Category"], row["Price"], row["City"])
                )

        conn.commit()
        cursor.close()
        conn.close()
        print("Данные успешно загружены в базу данных.")
    except Exception as e:
        print(f"Ошибка: {e}")

csv_file_path = "kingfisher.csv"
insert_data_to_db(csv_file_path)
