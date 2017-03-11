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
def update_db(child_id):
    data=plaid_config.get_plaid_transactions()
    db.child(child_id).push(data)

def get_transactions(child_id):
    return db.child(child_id).get().val()
