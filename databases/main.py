#!/usr/bin/env python3

import sqlite3

with sqlite3.connect('gta.db') as connection:
    release_list = [
        (1997, "Grand Theft Auto", "state of New Guernsey"), (1999, "Grand Theft Auto 2", "Anywhere USA"), (2001, "Grand Theft Auto III ", "Liberty City"), (2002, "Grand Theft Auto: Vice City ",
                                                                                                                                                             "Vice City"), (2004, "Grand Theft Auto: San Andreas ", "state of San Andreas"), (2008, "Grand Theft Auto IV ", "Liberty City"), (2013, "Grand Theft Auto V ", "Los Santos")
    ]
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE gta (release_year integer, release_name text, city text)")
    cursor.executemany("INSERT INTO gta VALUES(?,?,?)", release_list)

    for row in cursor.execute("SELECT * FROM gta"):
        print(row)
