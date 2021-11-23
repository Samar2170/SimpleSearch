import pandas as pd 
import sqlite3

remove=['\n','"',',','\\','/','+','-',')','(']

def lemmatize(arg):
    import re 
    string = re.sub(r'[^\w\s]','',arg)
    return string   
        
def build_ds(array, sel):
    all_words=[]
    for prod in array:
        if isinstance(prod,str):
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
    c=conn.cursor()
    c.execute("SELECT COUNT(*) FROM unique_words")
    last_entry=c.fetchone()
    count=last_entry[0]+ 1

    for i,u in enumerate(uniq_words):
        i=count+i
        conn.execute("INSERT INTO unique_words (id,word, selection) VALUES (?,?,?)",(i,u,sel))
    conn.commit()
    conn.close()        
    return uniq_words       

def score_data(uniq, array,sel):
    all_dict={}
    for prod in array:
        if isinstance(prod,str):
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
    for u in uniq:       
        for a in all_dict.keys():    
                if udict[u][a]==0:
                    udict[u].pop(a)
                    
    conn=sqlite3.connect('test.db')
    c=conn.cursor()
    c.execute("SELECT COUNT(*) FROM index_table")
    last_entry=c.fetchone()
    count=last_entry[0]+ 1
    for u in udict.keys():
        for a in udict[u].keys():
            conn.execute("INSERT INTO index_table (id,string,uniq_word,value, indx_selection) VALUES (?,?,?,?,?)",(count,a,u,udict[u][a],sel))
            count+=1
    conn.commit()    
    return udict    

