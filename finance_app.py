import pandas as pd
import itertools
import numpy as np
import os
import datetime
from config import *

# transactions.csv path defined in config file

# Load Data (Need outside of main() for testing)
df = pd.read_csv(dirs['transactions'], parse_dates=['Date'], index_col='Date')

# Current List of Expenses
food = ['Restaurants', 'Fast Food', 'Groceries', 'Food & Dining']
coffee = ['Coffee Shops']
transport = ['Public Transportation', 'Gas & Fuel', 'Rental Car & Taxi', 'Auto & Transport', 'Parking']
travel = ['Travel', 'Coach Bus', 'Air Travel', 'Hotel']
drinks = ['Alcohol & Bars']
sport = ['Sports', 'Sporting Goods', 'Hobbies']
shopping = ['Arts', 'Shopping', 'Electronics & Software', 'Music', 'Books', 'Clothing', 'Books & Supplies', 'Gift',
			'Office Supplies', 'Mobile Phone', 'Pharmacy']
entertainment = ['Event Tickets', 'Entertainment', 'Amusement', 'Arts', 'Movies & DVDs']
fees = ['ATM Fee', 'Finance Charge', 'Fees & Charges', 'Bank Fee', 'State Tax', 'Federal Tax', 'Service Fee']
misc = ['Service & Parts', 'Cash & ATM', 'Legal', 'Printing', 'Hair', 'Uncategorized', 'Business Services',
		'Transfer for Cash Spending', 'Doctor', 'Eyecare', 'Misc Expenses']
home = ['Home', 'Utilities', 'Mortgage & Rent', 'Rent', 'Home Improvement']
edu = ['Education', 'Tuition']
income = ['Interest Income', 'Paycheck', 'Income', 'Returned Purchase', 'Reimbursement']
airbnb = ['Rental Income']
hidden = ['Hide from Budgets & Trends', 'Transfer', 'Transfer for Cash Spending']

# Nested List of Expenses Should be all of the above (Todo: How to check variable names are in list?)
list_all_categories = [food, coffee, transport, travel, drinks, sport, shopping, entertainment, fees, misc, home, edu, income,
			  airbnb, hidden]

# Expenses that aren't accounted for
expenses_user = list(itertools.chain(*list_all_categories)) # use itertools module to iterate over flattened list
expenses = df.Category.unique().tolist() # all categories


# Monthly Budgets
def budgets():
	bdgts = {'food': 400, 'coffee':25, 'sport':75, 'shopping':50 }

def last_wk_data(_df):
	last_wk = datetime.


def compare_expenses(superset, subset):
	# Return Categories that are in Mint but not User Defined
	return set(superset) - set(subset)


if __name__ == '__main__':
	#df = df.truncate(after = '07/01/2016')

	# Print
	# Just Compare
	expenses_diff = compare_expenses(expenses, expenses_user)
	print(expenses_diff)
# EXTRA

# df.loc[df['col'].isin(list)] || df.['col'].isin(list).all(0)
#df['start date':'end date'