from plaid import Client
import requests
from plaid import errors as plaid_errors
from plaid.utils import json
import pprint
from config import *

client = Client(client_id='test_id', secret='test_secret', access_token='usertoken')
client.config({'url':'https://tartan.plaid.com'})

# Searching Institutions
# client.institution_all_search('tcf').json()
# client.institution(d['tcf-id']).json()

# Connect gives user transaction data and the user flow is:
# 1) Authenticaate user /connect
# 2) Submit MFA creds /connect/step
# 3) Get transactions /connect/get

def get_transactions():
    account_type = 'ins_100088'
    user = 'plaid_test'
    pwd = 'plaid_good'
    response = client.connect(account_type, {
        'username': user,
        'password': pwd
    })
    response = client.connect_step(account_type, 'tomato')
    return client.connect_get().json()['transactions']

def get_categories():
    pass #TODO return unique categories

# tcfaccess_token = "test_ins_100088"
# tcfclient = Client(client_id='test_id', secret='test_secret', access_token=tcfaccess_token)


# 1) client_id, secret, username, password, type, options
# try:
    # response = client.connect(account_type, {
        # 'username': 'plaid_test', # vs. plaid_test
        # 'password': 'plaid_good'
    # })
# except plaid_errors.PlaidError as e:
    # pass
# else:
    # if response.status_code == 200:
        # # User connected
        # print('response==200')
        # data = response.json()
        # print(data)
    # elif response.status_code == 201:
        # print('response==201')
        # print(response.json())
        # # MFA req'd
        # try:
            # mfa_response = answer_mfa(response.json())
        # except plaid_errors.PlaidError as e:
            # print('line 41')
            # pass
