import pyrebase

# db updated i pyrebase_config
def filter_amt_over(user, amount):
    # assume the account has been instantiated
    # user here is the firebase db child, let's make it match the plaid username
    trans=get_transactions()
    is_over=[i for i in trans if i['amount']>amount]
    return is_over

def filter_amt_under():
    pass

def filter_date_range(user, start, end):
    # Returns inclusive list. Inputs should be YYYY-MM-DD string
    trans=get_transactions()
    data=[i for i in trans if i['date']<=end if i['date']>=start]
    return data

def get_categories():
    pass #TODO return unique categories

def filter_categories():
    pass
