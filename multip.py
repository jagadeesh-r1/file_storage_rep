import time
import sys
import pandas as pd
import multiprocessing
from multiprocessing import Pool

def checking_function(dataset):
    dataset.reset_index(drop=True, inplace=True)
    rows = len(dataset.index)
    for ind in dataset.index:
        image = dataset['b'][ind]
        splited1 = image.split('.')
        splited = splited1[0].split('/')[-1]
        splited = splited.split('_')
        if splited[1].startswith('3'):
            if ind <= rows:
                print(ind)
                dataset = dataset[dataset.b != image]
            else:
                print('in else',ind,rows)
    return dataset

if __name__ == '__main__':
    columns = ['a','b','c']

    df = pd.read_csv('L0_Imagedata.csv',names=columns)

    num_processes = 10

    chunk_size = int(df.shape[0]/num_processes)

    chunks = [df.iloc[i:i + chunk_size,:] for i in range(0, df.shape[0], chunk_size)]

    pool = Pool(processes=num_processes)

    result = pool.map(checking_function, chunks)

    print("execution completed")
     
    skip_list = []
    for i in range(0,len(result)):
        if result[i].empty:
            skip_list.append(i)

    df2 = pd.DataFrame()

    for i in range(len(result)):
        if i not in skip_list:
            df2 = pd.concat([result[i],df2],ignore_index=True,) 
            df2.reset_index(drop=True, inplace=True)

    print('out of loop')


    df2.to_csv('result.csv',index=False,columns=None)

    print("done")
    pool.terminate()
    pool.join()