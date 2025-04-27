# Connexion with Database

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="health_tracker_db",
        user="hadriellamy",     
        password="170423",  
        host="localhost"
    )
