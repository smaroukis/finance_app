import pyrebase
from pyrebase_config import update_db, get_transactions, get_balance
from config import twil_config
from twilio.rest import TwilioRestClient
from twilio import twiml
from flask import Flask, request, redirect, url_for

### Flask
application = Flask(__name__)

### Twilio: create client (sandbox/trial)
client = TwilioRestClient(twil_config['account_sid'], twil_config['auth_token'])
# message=client.messages.create(to=to_number, from=from_number, body=message)
# message=client.messages.create(to=twil_config['to_number'], from_=twil_config['from_number'], body=body)
# user="test"

@application.route('/')
def root():
    # TODO user session cookies
    response = twiml.Response()

    if 'hopslam' is in session:

    try:
        body = request.form['Body']
        print(body)
    except:
        print("couldn't find message body")
        messages = client.messages.list()
        body = messages[0].body

    request = body.lower().strip() # TODO comes from Twilio? getting error
    if request in ["balance", "bal", "b"]:
        message = return_balance('user1')
    elif request in ["query", "q"]:
        message = launch_query('user1')
    else:
        message = "Usage: \n (1) 'balance', 'bal', or 'b' for "\
            "account balance. \n (2) 'query', 'q' for launching a query.\n"

    response.message(message)
    return str(response)

def return_balance(user):
    bal=get_balance(user)
    message = "balance\n"
    for k, v in bal.items():
        message += " {}: {} \n".format(k, v)
    return message

def launch_query(user):
    response = twiml.Response()
    # TODO create session cookie to put in root route for query
    response.redirect(url_for('query'))
    session['hopslam'] = True
    return str(response)

    # Redirect to /query which will prompt
    #response.redirect('/query', method='GET')

    #return str(response)

# use session key here somewhere
# use url redirect

#def bank_query():

### Filter Functions

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

if __name__=="__main__":
    application.run(debug=True)
### TWILIO functions
