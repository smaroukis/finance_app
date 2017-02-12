from plaid import Client
import requests
from plaid import errors as plaid_errors
from plaid.utils import json
import pprint

d = dict(institutions = 'https://tartan.plaid.com/institutions', client_id = '58991dd24e95b81dc56186c9', public_key = 'db10d55d87be474bb2087300c29653', secret = 'bdfef2d11864cf0b3f2f0e3aca16f5')
d['tcf-id'] = 'ins_100088'

client = Client(client_id='test_id', secret='test_secret', access_token='usertoken')
client.config({'url':'https://tartan.plaid.com'})


# Searching Institutions
client.institution_all_search('tcf').json()
client.institution(d['tcf-id']).json()


# Connect gives user transaction data and the user flow is:
# 1) Authenticaate user /connect
# 2) Submit MFA creds /connect/step
# 3) Get transactions /connect/get

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
account_type = 'ins_100088'
user = 'plaid_test'
pwd = 'plaid_good'
response = client.connect(account_type, {
    'username': user,
    'password': pwd
})
pprint.pprint(response.json())

# 2) for mfa response 201: client.connect_step(account_type, answer)
response = client.connect_step(account_type, 'tomato')
# 3) get Transactions
transactions = client.connect_get().json()['transactions']
print('--------------------------------------------------Printing Transactions ---------------------------------------------------')


for transaction in transactions:
    pprint.pprint(transaction['category'])


# print(response.json())
# tcfaccess_token = "test_ins_100088"
# tcfclient = Client(client_id='test_id', secret='test_secret', access_token=tcfaccess_token)
