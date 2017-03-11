import pyrebase
import plaid_app
from config import db_config

firebase = pyrebase.initialize_app(config.db_config)
db = firebase.database()

# Functions: Pull Data from Plaid, Push to firebase

# Get plaid data
# note: will have to add some user auth function first
def update_db(id)
    data=plaid_app.get_transactions()
    db.child(id).push(data)

# e.g. update_db("test")
