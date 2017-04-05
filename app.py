import pyrebase
from pyrebase_config import *
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

@application.route('/', methods=['POST','GET'])
def root():
    response = twiml.Response()
    print(session)
    body=""

    try:
        body = request.form['Body'] #doesn't work here
        print(body)
    except:
        messages = client.messages.list()
        body = messages[0].body # TODO works for now but need to change
        print(body)

    request = body.lower().strip() # TODO comes from Twilio? getting error
    # Check to see if user has launched a query
    if request in ["x", "quit"]: # TODO set cookies to expire after X mins
        print("Removing session key \n")
        session.clear()
        response.messsage("session cleared")
        return str(response)

    if 'query' in session:
        try:
            response.redirect('query', methods=['POST']) # to direct to query/<arg> use ..arg=value
        except:
            print('redirect failed \n')# check where the resopnse from /query returns to
        return str(response)

    if request in ["balance", "bal", "b"]:
        message = return_balance('user1')
    elif request in ["query", "q"]:
        message = launch_query(response)
    else:
        message = "Usage: \n (1) 'balance', 'bal', or 'b' for "\
            "account balance. \n (2) 'query', 'q' for launching a query.\n"\
            " (3) 'quit'/'x' to end the session.\n"
            
    response.message(message)
    return str(response)

def return_balance(user):
    bal=get_balance(user)
    message = "balance\n"
    for k, v in bal.items():
        message += " {}: {} \n".format(k, v)
    return message

def launch_query(response):
    session['query'] = 'launched'
    print(session)
    message = "You just launched a query. Current options:\n"\
            "-b  get transactions before date MM/DD/YYYY\n"\
            "-a  get transactions after date MM/DD/YYYY\n"\
            "-o  get all transactions over $X\n"\
            "-u  get all transactions under $X\n"
    return str(message) # TODO can you redirect and return a message?

@application.route('/query', methods=['POST','GET'])
def query():
    response = twiml.Response()
    body=""

    try:
        #messages=client.messages.list()
        #body=messages[0].body
        body=request.form['Body'] # works
        body=body.lower().strip()
    except:
        print('error getting body')

# TODO add in filter functions now
    if session['query']=='launched':
        print('launched with body: \n')
        print(body)
        response.message('launched..\n'+str(body))


        return str(response)

    else:
        pass
        # Get

    # Redirect to /query which will prompt
    #response.redirect('/query', method='GET')
application.secret_key=secret_key
    #return str(response)

if __name__=="__main__":
    application.run(debug=True)

### TWILIO functions
