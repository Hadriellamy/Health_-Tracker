# Insertion des données

from db import get_connection
from datetime import date

def insert_data(entry_date, steps, calories, sleep_hours):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO health_data (entry_date, steps, calories, sleep_hours)
        VALUES (%s, %s, %s, %s)
    """, (entry_date, steps, calories, sleep_hours))
    conn.commit()
    cur.close()
    conn.close()
    print("Données ajoutées avec succès.")

#Ce code définit une fonction insert_data qui insère des données (date, pas, calories, heures de sommeil) dans une base PostgreSQL en se connectant grâce à get_connection.

