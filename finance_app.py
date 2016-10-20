import pandas as pd
import itertools
import numpy as np
import os
import datetime
from config import *

# transactions.csv path defined in config file

# Load Data (Need outside of main() for testing)
df = pd.read_csv(dirs['dl'], parse_dates='Date', index_col='Date')


def compare_expenses(user_list, mint_list):
	return set(mint) - set(list(itertools.chain(*userlist)))


# Expenses that aren't accounted for
expenses_user = list(itertools.chain(*llexpenses)) # use itertools module to iterate over flattened list
expenses = df.Category.unique().tolist() # all categories
set(expenses_user) ^ set(expenses) # now write a test for this


if __name__ == '__main__':
	# Read Data in, index as datetime indices
	df = load_data() #.read_csv(dl_dir, parse_dates = 'Date', index_col = 'Date')
	#df = df.truncate(after = '07/01/2016')
	# Defining Groups
	food = ['Restaurants','Fast Food','Groceries','Food & Dining']
	coffee = ['Coffee Shops']
	transport = ['Public Transportation','Gas & Fuel', 'Rental Car & Taxi','Auto & Transport','Parking']
	travel = ['Travel','Coach Bus','Air Travel','Hotel']
	drinks = ['Alcohol & Bars']
	sport = ['Sports','Sporting Goods','Hobbies']
	shopping = ['Arts','Shopping', 'Electronics & Software','Music','Books','Clothing','Books & Supplies','Gift','Office Supplies','Mobile Phone','Pharmacy']
	entertainment = ['Event Tickets','Entertainment','Amusement','Arts', 'Movies & DVDs']
	fees = ['ATM Fee','Finance Charge','Fees & Charges','Bank Fee','State Tax','Federal Tax','Service Fee']
	misc = ['Service & Parts', 'Cash & ATM', 'Legal', 'Printing','Hair','Uncategorized','Business Services','Transfer for Cash Spending','Doctor','Eyecare','Misc Expenses']
	home = ['Home','Utilities','Mortgage & Rent','Rent', 'Home Improvement']
	edu = ['Education','Tuition']
	income = ['Interest Income', 'Paycheck', 'Income', 'Returned Purchase', 'Reimbursement']
	airbnb = ['Rental Income']
	hidden = ['Hide from Budgets & Trends', 'Transfer', 'Transfer for Cash Spending']

	# Create Nested List
	llexpenses = [food, coffee, transport, travel, drinks, sport, shopping, entertainment, fees, misc, home, edu, income, airbnb, hidden]
	mint = df.Category.unique().tolist()

	comparison = set(mint) - set(list(itertools.chain(*userlist)))


# EXTRA

# df.loc[df['col'].isin(list)] || df.['col'].isin(list).all(0)
#df['start date':'end date'