import pandas as pd 
import sqlite3

remove=['\n','"',',','\\','/','+','-',')','(']

def lemmatize(arg):
    import re 
    string = re.sub(r'[^\w\s]','',arg)
    return string   
        
def build_ds(array):
    all_words=[]
    for prod in array:
        all_strs=[p for p in prod.split(' ') if p not in remove]
        for a in all_strs:
            a=lemmatize(a)
            a=a.replace('\n','')
            all_words.append(a.lower())
    uniq_words=list(set(all_words))       
    
    
    drops=[]
    for i,u in enumerate(uniq_words):
        if len(u)<=2:
            drops.append(i)

        else:
            pass
        try:
            u=int(u)
            drops.append(i)

        except:
            pass
    drops.reverse()
    for d in drops:
        uniq_words.pop(d)
    
    conn=sqlite3.connect('test.db')
    for i,u in enumerate(uniq_words):
        conn.execute("INSERT INTO unique_words (id,word) VALUES (?,?)",(i,u))
    conn.commit()
    conn.close()        
    return uniq_words       

def score_data(uniq, array):
    all_dict={}
    for prod in array:
        words=[p for p in prod.split(' ') if p not in remove]
        words2=[]
        for w in words:
            w=lemmatize(w)
            w=w.replace('\n','')
            w=w.lower()
            words2.append(w)
        all_dict[prod]=words2 
    udict={}    
    for u in uniq:
        udict[u]={}
        for a in all_dict.keys():
            udict[u][a]=0
        for a in all_dict.keys():
            try:
                udict[u][a]+=(all_dict[a].index(u)+1)
            except:
                pass
    
    conn=sqlite3.connect('test.db')
    count=0
    for u in udict.keys():
        for a in udict[u].keys():
            conn.execute("INSERT INTO index_table (id,string,uniq_word,value) VALUES (?,?,?,?)",(count,a,u,udict[u][a]))
            count+=1
    conn.commit()    
    return udict    