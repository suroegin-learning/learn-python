#!/usr/bin/env python3

"""
https://github.com/utkuufuk/budget-cli/
"""

import sys

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

if __name__ == '__main__':

    # Get command and args
    command = sys.argv[1]  # 'id', 'url', 'expense', 'income'
    arg = sys.argv[2]
    if command == 'url':
        start = arg.find("spreadsheets/d/")
        end = arg.find("/edit/#")

    # Write spreadsheet ID and exit if command is 'id' or 'url'
    if command in ['id', 'url']:
        spreadsheet_id = arg if command == 'id' else arg[(start + 15):end]
        with open("spreadsheet.id", 'w') as f:
            f.write(spreadsheet_id)
        sys.exit(0)

    # Parse transaction parameters (date, amount, descr., category)
    entry = arg.split(',')

    # Read spreadsheet ID from file if command is 'expense' or 'income'
    with open('spreadsheet.id') as f:
        spreadsheet_id = f.read()



    # Authorize
    store = file.Storage('token.json')
    creds = store.get()
    service = build('sheets', 'v4', http=creds.authorize(Http()))
