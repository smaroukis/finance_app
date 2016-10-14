import unittest
import itertools

class BasicTest(unittest.TestCase):
	def test_all_categories(self):
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
		llexpenses = [food, coffee, transport, travel, drinks, sport, shopping, entertainment, fees, misc, home, edu, income, airbnb, hidden]
		mint = df.Category.unique().tolist()

		comparison = set(mint) - set(list(itertools.chain(*llexpenses)))

		self.AssertEqual(comparison, set([]))

if __name__ == '__main__':
	unittest.main()