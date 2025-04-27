Health Tracker

This project is a health tracking application that allows users to log data such as entry date, steps, calories burned, and hours of sleep. The data is then stored in a PostgreSQL database.

Features

Add health data: Allows users to log daily health information, such as steps, calories burned, and hours of sleep.

View data: Allows users to view stored health data.
Manage data: Includes features for deleting or displaying existing entries.
PostgreSQL database: Data is securely stored in a PostgreSQL database.
Requirements

To use this project, you must have Python 3.x installed on your machine, as well as PostgreSQL for the database.

Installation

Clone the repository:
git clone https://github.com/Hadriellamy/Health_-Tracker.git
cd Health_-Tracker


Create a virtual environment (optional but recommended):
python3 -m venv venv
source venv/bin/activate  

Set up PostgreSQL: Ensure that you have PostgreSQL installed and create a database for the project. You will need to modify the connection settings in the db.py file to match your PostgreSQL connection details.
Usage

Running the Application:

Start the main script main.py:
python main.py

The application runs directly in the terminal with a menu allowing you to view and delete health data stored in the database.


Project Structure:

- db.py: Contains the database connection functions and data insertion logic.
- insert_data.py: Handles inserting data into the database.
- view_data.py: Allows users to view and manage stored data.
- main.py: The main script that handles running the program via the terminal.
