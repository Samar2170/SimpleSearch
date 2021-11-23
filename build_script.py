import pandas as pd
from pandas.core.frame import DataFrame
from build_index import build_ds, score_data

def run():
    df=pd.read_csv('Feeder/retail_products.csv')
    names=[i for i in df['name']]
    ctgs=[i for i in df['cat_name'].unique()]
    ds1=build_ds(names,'name')
    ds2=build_ds(ctgs,'category')

    score1=score_data(ds1,names,'name')
    score2=score_data(ds2,ctgs,'category')
    



if __name__ == '__main__':
    run()
