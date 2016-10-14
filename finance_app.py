import pandas as pd
import itertools
import numpy as np
import os
import datetime
from config import *

# Set Directory Paths/Keys
dl_dir = dirs['dl']
out_dir = dirs['out']

# Todo: Autodownload

# Read Data in, index as datetime indices
df = pd.read_csv(dl_dir, parse_dates = 'Date', index_col = 'Date')
#df = df.truncate(after = '07/01/2016')

# Defining Groups
food = ['Restaurants','Fast Food','Groceries','Food & Dining']
coffee = ['Coffee Shops']
transport = ['Public Transportation','Gas & Fuel', 'Rental Car & Taxi','Auto & Transport','Parking']
travel = ['Travel','Coach Bus','Air Travel','Hotel']
drinks = ['Alcohol & Bars']
sport = ['Sports','Sporting Goods','Hobbies']
shopping = ['Electronics & Software','Music','Books','Clothing','Books & Supplies','Gift','Office Supplies','Mobile Phone'] # should it be a set?
entertainment = ['Event Tickets','Entertainment','Amusement','Arts']
fees = ['ATM Fee','Finance Charge','Fees & Charges','Bank Fee','State Tax','Federal Tax','Service Fee']
misc = ['Printing','Hair','Uncategorized','Business Services','Transfer for Cash Spending','Doctor','Eyecare','Misc Expenses']
home = ['Home','Utilities','Mortgage & Rent','Rent', 'Home Improvement']
edu = ['Education','Tuition']
llexpenses = [food, coffee, transport, travel, drinks, sport, shopping, entertainment, fees, misc, home, edu]
llnames = ['food','coffee','transport','travel','drinks','sport','shopping','entertainment','fees','misc', 'home', 'edu']
hidden = ['Hide from Budgets & Trends']
# More ideas: Recurring, Software, Big Spends


# Expenses that aren't accounted for
expenses_user = list(itertools.chain(*llexpenses)) # use itertools module to iterate over flattened list
expenses = df.Category.unique().tolist() # all categories
set(expenses_user) ^ set(expenses) # now write a test for this



# df.loc[df['col'].isin(list)] || df.['col'].isin(list).all(0)
#df['start date':'end date']