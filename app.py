import pyrebase
from pyrebase_config import update_db, get_transactions

# db updated i pyrebase_confi
# user="test"

def filter_amt_over(user, amount):
    # assume the account has been instantiated
    # user here is the firebase db child, let's make it match the plaid username
    trans=get_transactions(user)
    data=[i for i in trans if i['amount']>amount]
    return data

def filter_amt_under():
    trans=get_transactions(user)
    data=[i for i in trans if i['amount']>amount]
    return data

def filter_date_range(user, start, end):
    # Returns inclusive list. Inputs should be YYYY-MM-DD string
    trans=get_transactions(user)
    data=[i for i in trans if i['date']<=end if i['date']>=start]
    return data

def get_categories():
    pass #TODO return unique categories

def filter_categories():
    pass
