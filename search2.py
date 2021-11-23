import sqlite3
from search import spell_lda, search
import numpy as np
from functools import reduce

def parse_query(query):
    query = query.lower()
    query = query.split(' ')
    if len(query) == 1:
        query_bit = query[0]
        return query_bit
    return query

def mw_search(query):
    query_bit = parse_query(query)
    if isinstance(query_bit, str):
        score=search(query_bit)
        return score
    else:
        score_arr=[]
        for i in query_bit:
            score_arr.append(search(i))
        print(type(score_arr[0]))
        ids1=[s for s in score_arr[0]['string']]
        ids2=[s for s in score_arr[1]['string']]
        ids=list(set(ids1).intersection(ids2))



        
        return ids