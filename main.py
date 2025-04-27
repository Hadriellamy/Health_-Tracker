from insert_data import insert_data
from view_data import view_all, average_steps, delete_entry
from datetime import datetime
from utils import input_int, input_float


def main():
    print("\nWelcome to the Health Tracker")

    while True:
        print("""
1. Add an entry
2. View all entry
3. Average steps
4. Delete an entry
5. Exit             
              
        """)
        choice = input("Choice : ")

        if choice == "1":
            date_str = input("Date (YYYY-MM-DD) [or empty for today] : ")
            if date_str == "":
                entry_date = datetime.today().date()
            else:
                try:
                    entry_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                except ValueError:
                    print("Invalid date.")
                    continue

            steps = input_int("Number of steps: ")
            calories = input_int("Calories consumed : ")
            sleep_hours = input_float("Hours of sleep : ")

            insert_data(entry_date, steps, calories, sleep_hours)

        elif choice == "2":
            view_all()

        elif choice == "3":
            average_steps()

        elif choice == "4":
            entry_id = input("ID de l'entrée à supprimer : ")
            delete_entry(int(entry_id))
           
        elif choice == "5":
            print("See you soon !")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
