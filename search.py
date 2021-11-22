import enchant
import sqlite3
import pandas as pd

def spell_check(word):
    conn=sqlite3.connect('test.db')
    df=pd.read_sql("SELECT * FROM unique_words",conn)
    conn.close()
    lda_dict={}
    for i in df['word']:
        lda= enchant.utils.levenshtein(word,i)
        lda_dict[i]=lda/len(i)
    lda_dict={k: v for k, v in sorted(lda_dict.items(), key=lambda item: item[1])}
    lda_dict2=[i for i in lda_dict.items() if i[1] < 0.75]
    return lda_dict2

def search(query):
    conn=sqlite3.connect('test.db')
    score=spell_check(query)

    r1,r2=[],[]
    w1=score[0][0]
    w2=score[1][0]

    df=pd.read_sql("SELECT * FROM index_table WHERE uniq_word=(?) AND value > 0",conn,params=(w1,))
    df2=pd.read_sql("SELECT * FROM index_table WHERE uniq_word=(?) AND value > 0",conn,params=(w2,))
    df.sort_values(by=['value'],inplace=True)
    df2.sort_values(by=['value'], inplace=True)
    df=pd.concat([df,df2])
    df=df[:20]
    return df
