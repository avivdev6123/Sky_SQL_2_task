from sqlalchemy import create_engine, text
from pathlib import Path
import os
import sys

year = input('Enter a valid year (e.g 2007): ')
params = {
    "year" : year
}

engine = create_engine('sqlite:///data/masterschoolDB.sqlite3')
with engine.connect() as connection:


    # Task 2:
    exercise1 = connection.execute(text('SELECT * FROM books WHERE publication_year = :year'), params)
    results1 = exercise1.fetchall()
    for row in results1:
        print(row._mapping)

    # Bonus - task 2:
    title_key = input("\nenter the full book title or part of it: ")
    params2 = {
        "title": f"%{title_key}%"
    }

    bonus1 = connection.execute(text('SELECT * FROM books WHERE title LIKE :title'), params2)
    results_bonus1 = bonus1.fetchall()
    for row in results_bonus1:
        print(row._mapping)

    # Bonus - task 2:
    year_range_start = input("\nsearch books by publication time range - From Year: ")
    year_range_end = input("search books by publication time range - Until Year: ")
    params3 = {
        "year_range_start": year_range_start,
        "year_range_end": year_range_end
    }

    bonus2 = connection.execute(text('SELECT * FROM books WHERE publication_year BETWEEN :year_range_start AND :year_range_end'), params3)
    results_bonus2 = bonus2.fetchall()
    for row in results_bonus2:
        print(row._mapping)


    #Bonus - task 3:
    print("\nSearch books - fill in the following filters in order to minimise your search")

    year_range_start2 = input("\nsearch books by publication time range - From Year: ")
    year_range_end2 = input("search books by publication time range - Until Year: ")
    title2 = input("enter the book title (fill in full or partial title): ")
    params4 = {
        "year_range_start": year_range_start2,
        "year_range_end": year_range_end2,
        "title": f"%{title2}%"
    }

    bonus3 = connection.execute(text('SELECT * FROM books WHERE publication_year BETWEEN :year_range_start AND :year_range_end AND title like :title'), params4)
    results_bonus3 = bonus3.fetchall()
    for row3 in results_bonus3:
        print(row3._mapping)