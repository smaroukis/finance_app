from resources import *
import pandas as pd
import datetime


def main():
	# Read Recently Downloaded Transactions File & Expenses File
	recent = pd.read_csv(downloaded)
	expenses = pd.read_excel(expense_path)

	# Only need first hundred TODO set a last updated key or var
	expenses_df = expenses[:99]
	recent_df = recent[:99]

	# Return indexes of new df (recent) matching old df (expenses), Find contiguous indices, (like 5 in a row), find this
	#  row in old df, discard rest in new, discard top of old, concat
	count = 0
	indices = []
	for ix_recent, recent_data in recent_df.iterrows():
		for ix_expenses, expenses_data in expenses_df.iterrows():
			# if not found in any expenses_df row, print row
			if (expenses_data[1] == recent_data[1] and expenses_df[2] == recent_data[2]):  # TODO
				count += 1
		if count == 0:
			# print index_data, row_data[0], row_data[1], row_data[3]
			indices.append(ix_recent)

		count = 0

	# Get the rows of the recent data that are not repetitions
	newdf = recent_df.iloc[indices].sort_values('Date', ascending=False)

	# Todo Insert and Prepend inside the Excel File

	# Create a new file, in 'data-07-20' format
	output = newdf.append(expenses_df, ignore_index=True)
	foutname = 'data-' + str(datetime.datetime.today().month) + '-' + str(datetime.datetime.today().day)

	# Writeout
	newdf.to_csv(os.path.join(output_dir, foutname), index=False)


if __name__ == '__main__':
	main()
