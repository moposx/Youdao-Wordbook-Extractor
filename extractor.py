#!/usr/bin/env python3

# Core extractor
# @author: Maxfield Wang
# @date Nov 7, 2018

import logging
import os
import sqlite3


word_list = []

def youdao_dict(db_file):
    conn = sqlite3.Connection(db_file)
    cursor = conn.cursor()
    try:
        # read the `spell` column from `notes`
        column = cursor.execute("select word from notes")
        for word in column:
            # Exclude dummy spellings.
            # They can be, e.g. Korean, pound signs "#"
            if not "#" in word[0]:
                word_list.append(word[0])
    except sqlite3.DatabaseError as dbe:
        logging.exception(dbe)
        print("Oops!!!!!!!!!!!!!!!!!!!")
        print("Seems not youdao dict's database, trying another extractor...")
        youdao_reciteword(db_file)


def youdao_reciteword(db_file):
    conn = sqlite3.Connection(db_file)
    cursor = conn.cursor()
    try:
        # read the `word` column from `S_DictWord`
        column = cursor.execute("select word from S_DictWord")
        for word in column:
            word_list.append(word[0])
    except sqlite3.DatabaseError as dbe:
        logging.exception(dbe)
        print("Oh no! Failed again... You may need re-copy your database file.")


def extract(db_file):
    youdao_dict(db_file)
    return word_list