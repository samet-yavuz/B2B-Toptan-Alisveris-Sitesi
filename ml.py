from mlxtend.frequent_patterns import fpgrowth,association_rules
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
import getdata

def set_dataset(id):
    dataset = []
    faturalar = getdata.faturalar(id)
    for i in faturalar:
        dataset.append(getdata.fatura_icerik(i))
    return dataset

def run(id):
    dataset = set_dataset(id)
    
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    fp = fpgrowth(df, min_support=0.2, use_colnames=True, max_len=1).sort_values(by='support', ascending=True)
    
    return fix_out(fp)

def fix_out(fp):
    array =[]
    for i in range (5):
        array.append(next(iter(fp['itemsets'].values[i])))
    return array
    