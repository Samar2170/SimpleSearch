import sqlite3
from build_index import build_ds

def update_index(array):
    uniq_words=build_ds(array)
    
    conn=sqlite3.connect('test.db')
    rows=conn.execute("SELECT * FROM uniq_words")
    for i,u in enumerate(uniq_words):
        conn.execute("INSERT INTO unique_words (id,word) VALUES (?,?)",(i,u))
    db_uniq_words=[]
