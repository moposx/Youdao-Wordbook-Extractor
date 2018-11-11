#!/usr/bin/env python3

# Core extractor
# @author: Maxfield Wang (moposx)
# @date Nov 7, 2018

import logging
import os
import sqlite3


class Extractor():

    def __init__(self, *args, **kwargs):
        self.word_list = []
        self.normal_words = []

    def youdao_dict(self, db_file):
        print("Starting extracting the data...")
        conn = sqlite3.Connection(db_file)
        cursor = conn.cursor()
        try:
            # read the `spell` column from `notes`
            column = cursor.execute("select word from notes")
            for word in column:
                # Exclude dummy spellings.
                # They can be, e.g. Korean, pound signs "#"
                if not "#" in word[0]:
                    self.word_list.append(word[0])
        except sqlite3.DatabaseError as dbe:
            logging.exception(dbe)
            print("Oops!!!!!!!!!!!!!!!!!!!")
            print("Seems not a youdao dict's database, trying another extractor...")
            self.youdao_reciteword(db_file)

    def youdao_reciteword(self, db_file):
        conn = sqlite3.Connection(db_file)
        cursor = conn.cursor()
        try:
            # read the `word` column from `S_DictWord`
            column = cursor.execute("select word from S_DictWord")
            for word in column:     
                self.word_list.append(word[0])
                
            # also read the `word` column from `S_NormalWord`
            column = cursor.execute("select head from S_NormalWord")
            for word in column:
                self.normal_words.append(word[0])
            # There may be NULL value when retriving the words
            while None in self.normal_words:
                self.normal_words.remove(None)
        except sqlite3.DatabaseError as dbe:
            logging.exception(dbe)
            print("Oh no! Failed again... You may need to re-copy your database file.")

    def extract(self, db_file):
        self.youdao_dict(db_file)
        return sorted(self.word_list)
