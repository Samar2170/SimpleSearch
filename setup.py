import sqlite3

conn=sqlite3.connect('test.db')
conn.execute('''CREATE TABLE IF NOT EXISTS unique_words
                (id INT PRIMARY KEY NOT NULL,
                word TEXT NOT NULL);''')
# create table with foriegn key relationship           

conn.execute('''CREATE TABLE IF NOT EXISTS index_table
                (id INT PRIMARY KEY NOT NULL,
                string TEXT NOT NULL,
                uniq_word TEXT NOT NULL,
                value INT NOT NULL,
                FOREIGN KEY (uniq_word) REFERENCES unique_words(word));''')

conn.close()