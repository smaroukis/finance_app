import pyrebase
from pyrebase_config import update_db, get_transactions
from config import twil_config
from twilio.rest import TwilioRestClient
from twilio import twiml
from flask import Flask, request, redirect, url_for

### Flask
application = Flask(__name__)

### Twilio: create client (sandbox/trial)
client = TwilioRestClient(twil_config['test_account_sid'], twil_config['test_auth_token'])
# message=client.messages.create(to=to_number, from=from_number, body=message)
# message=client.messages.create(to=twil_config['to_number'], from_=twil_config['from_number'], body=body)
# user="test"

@application.route('/default')
def default_info():
    request = body.lower().strip()
    # Return Current Balance and Prompt for Query
    response = twiml.Response()
    


### Filter Functions

def balance(user):


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

def get_categories(user, query=None):
    """Get all the categories from a certain query"""
    if query is None:
        # Get all
        trans=get_transactions(user)
    else
        trans=query
    return [i['category'] for i in  trans]

def filter_categories():
    pass

### TWILIO functions
