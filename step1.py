from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///data/masterschoolDB.sqlite3')

with engine.connect() as connection:
    results1 = connection.execute(text('SELECT * FROM books WHERE publication_year > 2000'))
    rows1 = results1.fetchall()

    results2 = connection.execute(text('SELECT * FROM books WHERE publication_year > 2000'))
    rows2 = results2.fetchall()

    results3 = connection.execute(text('SELECT title, authors.name from books LEFT JOIN authors ON books.author_id = authors.author_id'
                                      ' WHERE books.publication_year > 2000'))
    rows3 =results3.fetchall()

    print(f"task1: ")
    print(results1.keys())
    print(type(rows1))
    for row1 in rows1:
        print(row1._mapping)

    print(f"\n\ntask2: Returned {len(rows2)} results:")
    print(results2.keys())
    print(type(rows2))
    for row2 in rows2:
        print(row2._mapping)

    print(f"\n\ntask 3: Returned {len(rows3)} results:")
    print(results3.keys())
    print(type(rows3))
    for row3 in rows3:
        print(f"{row3._mapping["title"]} ({row3._mapping["name"]})")