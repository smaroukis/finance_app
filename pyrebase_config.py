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
    return db.child(user).get().val()]

def get_transactions(user):
    response=get_response(user)
    balance = list(response.items())[0][1]['transactions'] # second index is 1 since 0 index is just the firebase key
    return balance

def get_balance(user):
    # maybe add account, only gets first for now
    response = get_response(user)
    balance = list(response.items())[0][1]['accounts'][0]['balance']
    return balance
