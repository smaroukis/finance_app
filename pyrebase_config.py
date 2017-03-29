# post data to firebase app
import pyrebase
import config
import plaid_config

firebase = pyrebase.initialize_app(config.db_config)
db = firebase.database()

def db_init():
    firebase = pyrebase.initialize_app(config.db_config)
    db = firebase.database()
    return db
# note: will have to add some user auth function first


# For updating database
def update_db(user):
    response=plaid_config.get_plaid_response()
    db.child(user).push(response)

# For accessing database
def get_response(user):
    return db.child(user).get().val()

def get_transactions(user):
    response=get_response(user)
    balance = list(response.items())[0][1]['transactions'] # second index is 1 since 0 index is just the firebase key
    return balance

def get_balance(user):
    # maybe add account, only gets first for now
    response = get_response(user)
    balance = list(response.items())[0][1]['accounts'][0]['balance']
    return balance

## Filter Functions    
def filter_amt_over(user, amount):
    # assume the account has been instantiated
    # user here is the firebase db child, let's make it match the plaid username
    trans=get_transactions(user)
    data=[i for i in trans if i['amount']>amount]
    return data

def filter_amt_under(user, amount):
    trans=get_transactions(user)
    data=[i for i in trans if i['amount']<amount]
    return data

def filter_date_range(user, before, after):
    # Returns inclusive list. Inputs should be YYYY-MM-DD string
    trans=get_transactions(user)
    data=[i for i in trans if i['date']<=before if i['date']>=after]
    return data

def get_categories(user, query=None):
    """Get all the categories from a certain query"""
    if query is None:
        # Get all
        trans=get_transactions(user)
    else:
        trans=query
    return [i['category'] for i in  trans]

def filter_categories():
    pass
