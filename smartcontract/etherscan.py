
from etherscan.accounts import Account
import json


address = '0x491179f035fdf219798d186f576abdf842c14ca6'

api = Account(address=address, api_key='ZD8EBE2I7GCGG8Y8YNY2PMD2GT3P2UIJ55')
transactions = api.get_transaction_page(page=1, offset=10000, sort='des')
print(transactions)