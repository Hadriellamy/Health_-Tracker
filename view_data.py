# Consultation et analyse

from db import get_connection

def view_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM health_data ORDER BY entry_date DESC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def average_steps():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT AVG(steps) FROM health_data")
    avg = cur.fetchone()[0]
    print(f"Average of steps : {avg:.2f}")
    cur.close()
    conn.close()

def delete_entry(entry_id):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("DELETE FROM health_data WHERE id = %s", (entry_id,)) #delete entry
        cur.execute("ALTER SEQUENCE health_data_id_seq RESTART WITH 1") #reinitialise a id 1
        conn.commit() #commit des changements
        print(f"Entry with ID {entry_id} deleted.")
    except Exception as e:
        print(f"Error while deleting : {e}")
    finally:
        cur.close()
        conn.close()    

