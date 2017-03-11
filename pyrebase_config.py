# post data to firebase app
import pyrebase
from config import db_config
import plaid_config

firebase = pyrebase.initialize_app(db_config)
db = firebase.database()
# note: will have to add some user auth function first
def update_db(child_id)
    data=plaid_config.get_transactions()
    db.child(child_id).push(data)
