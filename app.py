from __future__ import print_function

import os.path
import pandas as pd
from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1wxqVxx7Dd0U8prMuGMPbBxsYHPsLJXwM4nl_87UJJSI'
SERVICE_ACCOUNT_FILE = 'secrets/token.json'
SAMPLE_RANGE_NAME = 'form_participants'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        with build('sheets', 'v4', credentials=credentials) as service:
            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
            values = result['values']
            df = pd.DataFrame()
            # if not values:
            #     print('No data found.')
            #     return

            # print('Name, Major:')
            # for row in values:
            #     # Print columns A and E, which correspond to indices 0 and 4.
            #     print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()