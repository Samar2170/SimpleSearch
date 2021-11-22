import pandas as pd
from build_index import build_ds, score_data

def run():
    sts=open('Feeder/car_acessories.txt')
    prods=sts.readlines()
    uniq=build_ds(prods)
    udict=score_data(uniq,prods)


if __name__ == '__main__':
    run()
