#!/usr/bin/env python3

import sqlite3
import os

def extract(db_file):
    conn = sqlite3.Connection(db_file)
    cursor = conn.cursor()

    word_list = []

    # read the `spell` column
    column = cursor.execute("select word from notes")
    for word in column:
        # Exclude dummy spellings.
        # They can be, e.g. Korean, pound signs "#"
        if not "#" in word[0]:
            word_list.append(word[0])
    return sorted(word_list)

