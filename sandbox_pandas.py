import plaid_app
from pprint import pprint as pp
import pandas as pd
from pandas.io.json import json_normalize

def flatten_json(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

transactions = plaid_app.get_transactions()
pp(transactions)

keepkeys = ['_account', '_id', 'amount', 'category', 'date', 'name', 'pending']
clean = []
for d in transactions:
    clean = [ clean, {key: d[key] for key in keepkeys }]
# TODO fails because "category" is a list of categories
clean = { key: sbtrans[key] for key in keepkeys }
type(sbtrans[0])

pp(transactions)

# This will create a row flattening all of the (1) transaction data
for i in range(0,len(transactions)):
    flat = flatten_json(transactions[i])
    new_row = json_normalize(flat)

new_row


# json_normalize(transactions, '_id', ['_account', 'amount', 'date'])
