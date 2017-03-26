import pyrebase
from pyrebase_config import update_db, get_transactions, get_balance
from config import twil_config, secret_key
from twilio.rest import TwilioRestClient
from twilio import twiml
from flask import Flask, request, redirect, url_for, session

### Flask
application = Flask(__name__)
### Twilio: create client (sandbox/trial)
client = TwilioRestClient(twil_config['account_sid'], twil_config['auth_token'])
# message=client.messages.create(to=to_number, from=from_number, body=message)
# message=client.messages.create(to=twil_config['to_number'], from_=twil_config['from_number'], body=body)
# user="test"

@application.route('/')
def root():
    response = twiml.Response()



    try:
        body = request.form['Body']
        print(body)
    except:
        print("couldn't find message body")
        messages = client.messages.list() # TODO ask Al what this does
        body = messages[0].body

    request = body.lower().strip() # TODO comes from Twilio? getting error

    print('session is: \n')
    print(session)
    # Check to see if user has launched a query
    if 'query' in session:
        try:
            response.redirect('query') # to direct to query/<arg> use ..arg=value
        except:
            print("Error on redirect, removing session key")
            session.pop('query', None)
        return str(response)

    if request in ["balance", "bal", "b"]:
        message = return_balance('user1')
    elif request in ["query", "q"]:
        message = launch_query()
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

def launch_query():
    session['query'] = 'launched'
    print(session)
    message = "You just launched a query. Current options:\n"\
            "-b  get transactions before date MM/DD/YYYY\n"\
            "-a  get transactions after date MM/DD/YYYY\n"\
            "-o  get all transactions over $X\n"\
            "-u  get all transactions under $X\n"
    return message # TODO can you redirect and return a message?

    # Redirect to /query which will prompt
    #response.redirect('/query', method='GET')
application.secret_key=secret_key
    #return str(response)

if __name__=="__main__":
    application.run(debug=True)
### TWILIO functions
